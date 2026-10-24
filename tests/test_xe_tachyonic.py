import json
import math
import subprocess
import sys

import pytest
from aletheon_hyperbolic.xe.tachyon_gas import mode_state


@pytest.mark.parametrize('k,regime', [(0., 'unstable'), (.5, 'unstable'),
                                    (1., 'linear'), (2., 'oscillatory')])
def test_regimes_and_initial_conditions(k, regime):
    state = mode_state(k, 0., amplitude0=.7, velocity0=-.3)
    assert state.regime == regime
    assert state.amplitude == pytest.approx(.7)
    assert state.velocity == pytest.approx(-.3)


def test_known_solutions():
    assert mode_state(0., 2.).amplitude == pytest.approx(math.cosh(2.))
    assert mode_state(0., 2.).velocity == pytest.approx(math.sinh(2.))
    assert mode_state(1., 2., amplitude0=3., velocity0=4.).amplitude == 11.
    assert mode_state(0., math.pi, mass_squared=1.).amplitude == pytest.approx(-1.)
    assert mode_state(0., 2., velocity0=-1.).amplitude == pytest.approx(math.exp(-2.))


@pytest.mark.parametrize('k,mass2', [(0., -1.), (.5, -1.), (1., -1.), (2., -1.), (0., 1.)])
def test_differential_equation_and_quadratic_invariant(k, mass2):
    t, h = .7, 1e-4
    state = mode_state(k, t, mass2, .7, .2)
    before = mode_state(k, t-h, mass2, .7, .2)
    after = mode_state(k, t+h, mass2, .7, .2)
    acceleration = (after.amplitude-2*state.amplitude+before.amplitude)/h**2
    assert acceleration == pytest.approx(-state.omega_squared*state.amplitude, abs=1e-6)
    assert (after.amplitude-before.amplitude)/(2*h) == pytest.approx(state.velocity, abs=1e-6)
    initial = .5*.2**2 + .5*state.omega_squared*.7**2
    final = .5*state.velocity**2 + .5*state.omega_squared*state.amplitude**2
    assert final == pytest.approx(initial, abs=1e-10)


@pytest.mark.parametrize('name,value', [('k', -1.), ('time', -1.),
    ('k', float('nan')), ('time', float('inf')), ('mass_squared', float('nan')),
    ('amplitude0', float('inf')), ('velocity0', 'fast'), ('k', True)])
def test_invalid_inputs(name, value):
    args = dict(k=0., time=1.)
    args[name] = value
    with pytest.raises(ValueError):
        mode_state(**args)


def test_numerical_range():
    with pytest.raises(ValueError, match='range'):
        mode_state(0., 10000.)
    with pytest.raises(ValueError, match='range'):
        mode_state(1e308, 1.)


def test_cli():
    result = subprocess.run([sys.executable, '-m', 'aletheon_hyperbolic.xe.tachyon_gas'],
                            check=True, capture_output=True, text=True)
    report = json.loads(result.stdout)
    assert report['model'] == 'classical independent scalar modes'
    assert [s['regime'] for s in report['modes']] == ['unstable', 'unstable', 'linear', 'oscillatory']
