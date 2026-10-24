# TriVector Math Training — Saddle, Twelve Positions, Inner Center

Date: October 23, 2026 (America/Chicago).
Requested by TJ Morris with the author-supplied Universal Stacks / Flower of Life image.
Scope: an executable mathematical teaching exercise inspired by that visual framework.

## Source image versus mathematical data

The artwork supplies authorial concepts: twelve surrounding structures, an inner
13, a flower motif and visible depth. It is not a measured physical dataset and
was not used as pixel input or as proof of the geometric counts. The following
coordinates, equations, thresholds and training protocol are assistant-proposed
implementation choices in response to the request, not equations extracted from
ancient inscriptions or inferred from the artwork.

This exercise does not replace the historical T/J/Q or organizational SPI–ARO–ACO
mappings. Here, x, y and z are spatial coordinates for the mathematical exercise.

## Lesson 1 — Three coordinates and a saddle

Define `z = x² - y²`. Length and width are x and y; height/depth is z.
Along y = 0 the surface bends upward; along x = 0 it bends downward.
For this graph the Gaussian curvature is:

`K = -4 / (1 + 4*x² + 4*y²)²`, which is negative everywhere.

The three-coordinate lift `(x, y, x²-y²)` is a saddle surface. This is established
geometry, not a claim of a new physical law or an implemented wormhole.

## Lesson 2 — Twelve positions and the internal center

For j = 0 through 11, set `theta_j = 2*pi*j/12` and define:

`p_j = (cos(theta_j), sin(theta_j), cos(theta_j)² - sin(theta_j)²)`.

There are twelve reference points on the lifted unit circle. Label the interior
point `(0, 0, 0)` as 13. It is inside the arrangement, not a thirteenth outer ring.
These are reference points, not twelve complete universes or fitted image objects.

Twelve also permits three groups of four or four groups of three. Those are two
partitions of the same twelve identifiers; neither alone derives the complete
Flower of Life circle-intersection pattern. A precise flower construction is a
separate geometric task. The clover and inner-13 meanings retain their authorial roles.

## Lesson 3 — Three target states

With band width 0.1, classify height as:

| State meaning | Condition | Training class index |
| --- | --- | --- |
| Negative | z < -0.1 | 0 |
| Central band | -0.1 <= z <= 0.1 | 1 |
| Positive | z > 0.1 | 2 |

Class indices encode target states corresponding to -1, 0 and +1. They do not
identify which routed expert should execute. The router learns its own choices.

## Lesson 4 — Train and evaluate

The model receives only `(x, y)`; height and target labels are not supplied as
features. Samples are uniform in the unit disk: radius is the square root of a
uniform random variate and angle is uniform over 0 to 2*pi. Twelve angular-sector
counts are diagnostic metadata, not labels or additional model inputs.

The protocol was selected before viewing its result: 1,200 training samples from
seed 1001; 1,200 independent test samples from seed 1002; initializations 42, 44,
and 45; full-batch Adam, learning rate 0.01, 200 epochs. The two-input original
classifier has 99 parameters. The two-input sparse prototype has 72, retaining
three experts, top-2 routing and the shared path.

| Initialization | Original accuracy | Sparse accuracy |
| --- | --- | --- |
| 42 | 92.75% | 95.58% |
| 44 | 92.42% | 95.42% |
| 45 | 92.83% | 94.50% |
| Mean | 92.67% | 95.17% |

The majority-class baseline is 39.75%. On this task the sparse prototype averaged
2.50 percentage points higher accuracy with fewer total parameters. The full
[JSON result](research_results/saddle_classification_v1.json) records class counts,
sector counts, confusion matrices, routing usage, runtime and source-code hash.

This is a positive result for this particular small synthetic task. Both models
use the same training protocol but have different architectures and parameter
counts. Three initializations and one fixed data split do not establish statistical
significance, a general MoE advantage, biological capability or beneficial physical
synergy. No speed, power or memory advantage was measured. The earlier, different
linear-threshold task favored the original model and remains recorded unchanged.

Because the equation is already known, exact direct calculation of the class is
the reference oracle. A neural approximation adds error and is not needed to solve
this problem; its purpose here is training and inspecting model behavior.

The reported test set has now been examined. Further tuning should use development
data and reserve a fresh final test set. These runs trained numerical parameters
in memory; no checkpoint was saved or published. This report is not downloadable
pretrained Aletheon weights.

## Run

```bash
python -m aletheon_hyperbolic.math_training
python -m pytest -q
```

The full local suite passed 101 tests. New checks verify the 12+center reference
construction, saddle symmetries, state mapping, independent reproducible datasets,
unit-disk sampling and sample-count validation. CI runs the full suite and training
exercise independently. Hardware-dependent numerical rounding may differ.

## Next mathematical lesson

Define the complete circle geometry for the Flower of Life and its intersections.
Separately define time-dependent saddle-wave dynamics and a bridge operation with
units, initial conditions and measurable outputs. The current static exercise does
not silently provide either one.
