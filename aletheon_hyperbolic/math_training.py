"""Image-inspired saddle classification; equations, not pixels, supply labels."""
import json
import math
import torch
from .model import AletheonClassifier
from .moe import TriVectorMoE

BAND = .1


def saddle_labels(xy):
    """Class indices 0/1/2 mean negative/band/positive height, not expert IDs."""
    z = xy[:, 0].square() - xy[:, 1].square()
    return torch.where(z < -BAND, 0, torch.where(z > BAND, 2, 1))


def reference_geometry():
    """Twelve reference points plus internal center label 13; artistic mapping."""
    points = []
    for i in range(12):
        theta = 2*math.pi*i/12
        x, y = math.cos(theta), math.sin(theta)
        points.append(dict(label=i+1, x=x, y=y, z=x*x-y*y))
    points.append(dict(label=13, x=0., y=0., z=0.))
    return points


def make_dataset(samples, seed):
    if isinstance(samples, bool) or not isinstance(samples, int) or samples <= 0:
        raise ValueError('samples must be a positive integer')
    generator = torch.Generator().manual_seed(seed)
    radius = torch.rand(samples, generator=generator).sqrt()
    theta = torch.rand(samples, generator=generator)*2*math.pi
    xy = torch.stack((radius*theta.cos(), radius*theta.sin()), dim=-1)
    # Sector labels are metadata only, never model inputs or targets.
    sectors = torch.floor(theta/(2*math.pi)*12).long().clamp_max(11)
    return xy, saddle_labels(xy), sectors


def main():
    torch.set_num_threads(1)
    train, labels, train_sectors = make_dataset(1200, 1001)
    test, targets, test_sectors = make_dataset(1200, 1002)
    results = []
    for seed in (42, 44, 45):
        for name, make_model in [
            ('original', lambda: AletheonClassifier(input_dim=2)),
            ('sparse', lambda: TriVectorMoE(input_dim=2)),
        ]:
            torch.manual_seed(seed)
            model = make_model()
            optimizer = torch.optim.Adam(model.parameters(), lr=.01)
            for _ in range(200):
                optimizer.zero_grad()
                loss = torch.nn.functional.cross_entropy(model(train), labels)
                if not torch.isfinite(loss):
                    raise ValueError('Nonfinite training loss')
                loss.backward()
                optimizer.step()
            model.eval()
            with torch.no_grad():
                logits = model(test)
                if not torch.isfinite(logits).all():
                    raise ValueError('Nonfinite test predictions')
                predictions = logits.argmax(-1)
                confusion = torch.bincount(targets*3+predictions, minlength=9).reshape(3, 3)
                row = dict(model=name, initialization_seed=seed,
                    parameters=sum(p.numel() for p in model.parameters()),
                    loss=torch.nn.functional.cross_entropy(logits, targets).item(),
                    accuracy=(predictions == targets).float().mean().item(),
                    confusion_true_rows_predicted_columns=confusion.tolist())
                if name == 'sparse':
                    indices, _ = model.route(test)
                    row['expert_selection_counts'] = indices.flatten().bincount(minlength=3).tolist()
                results.append(row)
    print(json.dumps(dict(
        task='saddle height classification from x and y', equation='z = x*x - y*y',
        source='analytic synthetic data; illustration supplies visual inspiration only',
        class_meanings=['z < -0.1', '-0.1 <= z <= 0.1', 'z > 0.1'],
        train_samples=1200, test_samples=1200, train_seed=1001, test_seed=1002,
        epochs=200, learning_rate=.01, optimizer='Adam',
        train_class_counts=labels.bincount(minlength=3).tolist(),
        test_class_counts=targets.bincount(minlength=3).tolist(),
        train_sector_counts=train_sectors.bincount(minlength=12).tolist(),
        test_sector_counts=test_sectors.bincount(minlength=12).tolist(),
        majority_test_accuracy=targets.bincount().max().item()/len(targets),
        reference_geometry=reference_geometry(), results=results,
        checkpoint_saved=False,
    ), indent=2))


if __name__ == '__main__':
    main()
