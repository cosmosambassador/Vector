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
