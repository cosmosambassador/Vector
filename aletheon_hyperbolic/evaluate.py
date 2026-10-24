"""Held-out synthetic smoke evaluation; no real-world performance claims."""
import argparse
import json
import torch
from .load import load_checkpoint


def evaluate(path):
    model = load_checkpoint(path)
    generator = torch.Generator().manual_seed(43)
    x = torch.randn(1000, 8, generator=generator)
    y = torch.bucketize(x[:, 0] + 0.5 * x[:, 1], torch.tensor([-0.5, 0.5]))
    with torch.no_grad():
        logits = model(x)
        loss = torch.nn.functional.cross_entropy(logits, y)
        if not torch.isfinite(logits).all() or not torch.isfinite(loss):
            raise ValueError("Nonfinite held-out output")
        return {
            "dataset": "synthetic feature-threshold task",
            "heldout_seed": 43,
            "samples": len(y),
            "class_counts": y.bincount(minlength=3).tolist(),
            "loss": loss.item(),
            "accuracy": (logits.argmax(-1) == y).float().mean().item(),
            "majority_accuracy": y.bincount().max().item() / len(y),
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", help="Trusted local default-config checkpoint")
    args = parser.parse_args()
    print(json.dumps(evaluate(args.checkpoint), indent=2))


if __name__ == "__main__":
    main()
