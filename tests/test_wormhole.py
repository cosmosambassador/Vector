import json
import math
import subprocess
import sys
import pytest
from aletheon_hyperbolic.wormhole import EllisWormhole


def test_throat_and_two_sides():
    model = EllisWormhole(2.)
    assert model.radius(0.) == 2.
    assert model.embedding(0.) == (2., 0., 0.)
    for l in (.1, 1., 10.):
        assert model.radius(l) > 2.
        assert model.radius(l) == model.radius(-l)
        a, b = model.embedding(l), model.embedding(-l)
        assert a[:2] == b[:2] and a[2] == -b[2]


@pytest.mark.parametrize('l', [-5., -1., 0., 1., 5.])
def test_induced_spatial_metric(l):
    model = EllisWormhole(1.7)
    h = 1e-5
    before, after = model.embedding(l-h), model.embedding(l+h)
    speed2 = sum(((a-b)/(2*h))**2 for a,b in zip(after,before))
    assert speed2 == pytest.approx(1., abs=1e-8)
    x,y,z = model.embedding(l)
    assert math.hypot(x,y) == pytest.approx(1.7*math.cosh(z/1.7))


def test_curvature():
    model = EllisWormhole(2.)
    assert model.equatorial_curvature(0.) == pytest.approx(-.25)
    assert model.equatorial_curvature(3.) == pytest.approx(-4/(9+4)**2)


@pytest.mark.parametrize('start,end', [(-5., 5.), (5., -5.)])
def test_null_crossing(start,end):
    model = EllisWormhole()
    path = model.radial_null_path(start,end,21,c=2.)
    assert path[0]['l'] == start and path[-1]['l'] == end
    assert path[0]['t'] == 0 and path[-1]['t'] == 5.
    assert path[10]['l'] == 0. and path[10]['radius'] == 1.
    for a,b in zip(path,path[1:]):
        dt, dl = b['t']-a['t'], b['l']-a['l']
        assert dt > 0
        assert -4*dt**2+dl**2 == pytest.approx(0.,abs=1e-12)


@pytest.mark.parametrize('b', [0., -1., float('nan'), float('inf'), True])
def test_bad_throat(b):
    with pytest.raises(ValueError):
        EllisWormhole(b)


@pytest.mark.parametrize('kwargs', [{'c':0}, {'start':1.,'end':1.},
    {'samples':2}, {'samples':10002}, {'samples':True}, {'start':float('inf')},
    {'phi':float('nan')}])
def test_bad_path(kwargs):
    with pytest.raises(ValueError):
        EllisWormhole().radial_null_path(**kwargs)


def test_cli():
    result = subprocess.run([sys.executable,'-m','aletheon_hyperbolic.wormhole',
                             '--samples','5'],check=True,capture_output=True,text=True)
    data = json.loads(result.stdout)
    assert data['radial_travel_time'] == 10.
    assert len(data['path']) == 5
    assert data['path'][2]['l'] == 0.
