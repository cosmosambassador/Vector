import pytest
import torch
from aletheon_hyperbolic.moe import TriVectorMoE


def test_sparse_dispatch_and_weighted_combination():
    torch.manual_seed(42)
    model = TriVectorMoE()
    with torch.no_grad():
        model.router.weight.zero_()
        model.router.bias.copy_(torch.tensor([3., 2., -10.]))
    x = torch.randn(7, 8)
    indices, weights = model.route(x)
    assert (indices == torch.tensor([0, 1])).all()
    torch.testing.assert_close(weights.sum(-1), torch.ones(7))
    calls = [0, 0, 0]
    def hook(i):
        def record(module, args, result):
            calls[i] += len(args[0])
        return record
    handles = [expert.register_forward_hook(hook(i)) for i, expert in enumerate(model.experts)]
    actual = model(x)
    for handle in handles:
        handle.remove()
    assert calls == [7, 7, 0]
    expected = model.head(model.shared(x) + weights[:, :1]*model.experts[0](x)
                          + weights[:, 1:]*model.experts[1](x))
    torch.testing.assert_close(actual, expected)
    actual.square().mean().backward()
    assert torch.isfinite(model.router.bias.grad).all()
    assert model.router.bias.grad.abs().sum() > 0
    assert model.experts[2][0].weight.grad is None
    for i in (0, 1):
        assert torch.isfinite(model.experts[i][0].weight.grad).all()


@pytest.mark.parametrize('top_k', [1, 2, 3])
def test_input_dependent_routing_and_shapes(top_k):
    model = TriVectorMoE(top_k=top_k)
    with torch.no_grad():
        model.router.weight.zero_()
        model.router.bias.zero_()
        model.router.weight[:, 0] = torch.tensor([1., 0., -1.])
    x = torch.zeros(2, 8)
    x[:, 0] = torch.tensor([1., -1.])
    indices, weights = model.route(x)
    assert indices[0, 0] == 0 and indices[1, 0] == 2
    assert indices.shape == weights.shape == (2, top_k)
    assert model(x).shape == (2, 3)
    assert model(torch.empty(0, 8)).shape == (0, 3)


@pytest.mark.parametrize('kwargs', [{'top_k': 0}, {'top_k': 4}, {'top_k': True},
                                   {'expert_dim': -1}, {'input_dim': 0}])
def test_invalid_config(kwargs):
    with pytest.raises(ValueError):
        TriVectorMoE(**kwargs)


def test_bad_input():
    with pytest.raises(ValueError, match='batch'):
        TriVectorMoE()(torch.zeros(8))
