# Xe quality control

This is independent software work in cosmosambassador/Vector. It has no CERN commissioning, laboratory access, endorsement, or approval. The Xe ideal-gas calculation and normalized scalar modes remain uncoupled.

## Reproduce

```sh
OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -m pytest -q
python -m aletheon_hyperbolic.xe.quality_control
```

The QC command prints JSON and returns a nonzero exit status on failure. CI runs it separately from pytest. A reproducible local snapshot is in [xe_quality_control_v1.json](../research_results/xe_quality_control_v1.json); its Python version and SHA-256 hashes identify the three source files used. It records no trained weights. Regenerate it when those files change.

## Acceptance evidence

| Check | Acceptance rule | Evidence and scope |
|---|---|---|
| Independent scalar ODE solver | Absolute amplitude/velocity error <= 1e-7 at normalized time 1; refinement from 100 to 200 RK4 steps must not worsen error beyond 1e-13 roundoff allowance | 16 fixed cases: k = 0, 0.5, 1, 2; mass squared = -1, +1; two initial states. Includes unstable, linear and oscillatory regimes. |
| Xe heat-capacity reference | Constant-pressure enthalpy difference for one mole, 300 to 301 K, agrees with 20.786 J/(mol K) within 0.0005 | NIST-JANAF Xe standard-state ideal-gas consistency. Tolerance reflects the reference's three decimal places; it is not experimental uncertainty. |
| Decaying scalar branch | exp(-t) and its negative derivative retained at t = 40 and 710 | Regression for cancellation in cosh(t)-sinh(t), with unused growing exponential excluded. |
| Gas numerical range | Representable outputs retained with extreme reciprocal inputs; zero/nonfinite final pressure or energy rejected | Regression for intermediate subnormal rounding/underflow. Extreme inputs are numerical stress cases, not physical gas conditions. |
| Input validation | Oversized integers produce a controlled ValueError | Prevents an uncaught float-conversion overflow. |

The completed local suite contains **133 passing tests**, including 40 Xe tests. This local run does not establish that the new commit passed remote CI. The RK4 cases are disclosed software cross-checks, not a blind test, held-out scientific dataset, or independent human replication.

The gas calculation uses 50-digit Decimal intermediates before conversion to float. This extends the intermediate exponent range; it does not give float outputs 50 digits of accuracy. Scalar results remain subject to floating-point conditioning and precision in the initial data. No claim of exhaustive numerical validation is made.

## Reference provenance

Public sources checked on 2026-10-24:

- [BIPM SI defining constants](https://www.bipm.org/en/measurement-units/si-defining-constants): exact k = 1.380649e-23 J/K and N_A = 6.02214076e23 mol^-1.
- [NIST-JANAF Xe table](https://janaf.nist.gov/tables/Xe-001.html): Cp at 300 K = 20.786 J/(mol K), standard-state pressure 0.1 MPa, enthalpy reference temperature 298.15 K. Only the Cp value is transcribed into the QC reference. The ideal-gas enthalpy derivative is pressure-independent; matching it does not validate a real-Xe equation of state.
- [CERN Q2 cryo-assembly validation report, 8 September 2026](https://hilumilhc.web.cern.ch/all-q2-cryo-assemblies-required-for-the-tunnel-validated/): public example of stated operating targets and repeated tests under different conditions. This motivates traceable requirements and reproducible checks here; magnet qualification limits do not apply to Xe software.

These are source links and explicit transcriptions, not a complete archival provenance audit. No internal CERN records or Xe experimental dataset were retrieved.

## Remaining gates

1. **Execution:** remote CI must pass on the proposed commit; reviewers must be able to reproduce the report.
2. **Numerical review:** extend conditioning and long-time tests if a broader scalar operating domain is proposed; choose physically justified Xe temperature/density ranges and compare against a real-gas equation of state.
3. **Empirical evaluation:** obtain provenance-checked Xe measurements, uncertainties, calibration information, and a frozen held-out or blinded evaluation protocol before claiming predictive physical performance.
4. **Theory:** define an interaction, units, observables and falsifiable predictions before evaluating a proposed Xe/scalar coupling. Current software provides no evidence for physical tachyons.
5. **Human approval:** scientific review, source/licensing and security review, and maintainer approval remain separate from passing tests. Merge remains a maintainer decision.
