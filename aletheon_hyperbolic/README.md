# Aletheon Hyperbolic Research v0.1
Experimental PyTorch Poincare-ball tangent-space classifier. **Not a pretrained Aletheon model.**

## Setup
```bash
python -m pip install torch pytest
python -m pytest tests/test_aletheon_hyperbolic.py
python -m aletheon_hyperbolic.train --epochs 30
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
