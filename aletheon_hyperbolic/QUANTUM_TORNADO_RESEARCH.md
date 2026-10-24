# Quantum tornado: vector-flow research connection

Record date: 2026-10-24.
Human authority: TJ Morris, Cosmos Ambassador.
Prepared by: Aleth / MC. Scope: source review and proposed mathematical extension.
Founder instruction: “Add your vector,” following discussion of the quantum-tornado black-hole analogue.

## Published experiment

Švančara and colleagues reported a stabilized giant vortex in superfluid helium-4 and measured interactions between surface waves and the flow, including bound states and analogue black-hole ringdown signatures. The Nature article was published on 20 March 2024. This is evidence about wave propagation in an analogue system; it does not demonstrate an astrophysical black hole or gravitational repulsion.

King's College London's account, dated 21 March 2024, identifies Nottingham's Black Hole Laboratory and university collaborators. It describes progression from earlier water-based work to the helium platform. These sources do not identify this experiment as a CERN collider test. No later upgrade is established by this note.

## Proposed vector representation

For an idealized planar vortex outside a finite core, choose polar unit vectors e_r and e_theta and write:

```text
v(r, theta) = v_r(r) e_r + v_theta(r) e_theta
v_theta(r) = Gamma / (2 pi r),    r >= r_core > 0
```

Here r and r_core are in metres, velocity is in m/s, and signed circulation Gamma is in m²/s. The tangential equation is a proposed elementary circulation model, not a fit to the published experimental data. A nondraining baseline sets v_r = 0. A draining extension needs its own radial-flow law and boundary conditions.

Changing Gamma to -Gamma reverses the tangential velocity. The speed magnitude is unchanged at fixed r and absolute circulation. This is a reversal of fluid circulation; a magnetic field would require a separate electromagnetic model. Neither operation establishes a reversal of gravity.

This representation is singular at r = 0 and must not be evaluated there. The finite-core cutoff is an explicit modeling assumption. It does not reproduce the helium apparatus, quantized vortex dynamics, measured wave dispersion, or ringdown spectrum.

## Connection to Vector

| Existing component | Useful connection | Work still needed |
| --- | --- | --- |
| Xe ideal-gas baseline | Existing SI input validation and QC approach | A superfluid-helium model needs different material physics and parameters |
| Tachyonic scalar modes | Existing analytic versus numerical solver comparisons | Vortex wave propagation requires spatial dynamics, a dispersion relation and boundary conditions |
| Ellis wormhole model | Existing example of explicit geometry and stated assumptions | A wormhole metric and a vortex's effective wave geometry are distinct models; no automatic conversion is defined |
| 30-foot circumference | Optional project geometry: 9.144 m circumference and about 1.45531 m circular radius | No evidence connects that scale to the published helium experiment; its use would require a separately justified model |
| BE → DO → HAVE | Frame the question, run a bounded computation, preserve results | Scientific claims require evidence beyond the framework |

## Smallest next computational step

A future executable extension can first verify a finite-core velocity field before adding waves:

1. Specify circulation, core radius, sample radii, units and sign convention.
2. Check that integrating tangential velocity around each circular contour recovers Gamma.
3. Check that reversing Gamma reverses the tangential vector while preserving speed.
4. Reject the singular domain and report the chosen finite-core restriction.
5. Only then specify a wave equation and a measurable target for comparison with provenance-checked experimental data.

These were the initial proposed acceptance criteria. The subsequent 30 x 30 numerical baseline below implements the circulation checks. Wave propagation and experimental replication remain pending. Existing Xe and wormhole modules retain their own validation scope.

## Primary sources

Sources inspected on 2026-10-24:

- Švančara et al., *Rotating curved spacetime signatures from a giant quantum vortex*, Nature 628, 66–70 (2024), published 20 March 2024. DOI: [10.1038/s41586-024-07176-8](https://doi.org/10.1038/s41586-024-07176-8).
- King's College London, [Breakthrough black hole simulation could test space, time and matter concepts](https://www.kcl.ac.uk/news/breakthrough-black-hole-simulation-could-test-space-time-and-matter-concepts), 21 March 2024.

The paper is the primary scientific reference; the university account supplies institutional context. No data files or third-party source code have been imported.

Related project records: [Xe quality control](xe/QUALITY_CONTROL.md), [wormhole geometry](WORMHOLE_MODEL.md), and [five-element framework](BE_DO_HAVE_ELEMENTS.md).

## Executed 30 x 30 numerical baseline

Follow-up instructions: “Take the anti gravity test on 30x30 test no matter,” then “Over hot ice magnetic fields.”

Run from the repository root:

```sh
python -m aletheon_hyperbolic.xe.vortex_check
```

The command checks 30 radii and 30 azimuths (900 sample locations) in the ideal-vortex field and its reversed-circulation counterpart. The sampling grid is an implementation choice; “30 x 30” has not been established as an enclosure dimension or physical unit. The outer circle keeps the separately authorized 30-foot circumference. Illustrative circulation is 1 m²/s, and the excluded core radius is one hundredth of the outer radius. These are numerical choices, not measured material properties.

At each location, reversing circulation reverses the velocity vector and preserves speed. Six closed-contour checks cover three radii and both circulation signs. Midpoint quadrature over 256- and 512-segment polygons must converge toward the specified circulation; the finer absolute error must be below 2e-5 m²/s. The command exits nonzero if its numerical checks fail.

The [recorded numerical report](research_results/vortex_30x30_v1.json) includes settings, aggregate errors and a source hash. It can be regenerated from the command above. The prescribed gravity baseline is -9.80665 m/s² along an upward-positive z axis, assuming equal positive inertial and gravitational mass and no additional force on a test body. This value is an input, not a predicted or measured gravitational response. Fluid velocity is not the trajectory of that body.

**Antigravity assessment: not testable with this model.** A vortex-only calculation supplies no gravitational coupling. Numerical success neither establishes antigravity nor experimentally excludes a specified new hypothesis. The script records zero physical measurements.

### Requested hot-ice and magnetic-field condition

This condition is recorded as pending, with the following material alternatives kept distinct:

| Possible meaning | Established context | Missing inputs for this project |
| --- | --- | --- |
| Sodium acetate “hot ice” | Crystallization releases heat | Composition, phase, temperature, geometry and magnetic response |
| Superionic water ice | High-pressure/high-temperature water phase with mobile hydrogen ions | Pressure, temperature, phase, conductivity and an appropriate material model |
| Founder-defined symbolic material | A design label | Physical interpretation, if one is intended |

TJ subsequently clarified “Zero” as **magnetic field** through the quantity-selection prompt. The baseline condition is therefore B = (0, 0, 0) tesla, uniformly and independently of time: a field-off control. It does not set gravity or temperature to zero. Any later nonzero-field comparison needs its own field specification. “Over” still needs a defined separation and orientation. No material response, magnetic lift, thermal coupling, or altered gravitational acceleration is computed. The JSON report records the zero-field condition and the unresolved material.

For a later physical force budget, distinguish gravitational force from electromagnetic forces, fluid forces and thermal effects. A credible experiment would require calibrated measurements and appropriate field-off, field-reversed and thermal controls. No laboratory setup or high-pressure apparatus is operated here.

Additional primary institutional references checked 2026-10-24:

- [University of Washington: Supersaturation of Sodium Acetate](https://chem.washington.edu/lecture-demos/supersaturation-sodium-acetate): exothermic crystallization.
- [Lawrence Livermore National Laboratory: First experimental evidence for superionic ice](https://www.llnl.gov/article/44081/GET): high-pressure water experiments and ionic conductivity.

Material selection remains open to founder clarification. The zero-field control establishes no relationship to CERN magnetic-field reversal.

### Temperature follow-up: option 3

TJ next selected “3,” referring to the temperature option in the preceding quantity prompt. Record **requested T = 0 K** as an idealized target, alongside the existing B = 0 control. No thermal evolution or material state at 0 K is calculated. This selection supplies no phase model for “hot ice” and no evidence of gravitational cancellation. The Xe ideal-gas function requires positive temperature; it is not called with 0 K. The present circulation-only calculation has no temperature-dependent parameters.
