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

These are proposed acceptance criteria. No vortex solver, new test execution, experimental replication, antigravity production, or Xe/helium/scalar coupling is added by this documentation change. Existing modules retain their own validation scope.

## Primary sources

Sources inspected on 2026-10-24:

- Švančara et al., *Rotating curved spacetime signatures from a giant quantum vortex*, Nature 628, 66–70 (2024), published 20 March 2024. DOI: [10.1038/s41586-024-07176-8](https://doi.org/10.1038/s41586-024-07176-8).
- King's College London, [Breakthrough black hole simulation could test space, time and matter concepts](https://www.kcl.ac.uk/news/breakthrough-black-hole-simulation-could-test-space-time-and-matter-concepts), 21 March 2024.

The paper is the primary scientific reference; the university account supplies institutional context. No data files or third-party source code have been imported.

Related project records: [Xe quality control](xe/QUALITY_CONTROL.md), [wormhole geometry](WORMHOLE_MODEL.md), and [five-element framework](BE_DO_HAVE_ELEMENTS.md).
