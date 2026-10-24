# SPDX-License-Identifier: LGPL-2.1-only
import math

def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError("Expected a finite number")
    return value

def utilization(tokens, capacity):
    """N/C; null propagates. Same token accounting is caller's responsibility."""
    if tokens is None or capacity is None:
        return None
    _number(tokens); _number(capacity)
    if tokens < 0 or capacity <= 0 or tokens > capacity:
        raise ValueError("Require 0 <= tokens <= capacity and capacity > 0")
    return tokens / capacity

def retention(outcomes):
    """True means preserved; False means lost/corrupted; empty is undefined."""
    if any(type(v) is not bool for v in outcomes):
        raise ValueError("Each checklist result must be boolean")
    if not outcomes:
        return {"L": None, "Q": None}
    loss = outcomes.count(False) / len(outcomes)
    return {"L": loss, "Q": 1 - loss}

def objective(discrepancy, loss, cost, loss_weight, cost_weight):
    """D + lambda*L + mu*Cost. Caller must establish compatible units."""
    values = (discrepancy, loss, cost, loss_weight, cost_weight)
    if any(v is None for v in values):
        return None
    for v in values:
        if _number(v) < 0:
            raise ValueError("Inputs and weights must be nonnegative")
    if loss > 1:
        raise ValueError("Loss must be between zero and one")
    return discrepancy + loss_weight * loss + cost_weight * cost
