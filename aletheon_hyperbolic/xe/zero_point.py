"""Ground-state energy of one stable quantum harmonic oscillator in SI.

Energy is relative to the minimum of its specified quadratic potential.
No field-vacuum sum, extraction mechanism, material model or gravity coupling.
"""
import argparse
from decimal import Decimal, localcontext
import hashlib
import json
from pathlib import Path

from .tachyon_gas import _finite

PLANCK_J_S = 6.62607015e-34  # Exact SI defining value; float representation rounded.


def ground_state_energy(frequency_hz):
    """Return E0 = h*f/2 in joules for a finite, strictly positive frequency.

    A zero-frequency free mode or an unstable inverted potential is outside this
    bound-oscillator model. A positive result must be representable as a float.
    """
    frequency = _finite('frequency_hz', frequency_hz)
    if frequency <= 0:
        raise ValueError('frequency_hz must be strictly positive for a bound oscillator')
    with localcontext() as context:
        context.prec = 50
        energy = float(Decimal('6.62607015e-34')*Decimal(frequency)/2)
    if energy <= 0:
        raise ValueError('Ground-state energy is below numerical range')
    return energy


def research_report(frequency_hz=1e9):
    energy = ground_state_energy(frequency_hz)
    return dict(model='one stable quantum harmonic oscillator',
                frequency_hz=float(frequency_hz), ground_state_energy_j=energy,
                energy_reference='minimum of the specified quadratic potential',
                state='ground state; idealized zero-temperature limit',
                magnetic_field='not a parameter of this uncoupled oscillator',
                couplings_to_xe_vortex_gravity='not defined',
                energy_extraction='not modeled', physical_measurements=0,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frequency-hz', type=float, default=1e9)
    args = parser.parse_args()
    try:
        report = research_report(args.frequency_hz)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
