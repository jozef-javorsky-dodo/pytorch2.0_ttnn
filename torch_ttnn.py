import torch.linalg
import ttnn
import torch.nn as nn
import torch
from torch.fx import symbolic_trace
import operator
from typing import List

torch.fx.graph._register_custom_builtin('Device', 'from ttnn import Device', ttnn.Device)

def linear(i, weight, bias):
    return ttnn.add(ttnn.matmul(i, weight), bias)


def replace_with_ttnn(node, func, device):
    """
    Replace a node with a new node that calls the given function with the same arguments.
    """
    graph: torch.fx.Graph = node.graph
    with graph.inserting_before(node):
        from_torch = tuple(graph.call_function(ttnn.from_torch, (i,)) for i in node.args)
        to_device = tuple(graph.call_function(ttnn.to_device, (i, device)) for i in from_torch)
        ttnn_op = graph.call_function(func, to_device)
        from_device = graph.call_function(ttnn.from_device, (ttnn_op, device))
        to_torch = graph.call_function(ttnn.to_torch, (from_device,))
        node.replace_all_uses_with(to_torch)
        graph.erase_node(node)


def aten_backend(gm: torch.fx.GraphModule, sexample_inputs: List[torch.Tensor]) -> torch.fx.GraphModule:
    """
    The backend for torch.compile that converts a graph to use ttnn.
    The graph is wrapped in torch._dynamo.backends.common.aot_autograd, which
    trace into low level ATen ops not only high level torch ops.
    """
    device = ttnn.Device(7)
    graph: torch.fx.Graph = gm.graph
    for node in gm.graph.nodes:
        if node.op == 'call_function' and node.target == torch.ops.aten.add.Tensor:
            replace_with_ttnn(node, ttnn.add, device)
        elif node.op == 'call_function' and node.target == torch.ops.aten.mul.Tensor:
            replace_with_ttnn(node, ttnn.matmul, device)

    gm.recompile()
    gm.graph.print_tabular()
    return gm

from torch._dynamo.backends.common import aot_autograd
backend = aot_autograd(fw_compiler=aten_backend)
