import torch

try:
    import ttnn
except ImportError:
    print("ttnn is not installed, use mock_ttnn instead")
    import mock_ttnn as ttnn


def mm_pat(x, y):
    return torch.ops.aten.mm.default(x, y)


def mm_rep(x, y):
    return ttnn.matmul(x, y)


def mm_pat2(x):
    return torch.ops.aten.mm.default(x, x)


def mm_rep2(x):
    return ttnn.matmul(x, x)


pat_rep_list = [
    (mm_pat, mm_rep),
    (mm_pat2, mm_rep2),
]
