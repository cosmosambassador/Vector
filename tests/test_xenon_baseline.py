import math
import pytest
from aletheon_hyperbolic.xe.xenon_tachyon_gas import (
    BOLTZMANN_J_PER_K, research_report, xenon_ideal_gas,
)


def test_si_baseline_and_scaling():
    state = xenon_ideal_gas(300., 1e20, .001)
    assert state['pressure_pa'] == pytest.approx(414.1947)
    assert state['internal_energy_j'] == pytest.approx(.62129205)
    assert state['pressure_pa']*.001 == pytest.approx(1e20*BOLTZMANN_J_PER_K*300.)
    assert xenon_ideal_gas(300., 1e20, .002)['pressure_pa'] == pytest.approx(state['pressure_pa']/2)
    assert xenon_ideal_gas(600., 1e20, .001)['pressure_pa'] == pytest.approx(state['pressure_pa']*2)


@pytest.mark.parametrize('name,value', [('temperature_k', 0), ('temperature_k', -1),
    ('atom_count', 0), ('volume_m3', 0), ('volume_m3', -1),
    ('temperature_k', float('nan')), ('atom_count', float('inf'))])
def test_gas_input_rejection(name, value):
    args = dict(temperature_k=300., atom_count=1e20, volume_m3=.001)
    args[name] = value
    with pytest.raises(ValueError):
        xenon_ideal_gas(**args)


def test_uncoupled_report():
    report = research_report()
    assert report['coupling_status'].startswith('not defined')
    assert len(report['scalar_modes_normalized']) == 4
    assert report['xenon_si']['species'] == 'Xe'
    assert all(math.isfinite(x['amplitude']) for x in report['scalar_modes_normalized'])


def test_gas_numerical_range():
    with pytest.raises(ValueError, match='range'):
        xenon_ideal_gas(1e308, 1e308, .001)
