"""Regression checks for numerical failures and reproducible QC."""
import json
import math
import subprocess
import sys

import pytest

from aletheon_hyperbolic.xe.quality_control import run_quality_control
from aletheon_hyperbolic.xe.tachyon_gas import mode_state
from aletheon_hyperbolic.xe.xenon_tachyon_gas import xenon_ideal_gas


def test_decaying_mode_survives_cancellation_and_unused_overflow():
    for time in (40., 710.):
        state = mode_state(0., time, velocity0=-1.)
        assert state.amplitude == pytest.approx(math.exp(-time), rel=1e-12, abs=0)
        assert state.velocity == -state.amplitude


@pytest.mark.parametrize('mass_squared', [-1e-30, 0., 1e-30])
def test_continuous_zero_frequency_limit(mass_squared):
    state = mode_state(0., 2., mass_squared, .3, -.7)
    assert state.amplitude == pytest.approx(-1.1)
    assert state.velocity == pytest.approx(-.7)


@pytest.mark.parametrize('temperature,count', [(1e300, 1e-300), (1e-300, 1e300)])
def test_gas_intermediate_underflow_preserves_representable_result(temperature, count):
    gas = xenon_ideal_gas(temperature, count, 1.)
    assert gas['pressure_pa'] == pytest.approx(1.380649e-23, rel=1e-14, abs=0)
    assert gas['internal_energy_j'] == pytest.approx(2.0709735e-23, rel=1e-14, abs=0)


def test_unrepresentable_gas_output_rejected():
    with pytest.raises(ValueError, match='numerical range'):
        xenon_ideal_gas(1e-300, 1e-300, 1.)


def test_oversized_integer_is_controlled_validation_error():
    with pytest.raises(ValueError, match='finite real'):
        mode_state(10**1000, 1.)


def test_independent_solver_and_reference_report():
    report = run_quality_control()
    assert report['passed']
    assert len(report['scalar_cases']) == 16
    assert {c['mass_squared'] for c in report['scalar_cases']} == {-1., 1.}
    assert all(c['fine_error'] <= report['scalar_absolute_tolerance']
               for c in report['scalar_cases'])
    assert report['pending']
    assert len(report['source_sha256']) == 3


def test_qc_cli_emits_machine_readable_pass():
    result = subprocess.run([sys.executable, '-m', 'aletheon_hyperbolic.xe.quality_control'],
                            capture_output=True, text=True, check=True)
    assert json.loads(result.stdout)['passed']
