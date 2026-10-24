# Zero-point energy baseline

Record date: 2026-10-24. Human authority: TJ Morris, Cosmos Ambassador.
Founder instruction: “Do it,” following the definition of zero-point energy.

## Implemented calculation

`zero_point.py` evaluates the ground-state energy of one stable quantum harmonic oscillator:

```text
H = p²/(2m) + m omega² x²/2
E0 = hbar omega/2 = h f/2
omega = 2 pi f
h = 6.62607015e-34 J s
```

Energy is referenced to the minimum of this quadratic potential. Frequency f is in hertz and must be finite and strictly positive. The output is in joules. This is an analytic quantum-mechanical baseline; it does not dynamically evolve a quantum state. The associated mass and spring constant are not separately determined by a supplied frequency.

At the illustrative input **f = 1 GHz**, E0 = **3.313035075e-25 J**. This frequency is a numerical example, not a measured Xe, helium, vortex or “hot ice” material parameter. The [JSON result](../research_results/zero_point_v1.json) records this example and the source hash.

```sh
python -m aletheon_hyperbolic.xe.zero_point --frequency-hz 1000000000
OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -m pytest -q
```

## Connection to the zero conditions

| Condition | Interpretation in this baseline |
| --- | --- |
| Requested T = 0 K | Idealized ground-state limit; no thermal preparation or cooling apparatus is modeled |
| Selected B = 0 tesla | Separate field-off condition from the vortex record; magnetic field is not a parameter of this oscillator |
| Nonzero E0 | Quantum ground-state energy relative to the specified potential minimum |
| 30-foot circumference / 30 x 30 grid | No oscillator frequency follows from geometry alone; no boundary-derived mode spectrum is supplied |
| Tachyonic scalar instability | The bound harmonic-oscillator formula is not applied to negative omega squared; an inverted quadratic potential has no lower-bounded oscillator ground state |

This module is separate from the existing classical gas, scalar and vortex calculations. No coupling or shared energy sum is defined. It does not model superionic ice or sodium acetate at 0 K, compute a gravitational response, or provide an energy-extraction mechanism. It does not sum an unlimited number of field modes or identify this one-mode energy with a total physical vacuum energy.

## Verification and limitations

Twelve new tests cover the SI example, the angular-frequency convention, invalid/unstable-or-free-mode frequency inputs, numerical underflow rejection, report scope and CLI output. An independent finite-difference solution of the dimensionless Schroedinger eigenproblem verifies the lowest eigenvalue and convergence under grid refinement. Its potential, boundary and discretization are stated in the test.

These checks verify the implemented oscillator baseline; no physical measurements or new experiment are claimed. Decimal intermediates preserve the SI defining value before conversion to a float; reported precision remains limited by float inputs and outputs. The numerical eigenproblem is a bounded reference calculation, not an exact representation of every quantum system.

## Primary references

Sources checked on 2026-10-24:

- [NIST: Meet the Constants](https://www.nist.gov/si-redefinition/meet-constants), exact SI definition of Planck's constant.
- [MIT OpenCourseWare, 8.04 Quantum Physics I, harmonic-oscillator lecture transcript](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/4834af67a8162364522a3d7f943f65d4_VSqpYPgxcps.pdf), ground-state energy relative to the potential minimum.

Related: [30 x 30 vortex and zero-field record](../QUANTUM_TORNADO_RESEARCH.md), [Xe quality control](QUALITY_CONTROL.md).
