"""Xenon–Tachyon Gas: two uncoupled educational calculations.

Ordinary Xe uses a dilute monatomic ideal-gas approximation in SI. Scalar modes
use normalized natural units. No xenon/tachyon interaction or unit conversion
between those branches is defined or implied.
"""
import json
import math
from dataclasses import asdict
from .tachyon_gas import _finite, mode_state

BOLTZMANN_J_PER_K = 1.380649e-23  # Exact SI defining constant, NIST.


def xenon_ideal_gas(temperature_k, atom_count, volume_m3):
    """Return an idealized gas baseline, not a real-xenon equation of state.

    Atom count is a macroscopic expected count and may be a positive real value.
    The caller must justify the dilute, classical, monatomic regime. Condensation,
    interactions, ionization, quantum statistics and xenon-specific corrections
    are omitted. Passing validation does not establish physical validity.
    """
    temperature = _finite('temperature_k', temperature_k)
    count = _finite('atom_count', atom_count)
    volume = _finite('volume_m3', volume_m3)
    if min(temperature, count, volume) <= 0:
        raise ValueError('Temperature, atom count and volume must be positive')
    energy = count*BOLTZMANN_J_PER_K*temperature
    pressure = energy/volume
    internal_energy = 1.5*energy
    if not all(math.isfinite(x) for x in (energy, pressure, internal_energy)):
        raise ValueError('Gas calculation exceeds numerical range')
    return dict(species='Xe', approximation='dilute monatomic ideal gas',
                temperature_k=temperature, atom_count=count, volume_m3=volume,
                pressure_pa=pressure, internal_energy_j=internal_energy)


def research_report():
    return dict(
        project_label='Xenon–Tachyon Gas',
        coupling_status='not defined; independent calculations',
        xenon_si=xenon_ideal_gas(300., 1e20, 1e-3),
        scalar_modes_normalized=[dict(k=k, **asdict(mode_state(k, 2.)))
                                 for k in (0., .5, 1., 2.)],
    )


def main():
    print(json.dumps(research_report(), indent=2))


if __name__ == '__main__':
    main()
