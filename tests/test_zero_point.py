"""SI examples, domain rejection and an independent ground-state eigenproblem."""
import json
import math
import subprocess
import sys

import pytest
import torch

from aletheon_hyperbolic.xe.zero_point import ground_state_energy, research_report


def test_one_ghz_ground_state_energy_si():
    assert ground_state_energy(1e9) == pytest.approx(3.313035075e-25, rel=1e-14, abs=0)


@pytest.mark.parametrize('frequency', [0, -1, float('nan'), float('inf'), True, '1', 10**1000])
def test_bound_oscillator_domain(frequency):
    with pytest.raises(ValueError):
        ground_state_energy(frequency)


def test_unrepresentable_positive_energy_rejected():
    with pytest.raises(ValueError, match='numerical range'):
        ground_state_energy(1e-300)


def test_independent_schrodinger_ground_state_converges():
    # H/(hbar*omega) = -1/2 d²/dx² + x²/2, Dirichlet at x=+-8.
    # Solve a finite-difference eigenproblem, independently of the energy formula.
    errors = []
    frequency = 1e9
    dimensionless_reference = ground_state_energy(frequency)/(6.62607015e-34*frequency)
    for cells in (160, 320):
        spacing = 16/cells
        x = torch.arange(1, cells, dtype=torch.float64)*spacing-8
        diagonal = 1/spacing**2+x*x/2
        off = torch.full((cells-2,), -.5/spacing**2, dtype=torch.float64)
        hamiltonian = torch.diag(diagonal)+torch.diag(off, 1)+torch.diag(off, -1)
        lowest = torch.linalg.eigvalsh(hamiltonian)[0].item()
        errors.append(abs(lowest-dimensionless_reference))
    assert errors[1] < errors[0]/3
    assert errors[1] < 1e-4


def test_si_and_angular_frequency_conventions_agree():
    # Independent unit conversion: omega = 2*pi*f, hbar = h/(2*pi).
    omega = 2*math.pi*7e12
    hbar = 6.62607015e-34/(2*math.pi)
    assert ground_state_energy(7e12) == pytest.approx(.5*hbar*omega, rel=1e-14, abs=0)


def test_report_and_cli_preserve_scope():
    report = research_report()
    assert report['physical_measurements'] == 0
    assert report['couplings_to_xe_vortex_gravity'] == 'not defined'
    result = subprocess.run([sys.executable, '-m', 'aletheon_hyperbolic.xe.zero_point',
                             '--frequency-hz', '1000000000'],
                            capture_output=True, text=True, check=True)
    assert json.loads(result.stdout) == report
