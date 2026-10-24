"""Reproducible toy comparison; does not establish a general MoE advantage."""
import json
import torch
from .model import AletheonClassifier
from .moe import TriVectorMoE


def labels(x):
    return torch.bucketize(x[:, 0] + .5 * x[:, 1], torch.tensor([-.5, .5]))


def main():
    torch.set_num_threads(1)
    x = torch.randn(240, 8, generator=torch.Generator().manual_seed(42))
    xt = torch.randn(1000, 8, generator=torch.Generator().manual_seed(43))
    y, yt = labels(x), labels(xt)
    results = []
    for seed in (42, 44, 45):
        for name, constructor in [('dense', AletheonClassifier), ('sparse', TriVectorMoE)]:
            torch.manual_seed(seed)
            model = constructor()
            optimizer = torch.optim.Adam(model.parameters(), lr=.01)
            for _ in range(30):
                optimizer.zero_grad()
                loss = torch.nn.functional.cross_entropy(model(x), y)
                loss.backward()
                optimizer.step()
            model.eval()
            with torch.no_grad():
                logits = model(xt)
                assert torch.isfinite(logits).all()
                row = dict(model=name, seed=seed, epochs=30,
                           parameters=sum(p.numel() for p in model.parameters()),
                           loss=torch.nn.functional.cross_entropy(logits, yt).item(),
                           accuracy=(logits.argmax(-1) == yt).float().mean().item())
                if name == 'sparse':
                    indices, _ = model.route(xt)
                    row['routed_selection_counts'] = indices.flatten().bincount(minlength=3).tolist()
                results.append(row)
    print(json.dumps(dict(task='synthetic threshold classification', train_samples=240,
                          train_seed=42, heldout_samples=1000, heldout_seed=43,
                          majority_accuracy=yt.bincount().max().item()/len(yt),
                          results=results), indent=2))


if __name__ == '__main__':
    main()
