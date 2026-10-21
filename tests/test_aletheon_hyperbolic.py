import torch
from aletheon_hyperbolic.geometry import exp0, log0
from aletheon_hyperbolic.model import AletheonClassifier
def test_round_trip():
    x = torch.randn(4, 8)*0.1
    assert torch.allclose(log0(exp0(x)), x, atol=1e-5)
def test_ball_and_gradients():
    model = AletheonClassifier()
    x = torch.randn(5, 8)
    out = model(x)
    assert out.shape == (5, 3)
    out.square().mean().backward()
    assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in model.parameters())
