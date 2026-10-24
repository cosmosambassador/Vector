import torch
from .model import AletheonClassifier
def load_checkpoint(path, map_location="cpu"):
    # Load only trusted checkpoints. weights_only avoids arbitrary pickle objects.
    checkpoint = torch.load(path, map_location=map_location, weights_only=True)
    model = AletheonClassifier(**checkpoint["config"])
    model.load_state_dict(checkpoint["state_dict"])
    return model.eval()
