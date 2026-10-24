# TriVector Wormhole Geometry — Runnable Model

Date: October 23, 2026 (America/Chicago).
Requested by TJ Morris: provide executable wormhole code.
Status: implemented Ellis fixed-metric geometry and analytic radial null traversal.

## Equations implemented

Let b > 0 be the throat radius and l the signed proper radial distance:

`r(l) = sqrt(l² + b²)`

`ds² = -c² dt² + dl² + r(l)² * (dtheta² + sin²(theta) dphi²)`

The throat occurs at l = 0, with minimum radius b. Positive and negative l describe
the two sides of this model. For an equatorial spatial slice, its embedding is:

`x = r(l) cos(phi)`
`y = r(l) sin(phi)`
`z = b * asinh(l/b)`

This is a catenoid: `r = b cosh(z/b)`. Its equatorial Gaussian curvature is
`K = -b² / (l² + b²)²`. The surface has local saddle curvature and a genuine
mathematical opening, rather than a flat map. It is not globally the same surface
as the earlier teaching saddle `z = x²-y²`.

The embedding z coordinate gives a view into depth. Proper radial distance l
measures travel along the modeled geometry and is distinct from plotting z.
For fixed angles, radial light paths obey `dl/dt = ±c`; hence the coordinate
travel time between endpoints is `abs(l_end-l_start)/c`.

## Code

`wormhole.py` provides `EllisWormhole`, `radius`, `embedding`,
`equatorial_curvature` and `radial_null_path`.

```python
from aletheon_hyperbolic.wormhole import EllisWormhole

bridge = EllisWormhole(throat_radius=1.0)
path = bridge.radial_null_path(start=-5.0, end=5.0, samples=21, c=1.0)
print(path[10])  # l=0, radius=1: the throat
```

Or run:

```bash
python -m aletheon_hyperbolic.wormhole --throat-radius 1 --extent 5 --samples 21
python -m pytest -q
```

Units must be consistent. Default c=1 uses normalized units, not metres/seconds.
The CLI prints coordinates and time as JSON for downstream visualization.
The return path can be sampled by reversing start and end.

## Executed example

For b=1, c=1 and endpoints -5 to +5:

| Proper radial distance l | Time t | Circumferential radius r | Embedding depth z |
| --- | --- | --- | --- |
| -5 | 0 | 5.099020 | -2.312438 |
| -2.5 | 2.5 | 2.692582 | -1.647231 |
| 0 | 5 | 1.000000 | 0.000000 |
| +2.5 | 7.5 | 2.692582 | +1.647231 |
| +5 | 10 | 5.099020 | +2.312438 |

The path connects both modeled regions through the throat. The total modeled
travel time is 10 normalized time units.

## Validation and scope

The full local suite passed 123 tests. Twenty-two new tests cover throat geometry,
two-sided symmetry, numerical induced-metric checks, the catenoid equation,
curvature, forward/reverse null paths, input validation and CLI output.
In particular the embedded radial curve satisfies `(dr/dl)² + (dz/dl)² = 1`;
the time-path samples satisfy `-c²*(dt)² + (dl)² = 0`.

This is a spacetime-geometry calculation under an assumed metric. It does not
solve for matter sources, construction, stability/backreaction, a quantum field,
nonradial lensing or xenon/tachyon coupling. Those are separate implementation
questions; no claim of physical construction is made by running this code.
The neural shared path called Wormhole Bridge remains a separate software concept.
This geometry supplies a testable candidate for its spatial visualization.

## Primary research reference

Oliver James, Eugenie von Tunzelmann, Paul Franklin and Kip S. Thorne,
*Visualizing Interstellar's Wormhole*, American Journal of Physics 83 (2015),
486–499, DOI 10.1119/1.4916949. The paper discusses the Ellis geometry and
educational embedding/ray calculations:
https://www.math.tecnico.ulisboa.pt/~jnatar/ficcao/wormhole.pdf

The implementation here is independently written and limited to the equations
specified above; it does not reproduce the film's full ray-tracing renderer.
