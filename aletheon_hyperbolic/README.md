# Aletheon Hyperbolic Research v0.1
Experimental PyTorch Poincare-ball tangent-space classifier. **Not a pretrained Aletheon model.**

## Setup
Run these commands from the repository root using Python 3.12 (CPU):
```bash
python -m pip install torch==2.14.1 --index-url https://download.pytorch.org/whl/cpu
python -m pip install pytest==9.1.1
python -m pytest -q
python -m aletheon_hyperbolic.train --epochs 30
python -m aletheon_hyperbolic.evaluate aletheon_checkpoint.pt
```

## Load a local checkpoint
```python
from aletheon_hyperbolic.load import load_checkpoint
model = load_checkpoint("aletheon_checkpoint.pt")
```

## Hugging Face compatibility
The PyTorch `state_dict` can be saved as a model artifact in a Hugging Face repository after human approval. No Hub repository, pretrained weights, or automatic upload is configured. Future work: encoder adapter, real dataset, held-out evaluation, model card and gated publishing.

## Provenance
Status: experimental draft; human review required before merge or publication. Synthetic training labels are generated from two input features. Report held-out metrics before making performance claims. Never commit real datasets, credentials or private records.

## Validation scope
The CPU workflow runs the full tests plus training and held-out evaluation. Training
uses seed 42 and 240 samples; evaluation uses an independent generator with seed 43
and 1,000 samples from the same synthetic rule. The evaluation reports class counts,
cross-entropy, accuracy, and majority-class accuracy. Its input is a trusted local
checkpoint with the default eight-input, three-class configuration. Do not tune on
this fixed held-out set and then describe it as an untouched final test set.

Numerical checks cover float32/float64, positive curvature magnitudes 0.1, 1 and 10,
zero/tiny/interior/large vectors, near-boundary behavior and an interior gradient
check. Other dtypes/devices and arbitrary configurations are not validated. Curvature
must be finite and positive; projection margin must be between zero and one.

`c` is the positive magnitude of negative curvature. The origin-map convention uses
`tanh(sqrt(c) * norm(v))`; the inverse uses `atanh`. Projection intentionally clips
large inputs, so their round trips need not recover the original vectors. Where
projection and saturation are inactive, the paired origin maps cancel and the
classifier reduces mathematically to linear–tanh–linear. No hyperbolic advantage is
claimed. Such a claim would require a matched Euclidean baseline and broader data.

Checkpoint loading uses `weights_only=True`; accept only trusted local artifacts.
The tests cover prediction round trips and rejection of missing configuration,
incompatible weights and invalid curvature. This is not a security audit or proof
that arbitrary checkpoint files are safe. Root ignore rules exclude generated
weights and test caches; CI keeps checkpoint files in runner temporary storage.

Historical identity and source-chronology questions remain as marked in
`CONTINUITY_CROSSWALK.md`. Test success does not resolve provenance or constitute
founder approval, merge approval, or permission to publish model artifacts.

## TriVector sparse-expert prototype
`TriVectorMoE` is a separate classical PyTorch experiment inspired by the general
shared/routed expert pattern, not a reproduction of DeepSeek or a pretrained LLM.
It has three routed experts labeled `(-1, 0, +1)` plus a shared computational path.
The labels identify components; they do not impose signed weights, consciousness,
quantum states, or physical saddle-wave behavior.

For each input row, the router selects two experts by default. Their selected
scores are normalized with softmax; only selected rows are sent to each expert.
The output is a classifier applied to:

`shared(x) + sum(selected_weight[i] * expert[i](x))`

```python
import torch
from aletheon_hyperbolic.moe import TriVectorMoE
model = TriVectorMoE()
logits = model(torch.randn(5, 8))
```

Run `python -m aletheon_hyperbolic.compare_moe` from the repository root for a
three-seed comparison with the original classifier. Both receive the same 240
training samples, 1,000 independent held-out samples, Adam learning rate 0.01 and
30 epochs. There is no load-balancing loss or claim of specialist meaning; the
report includes selection counts to expose unequal routing. This initial test
set is now a development diagnostic, not an untouched final benchmark.

Initial CPU results (Python 3.12.14, torch 2.14.1+cpu):

| Initialization seed | Original classifier accuracy | Sparse prototype accuracy |
| --- | --- | --- |
| 42 | 86.4% | 76.9% |
| 44 | 88.6% | 82.1% |
| 45 | 87.8% | 76.5% |
| Mean | 87.6% | 78.5% |

The majority baseline is 34.6%. The sparse prototype has 186 total parameters
versus 195 in the original model. It uses 150 parameters in active components per
row (router, shared path, two experts, head), but this is not a measured runtime
or memory saving: dispatch overhead matters. The original classifier scored
higher in all three trials. These unequal architectures are an initial smoke
comparison, not evidence of an MoE advantage. No task-beneficial synergy has yet
been demonstrated, and the sparse prototype does not use the hyperbolic layer.

The full suite locally passed 64 tests, including selected-only expert dispatch,
weighted output equivalence, router gradients, input-dependent selection and
configuration rejection. CI independently verifies the pushed code. The existing
`load_checkpoint` is for the original classifier only; no sparse checkpoint
format, automatic upload or live service is introduced here.

Design reference: [DeepSeekMoE official source](https://github.com/deepseek-ai/DeepSeek-MoE).
This prototype uses independently written minimal linear/tanh experts.

## Four-leaf clover design
TJ Morris approved the three routed leaves plus the shared **Wormhole Bridge**,
meeting at the **Synergy** center. See [the design and software mapping](CLOVER_DESIGN.md).
This names the existing computation; it does not change activation or predictions.

## Q research function
[Q — Synthetic Biology Research Response](Q_RESEARCH_CHARTER.md) records the
founder-directed mission, scientific references, evidence ledger and proposed research
workflow. This is a prepared specification; it adds no live agent or biological capability.

[Q Vector — twin-tower Syzygy architecture](Q_TWIN_TOWERS.md) records the requested two stacks,
two towers and four conceptual Q elements. It is a design specification, not deployed supercomputer hardware.

[W/Q Mars mission brief](WQ_MARS_MISSION.md): founder-directed destination,
architecture preserved, computational research/planning scope.

[Updated TriVector research map](TRIVECTOR_MAP.md) connects T/J/Q functions, W continuity,
the twin-tower Syzygy and the Mars research mission, preserving earlier mappings.

[Ecosystem retrieval audit](ECOSYSTEM_RETRIEVAL_AUDIT.md) documents observed continuity
failures, corrections, visibility limits and a proposed evaluation of retrieval quality.

## Xe quantum-physics research
[Xenon–Tachyon Gas research models](xe/README.md) provide a xenon ideal-gas baseline
and a separate classical tachyonic scalar-mode calculation, with no assumed coupling.

## TriVector math training
[Artwork-inspired saddle curriculum and measured results](MATH_TRAINING.md) define
twelve reference positions, the inner center label 13 and a reproducible three-class
saddle-height exercise. Neural training uses explicit equations, not image pixels.

## Wormhole geometry
[Runnable Ellis throat and traversal model](WORMHOLE_MODEL.md) provides a two-sided
3D embedding and analytic radial light paths, with equations, examples and tests.

## BE → DO → HAVE framework

[Air, Water, Earth, Fire and Essence](BE_DO_HAVE_ELEMENTS.md) connect the founder-directed symbolic framework to practical research steps, traceable results and the permission record for the GitHub-to-Hugging-Face workflow.

## Quantum-tornado research connection

[Quantum tornado and vector-flow research](QUANTUM_TORNADO_RESEARCH.md) records the 2024 helium-vortex sources, an explicit circulation-vector proposal and acceptance criteria for a future computation.

## Matter diversity and recognizing difference

[Two research notes](MATTER_DIVERSITY_AND_DISTINCTION.md) distinguish the physical origins of ordinary-matter diversity from operational comparison and measurement, preserving the proposed WField laboratory terminology.

## AISI Vector New Math — Living Language Bridge

[Complete white paper v0.1](new_math/LIVING_LANGUAGE_BRIDGE_WHITE_PAPER.md) preserves the October 24 closeout continuation: Genesis 1:1 and John 1:1, multilingual benchmark design, context utilization, continuity retention, the proposed research objective and initial YAML structure. Benchmark execution and human translation review remain pending.
