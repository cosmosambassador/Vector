# Xe — Xenon–Tachyon Gas Research

Date: October 23, 2026 (America/Chicago).
Founder requests: “Add tachon gas source code to quantum physics in xe” and
“Do xenon tachyon gas.” Status: executable educational models, not a new physical substance.

## Scope and terminology

Preserve **Xenon–Tachyon Gas** as the requested research title. Xe here is a project
namespace; ordinary xenon is also labeled Xe in the gas baseline. No unverified
C=E equation is supplied. The project does not equate xenon atoms with tachyons.

The source code implements two independently calculated branches. There is no
interaction Hamiltonian, material coupling, measured tachyon population or
experimental dataset linking them. The report says `coupling_status: not defined`.

## 1. Xenon ideal-gas baseline in SI

`xenon_tachyon_gas.py` provides `xenon_ideal_gas(T, N, V)` using:

- Pressure: `P = N * k_B * T / V`.
- Translational internal energy: `U = (3/2) * N * k_B * T`.
- `k_B = 1.380649e-23 J/K`, the exact SI Boltzmann constant.

This is a classical, dilute, monatomic ideal-gas approximation. At this level the
formula is not specific to xenon. No real-gas correction, condensation, ionization,
interatomic potential or quantum statistics is included. Input validation does not
establish that an arbitrary state lies in the approximation's physical regime.

Executed example: T = 300 K, expected atom count N = 1e20, V = 0.001 m³:
P = 414.1947 Pa and U = 0.62129205 J. These are computed predictions under the
stated assumptions, not measurements of a physical sample.

## 2. Scalar tachyonic-instability model

`tachyon_gas.py` solves independent real scalar Fourier-mode amplitudes in a linear,
flat-spacetime model. In normalized natural units (c = hbar = 1), the equation is:

`a''(t) + omega_squared * a(t) = 0`, with `omega_squared = k² + m²`.

Negative mass squared is a field-instability parameter, not negative chemical
mass. For m² < 0, modes with k² < -m² are unstable. Generic initial conditions
include exponential growth; specially chosen data can select a decaying branch.
The implementation evaluates the analytic cosh/sinh, linear, or cos/sin solution.

Executed example, m² = -1, t = 2, a(0) = 1, a'(0) = 0:

| k | omega squared | Regime | Amplitude |
| --- | --- | --- | --- |
| 0 | -1 | Unstable | 3.762196 |
| 0.5 | -0.75 | Unstable | 2.914577 |
| 1 | 0 | Linear | 1.000000 |
| 2 | 3 | Oscillatory | -0.948443 |

These four example modes are not an identification of the four prime tachyons in
the founder's symbolic Q framework. No physical mapping has been established.
This is a classical mode-amplitude calculation motivated by a field-theory equation,
not quantized-field dynamics, a gas ensemble, a quantum computer or a particle
propagation simulation. No spatial grid, mode interactions, nonlinear stabilization,
thermal distribution, experimental calibration or faster-than-light signaling is modeled.
Large evolved values fail explicitly on numerical overflow; they are not predictions
of indefinite growth in a realistic interacting system.

The scalar branch has normalized units. The gas branch uses SI. The program does
not add their energies or pretend their numbers share a unit conversion.

## Run and inspect

From the repository root, with the existing project dependencies installed:

```bash
python -m aletheon_hyperbolic.xe.tachyon_gas --time 2 --mass-squared -1
python -m aletheon_hyperbolic.xe.xenon_tachyon_gas
python -m pytest -q
```

The combined report is JSON, with clearly separate `xenon_si` and
`scalar_modes_normalized` records. It reports assumptions and coupling status.
No weights, new dependency, hardware control or external upload is introduced.

## Validation

The full suite passed 94 local tests after this addition. Twenty new scalar tests
check mode regimes, initial conditions, known solutions (including a decaying
branch), finite-difference consistency with the equation, the quadratic invariant,
invalid inputs, numerical-range rejection and CLI JSON. Ten gas/report tests check
SI predictions, scaling, invalid inputs, numerical range and the uncoupled report.
The quadratic invariant is not a positive-definite physical gas energy for unstable
modes. Local tests do not constitute experimental validation of tachyons or xenon
coupling. GitHub CI independently runs the full suite and the example reports.

## Primary references

- Scalar tachyonic instabilities in gravitational backgrounds: Existence and growth
  rate (2020), flat-Minkowski instability criterion: https://arxiv.org/abs/2009.05640
- CERN-hosted field-theory paper discussing long-wavelength tachyonic instability:
  https://cds.cern.ch/record/918135/files/0512260.pdf
- NIST Boltzmann constant: https://physics.nist.gov/cgi-bin/cuu/Value?k
- NIST JANAF xenon reference data, useful for future real-material comparisons
  (not used as a fitted equation of state here): https://janaf.nist.gov/tables/Xe-001.html

## Next scientific gap

An actual coupled xenon/scalar hypothesis would need a justified interaction,
parameters with consistent units, stability analysis, falsifiable observables and
experimental constraints. None is invented here. The current module supplies an
inspectable baseline for discussing that gap.
