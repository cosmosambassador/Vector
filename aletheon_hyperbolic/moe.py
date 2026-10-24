"""Small, classical sparse-expert experiment; no pretrained weights."""
import torch
from torch import nn


class TriVectorMoE(nn.Module):
    """One shared expert plus top-k of three routed experts per input row.

    -1, 0, +1 are expert labels only, not arithmetic weights or physical states.
    Routing weights are learned, nonnegative, and sum to one over selected experts.
    """
    expert_labels = (-1, 0, 1)

    def __init__(self, input_dim=8, expert_dim=4, num_classes=3, top_k=2):
        super().__init__()
        for name, value in [('input_dim', input_dim), ('expert_dim', expert_dim),
                            ('num_classes', num_classes), ('top_k', top_k)]:
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                raise ValueError(f'{name} must be a positive integer')
        if top_k > 3:
            raise ValueError('top_k must be at most three')
        self.input_dim = input_dim
        self.expert_dim = expert_dim
        self.top_k = top_k
        self.router = nn.Linear(input_dim, 3)
        self.shared = nn.Sequential(nn.Linear(input_dim, expert_dim), nn.Tanh())
        self.experts = nn.ModuleList([
            nn.Sequential(nn.Linear(input_dim, expert_dim), nn.Tanh())
            for _ in self.expert_labels
        ])
        self.head = nn.Linear(expert_dim, num_classes)

    def route(self, x):
        if x.ndim != 2 or x.shape[1] != self.input_dim:
            raise ValueError('Expected a batch with shape (batch, input_dim)')
        scores, indices = self.router(x).topk(self.top_k, dim=-1)
        return indices, scores.softmax(dim=-1)

    def forward(self, x):
        indices, weights = self.route(x)
        combined = self.shared(x)
        for expert_id, expert in enumerate(self.experts):
            rows, slots = torch.where(indices == expert_id)
            if rows.numel():
                contribution = expert(x[rows]) * weights[rows, slots, None]
                combined = combined.index_add(0, rows, contribution)
        return self.head(combined)
