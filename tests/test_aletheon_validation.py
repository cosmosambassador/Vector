"""Numerical and artifact checks for the experimental CPU workspace."""
import subprocess
import sys

import pytest
import torch

from aletheon_hyperbolic.evaluate import evaluate
from aletheon_hyperbolic.geometry import exp0, log0, project
from aletheon_hyperbolic.load import load_checkpoint
from aletheon_hyperbolic.model import AletheonClassifier


@pytest.mark.parametrize('dtype', [torch.float32, torch.float64])
@pytest.mark.parametrize('c', [0.1, 1.0, 10.0])
@pytest.mark.parametrize('scale', [0., 1e-12, .1, 10., 100.])
def test_geometry_domain(dtype, c, scale):
    generator = torch.Generator().manual_seed(42)
    x = (torch.randn(8, 8, dtype=dtype, generator=generator) * scale).requires_grad_()
    ball = exp0(x, c)
    recovered = log0(ball, c)
    recovered.sum().backward()
    assert torch.isfinite(recovered).all()
    assert torch.isfinite(x.grad).all()
    assert (ball.norm(dim=-1) < c ** -.5).all()
    if scale <= .1:
        torch.testing.assert_close(recovered, x, atol=1e-6, rtol=1e-5)


@pytest.mark.parametrize('c', [0., -1., float('nan'), float('inf')])
@pytest.mark.parametrize('operation', [project, exp0, log0])
def test_invalid_curvature(operation, c):
    with pytest.raises(ValueError, match='finite positive'):
        operation(torch.zeros(1, 8), c)


@pytest.mark.parametrize('eps', [0., 1., -1., float('nan')])
def test_invalid_projection_margin(eps):
    with pytest.raises(ValueError, match='eps'):
        project(torch.zeros(1, 8), eps=eps)


def test_near_boundary_and_gradcheck():
    x = torch.tensor([[1. - 1e-8, 0.]], dtype=torch.float64, requires_grad=True)
    result = log0(x)
    result.sum().backward()
    assert torch.isfinite(result).all() and torch.isfinite(x.grad).all()
    interior = torch.tensor([[.1, -.2]], dtype=torch.float64, requires_grad=True)
    assert torch.autograd.gradcheck(lambda v: log0(exp0(v)), (interior,))


def test_checkpoint_round_trip(tmp_path):
    torch.manual_seed(42)
    model = AletheonClassifier().eval()
    path = tmp_path / 'checkpoint.pt'
    torch.save({'config': {}, 'state_dict': model.state_dict()}, path)
    loaded = load_checkpoint(path)
    x = torch.randn(5, 8)
    assert not loaded.training
    torch.testing.assert_close(model(x), loaded(x))


@pytest.mark.parametrize('kind', ['missing', 'shape', 'curvature'])
def test_invalid_checkpoint(tmp_path, kind):
    checkpoint = {'config': {}, 'state_dict': AletheonClassifier().state_dict()}
    if kind == 'missing':
        del checkpoint['config']
        error = KeyError
    elif kind == 'shape':
        checkpoint['state_dict']['head.weight'] = torch.zeros(1, 1)
        error = RuntimeError
    else:
        checkpoint['config']['c'] = 0.
        error = ValueError
    path = tmp_path / 'bad.pt'
    torch.save(checkpoint, path)
    with pytest.raises(error):
        load_checkpoint(path)


def test_training_and_heldout(tmp_path):
    path = tmp_path / 'trained.pt'
    subprocess.run([sys.executable, '-m', 'aletheon_hyperbolic.train',
                    '--epochs', '30', '--checkpoint', str(path)], check=True,
                   capture_output=True, text=True)
    metrics = evaluate(path)
    assert sum(metrics['class_counts']) == metrics['samples'] == 1000
    assert metrics['accuracy'] > metrics['majority_accuracy']
    assert metrics['loss'] >= 0
