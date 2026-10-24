import math
import torch

def _validate_curvature(c):
    if not isinstance(c, (int, float)) or not math.isfinite(c) or c <= 0:
        raise ValueError("c must be a finite positive scalar")

def project(x, c=1.0, eps=1e-5):
    _validate_curvature(c)
    if not math.isfinite(eps) or not 0 < eps < 1:
        raise ValueError("eps must be finite and between zero and one")
    limit = (1-eps)/(c**0.5)
    norm = x.norm(dim=-1, keepdim=True).clamp_min(1e-15)
    return x * (limit/norm).clamp(max=1.0)
def exp0(v, c=1.0):
    _validate_curvature(c)
    norm = v.norm(dim=-1, keepdim=True).clamp_min(1e-15)
    root = c**0.5
    return project(torch.tanh(root*norm)*v/(root*norm), c)
def log0(x, c=1.0):
    x = project(x, c)
    norm = x.norm(dim=-1, keepdim=True).clamp_min(1e-15)
    root = c**0.5
    z = (root*norm).clamp(max=1-1e-6)
    return torch.atanh(z)*x/(root*norm)
