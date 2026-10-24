"""Executable Ellis wormhole geometry and radial null paths on a fixed metric."""
import argparse
from dataclasses import dataclass
import json
import math
from numbers import Real


def _finite(name, value):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f'{name} must be a finite real number')
    try:
        value = float(value)
    except OverflowError as exc:
        raise ValueError(f'{name} exceeds numerical range') from exc
    if not math.isfinite(value):
        raise ValueError(f'{name} must be a finite real number')
    return value


@dataclass(frozen=True)
class EllisWormhole:
    """Two asymptotic regions joined at a throat of radius b > 0.

    ds² = -c² dt² + dl² + (l²+b²)(dtheta² + sin²(theta) dphi²).
    l is signed proper radial distance. Embedding z is a plotting coordinate,
    distinct from l. This class specifies geometry, not material construction.
    """
    throat_radius: float = 1.0

    def __post_init__(self):
        b = _finite('throat_radius', self.throat_radius)
        if b <= 0:
            raise ValueError('throat_radius must be positive')
        object.__setattr__(self, 'throat_radius', b)

    def radius(self, proper_distance):
        l = _finite('proper_distance', proper_distance)
        radius = math.hypot(l, self.throat_radius)
        if not math.isfinite(radius):
            raise ValueError('Radius exceeds numerical range')
        return radius

    def embedding(self, proper_distance, phi=0.):
        """Equatorial spatial slice embedded as a catenoid in Euclidean 3D."""
        l = _finite('proper_distance', proper_distance)
        phi = _finite('phi', phi)
        radius = self.radius(l)
        z = self.throat_radius*math.asinh(l/self.throat_radius)
        if not math.isfinite(z):
            raise ValueError('Embedding exceeds numerical range')
        return (radius*math.cos(phi), radius*math.sin(phi), z)

    def equatorial_curvature(self, proper_distance):
        """Gaussian curvature of the equatorial embedded surface."""
        radius = self.radius(proper_distance)
        return -(self.throat_radius/radius)**2 / radius**2

    def radial_null_path(self, start=-5., end=5., samples=21, c=1., phi=0.):
        """Sample an analytic radial light path; t = abs(l-start)/c.

        Use consistent length/time units; default c=1 is normalized, not SI.
        Coordinates are for visualizing an equatorial spatial slice. The ray
        travels in the fixed spacetime metric, not in the ambient plot space.
        """
        start, end = _finite('start', start), _finite('end', end)
        c, phi = _finite('c', c), _finite('phi', phi)
        if c <= 0 or start == end:
            raise ValueError('c must be positive and endpoints must differ')
        if isinstance(samples, bool) or not isinstance(samples, int) or not 3 <= samples <= 10001:
            raise ValueError('samples must be an integer from 3 to 10001')
        distance = abs(end-start)
        if not math.isfinite(distance) or not math.isfinite(distance/c):
            raise ValueError('Path exceeds numerical range')
        points = []
        for i in range(samples):
            fraction = i/(samples-1)
            l = (1-fraction)*start + fraction*end
            x, y, z = self.embedding(l, phi)
            points.append(dict(l=l, t=fraction*distance/c,
                               radius=self.radius(l), x=x, y=y, z=z))
        return points


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--throat-radius', type=float, default=1.)
    parser.add_argument('--extent', type=float, default=5.)
    parser.add_argument('--samples', type=int, default=21)
    args = parser.parse_args()
    try:
        if not math.isfinite(args.extent) or args.extent <= 0:
            raise ValueError('extent must be finite and positive')
        model = EllisWormhole(args.throat_radius)
        path = model.radial_null_path(-args.extent, args.extent, args.samples)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(dict(model='Ellis fixed-metric wormhole',
                          units='consistent normalized units, c=1',
                          throat_radius=model.throat_radius,
                          radial_travel_time=path[-1]['t'],
                          path=path), indent=2))


if __name__ == '__main__':
    main()
