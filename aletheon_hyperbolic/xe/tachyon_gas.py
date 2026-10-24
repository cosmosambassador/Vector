"""Classical scalar-mode model of tachyonic instability.

'Tachyon gas' is the project's conceptual label. This module solves independent
linear modes, not gas thermodynamics, quantum particles, chemistry or FTL travel.
Equation in normalized natural units: a'' + (k*k + mass_squared) * a = 0.
"""
import argparse
from dataclasses import asdict, dataclass
import json
import math
from numbers import Real


@dataclass(frozen=True)
class ModeState:
    time: float
    amplitude: float
    velocity: float
    omega_squared: float
    regime: str


def _finite(name, value):
    if isinstance(value, bool) or not isinstance(value, Real) or not math.isfinite(value):
        raise ValueError(f'{name} must be a finite real number')
    return float(value)


def mode_state(k, time, mass_squared=-1.0, amplitude0=1.0, velocity0=0.0):
    """Solve one real scalar Fourier-mode amplitude analytically.

    Negative omega_squared gives an unstable mode, zero a free linear mode, and
    positive omega_squared an oscillating mode. Generic unstable initial data
    include a growing exponential; particular data may select the decaying branch.
    No spatial propagation or nonlinear late-time stabilization is modeled.
    """
    k = _finite('k', k)
    time = _finite('time', time)
    mass_squared = _finite('mass_squared', mass_squared)
    a0 = _finite('amplitude0', amplitude0)
    v0 = _finite('velocity0', velocity0)
    if k < 0 or time < 0:
        raise ValueError('k and time must be nonnegative')
    omega2 = k*k + mass_squared
    if not math.isfinite(omega2):
        raise ValueError('Mode frequency exceeds numerical range')
    try:
        if omega2 < 0:
            rate = math.sqrt(-omega2)
            z = rate*time
            amplitude = a0*math.cosh(z) + v0*math.sinh(z)/rate
            velocity = a0*rate*math.sinh(z) + v0*math.cosh(z)
            regime = 'unstable'
        elif omega2 > 0:
            frequency = math.sqrt(omega2)
            z = frequency*time
            amplitude = a0*math.cos(z) + v0*math.sin(z)/frequency
            velocity = -a0*frequency*math.sin(z) + v0*math.cos(z)
            regime = 'oscillatory'
        else:
            amplitude = a0 + v0*time
            velocity = v0
            regime = 'linear'
    except (OverflowError, ValueError) as exc:
        raise ValueError('Evolution exceeds numerical range') from exc
    if not math.isfinite(amplitude) or not math.isfinite(velocity):
        raise ValueError('Evolution exceeds numerical range')
    return ModeState(time, amplitude, velocity, omega2, regime)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--time', type=float, default=2.0)
    parser.add_argument('--mass-squared', type=float, default=-1.0)
    args = parser.parse_args()
    try:
        modes = [dict(k=k, **asdict(mode_state(k, args.time, args.mass_squared)))
                 for k in (0., .5, 1., 2.)]
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(dict(model='classical independent scalar modes',
                          namespace='Xe', mass_squared=args.mass_squared,
                          units='normalized natural units', modes=modes), indent=2))


if __name__ == '__main__':
    main()
