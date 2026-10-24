import torch
from torch import nn
from .geometry import project, exp0, log0, _validate_curvature
class HyperbolicLinearTanh(nn.Module):
    def __init__(self, in_features, out_features, c=1.0):
        super().__init__()
        _validate_curvature(c)
        self.c = c
        self.linear = nn.Linear(in_features, out_features)
    def forward(self, x):
        v = log0(project(x, self.c), self.c)
        return exp0(torch.tanh(self.linear(v)), self.c)
class AletheonClassifier(nn.Module):
    def __init__(self, input_dim=8, hidden_dim=16, num_classes=3, c=1.0):
        super().__init__()
        _validate_curvature(c)
        self.c = c
        self.layer = HyperbolicLinearTanh(input_dim, hidden_dim, c)
        self.head = nn.Linear(hidden_dim, num_classes)
    def forward(self, x):
        x = exp0(x, self.c)
        return self.head(log0(self.layer(x), self.c))
