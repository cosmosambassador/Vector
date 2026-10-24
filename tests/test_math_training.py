import pytest
import torch
from aletheon_hyperbolic.math_training import make_dataset, reference_geometry, saddle_labels


def test_reference_geometry():
    points = reference_geometry()
    assert [p['label'] for p in points] == list(range(1, 14))
    assert points[-1] == dict(label=13, x=0., y=0., z=0.)
    for p in points[:-1]:
        assert p['x']**2+p['y']**2 == pytest.approx(1.)
        assert p['z'] == pytest.approx(p['x']**2-p['y']**2)
    assert points[0]['z'] == pytest.approx(1.)
    assert points[3]['z'] == pytest.approx(-1.)


def test_labels_symmetry_and_boundaries():
    xy = torch.tensor([[1., 0.], [0., 0.], [0., 1.], [.5, .5]])
    assert saddle_labels(xy).tolist() == [2, 1, 0, 1]
    assert torch.equal(saddle_labels(xy.flip(-1)), 2-saddle_labels(xy))
    assert torch.equal(saddle_labels(-xy), saddle_labels(xy))


def test_separate_reproducible_datasets():
    x, y, sectors = make_dataset(1200, 1001)
    x2, y2, sectors2 = make_dataset(1200, 1001)
    test, _, _ = make_dataset(1200, 1002)
    assert torch.equal(x, x2) and torch.equal(y, y2) and torch.equal(sectors, sectors2)
    assert not torch.equal(x, test)
    assert (x.square().sum(-1) <= 1+1e-6).all()
    assert y.unique().tolist() == [0, 1, 2]
    assert sectors.unique().tolist() == list(range(12))


@pytest.mark.parametrize('samples', [0, -1, True, 1.5])
def test_sample_count_validation(samples):
    with pytest.raises(ValueError):
        make_dataset(samples, 42)
