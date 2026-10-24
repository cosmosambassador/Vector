"""Reproducible software cross-checks for the independent Xe research model."""
import hashlib
import json
from pathlib import Path
import platform

from .tachyon_gas import mode_state
from .xenon_tachyon_gas import xenon_ideal_gas


def _rk4(omega2, a, v, time, steps):
    """Integrate a'=v, v'=-omega2*a without the analytic solution."""
    h = time/steps
    for _ in range(steps):
        a1, v1 = v, -omega2*a
        a2, v2 = v+h*v1/2, -omega2*(a+h*a1/2)
        a3, v3 = v+h*v2/2, -omega2*(a+h*a2/2)
        a4, v4 = v+h*v3, -omega2*(a+h*a3)
        a += h*(a1+2*a2+2*a3+a4)/6
        v += h*(v1+2*v2+2*v3+v4)/6
    return a, v


def run_quality_control():
    cases = []
    tolerance = 1e-7
    for mass_squared in (-1., 1.):
        for k in (0., .5, 1., 2.):
            for a0, v0 in ((1., 0.), (.3, -.7)):
                analytic = mode_state(k, 1., mass_squared, a0, v0)
                coarse = _rk4(k*k+mass_squared, a0, v0, 1., 100)
                fine = _rk4(k*k+mass_squared, a0, v0, 1., 200)
                errors = [max(abs(a-analytic.amplitude), abs(v-analytic.velocity))
                          for a, v in (coarse, fine)]
                cases.append(dict(k=k, mass_squared=mass_squared,
                                  amplitude0=a0, velocity0=v0,
                                  coarse_error=errors[0], fine_error=errors[1],
                                  passed=errors[1] <= tolerance and
                                  errors[1] <= errors[0]+1e-13))
    # One mole, constant pressure, 300 -> 301 K. H = U + PV in SI.
    # N_A is an exact SI defining constant. JANAF's Cp is rounded to .001.
    states = [xenon_ideal_gas(t, 6.02214076e23, .025*t/300)
              for t in (300., 301.)]
    enthalpies = [s['internal_energy_j']+s['pressure_pa']*s['volume_m3']
                  for s in states]
    cp = enthalpies[1]-enthalpies[0]
    reference = dict(source='https://janaf.nist.gov/tables/Xe-001.html',
                     temperature_k=300., cp_j_per_mol_k=20.786,
                     computed_cp_j_per_mol_k=cp, absolute_tolerance=.0005,
                     passed=abs(cp-20.786) <= .0005)
    root = Path(__file__).parent
    hashes = {name: hashlib.sha256((root/name).read_bytes()).hexdigest()
              for name in ('tachyon_gas.py', 'xenon_tachyon_gas.py',
                           'quality_control.py')}
    return dict(schema_version=1, python=platform.python_version(),
                scope='software verification and ideal-gas reference consistency',
                affiliation='independent project; no CERN approval or commissioning',
                scalar_absolute_tolerance=tolerance, time=1., steps=[100, 200],
                scalar_cases=cases, xenon_reference=reference,
                source_sha256=hashes,
                passed=all(c['passed'] for c in cases) and reference['passed'],
                pending=['real Xe measurements and equation-of-state validation',
                         'blind or held-out experimental evaluation',
                         'defined Xe/scalar coupling and physical evidence',
                         'independent scientific and maintainer review'])


def main():
    result = run_quality_control()
    print(json.dumps(result, indent=2, allow_nan=False))
    raise SystemExit(0 if result['passed'] else 1)


if __name__ == '__main__':
    main()
