import torch
import torch_ttnn
import pytest
import pickle
import ttnn
from pathlib import Path
from tests.utils import calculate_accuracy, render_metric_string_list_to_input_args_kwargs


class AtenModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.ops.aten.view.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/codegen", "aten.view.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 5]> self = ?", "List[int] size = [-1, 5]"],
        ["Tensor<[1, 5]> self = ?", "List[int] size = [1, -1]"],
        ["Tensor<[1, 5, 1024]> self = ?", "List[int] size = [5, 1024]"],
        ["Tensor<[5, 3072]> self = ?", "List[int] size = [1, 5, 3072]"],
        ["Tensor<[1, 5, 3072]> self = ?", "List[int] size = [1, 5, 4, -1]"],
        ["Tensor<[1, 5, 4, 256]> self = ?", "List[int] size = [1, 5, 4, 4, 64]"],
        ["Tensor<[1, 5, 1, 16, 2]> self = ?", "List[int] size = [1, 5, 1, 32]"],
        ["Tensor<[1, 5, 16, 16, 2]> self = ?", "List[int] size = [1, 5, 16, 32]"],
        ["Tensor<[1, 16, 5, 64]> self = ?", "List[int] size = [16, 5, 64]"],
        ["Tensor<[1, 16, 64, 5]> self = ?", "List[int] size = [16, 64, 5]"],
        ["Tensor<[16, 5, 5]> self = ?", "List[int] size = [1, 16, 5, 5]"],
        ["Tensor<[1, 16, 5, 5]> self = ?", "List[int] size = [16, 5, 5]"],
        ["Tensor<[16, 5, 64]> self = ?", "List[int] size = [1, 16, 5, 64]"],
        ["Tensor<[1, 5, 16, 64]> self = ?", "List[int] size = [1, 5, 1024]"],
        ["Tensor<[5, 1024]> self = ?", "List[int] size = [1, 5, 1024]"],
        ["Tensor<[5, 4096]> self = ?", "List[int] size = [1, 5, 4096]"],
        ["Tensor<[1, 5, 4096]> self = ?", "List[int] size = [5, 4096]"],
        ["Tensor<[1, 5, 1024]> self = ?", "List[int] size = [1, 5, 1024]"],
        ["Tensor<[5, 51200]> self = ?", "List[int] size = [1, 5, 51200]"],
        ["Tensor<[1, 1]> self = ?", "List[int] size = [-1, 1]"],
        ["Tensor<[1, 6]> self = ?", "List[int] size = [1, -1]"],
        ["Tensor<[1, 1, 1024]> self = ?", "List[int] size = [1, 1024]"],
        ["Tensor<[1, 3072]> self = ?", "List[int] size = [1, 1, 3072]"],
        ["Tensor<[1, 1, 3072]> self = ?", "List[int] size = [1, 1, 4, -1]"],
        ["Tensor<[1, 1, 4, 256]> self = ?", "List[int] size = [1, 1, 4, 4, 64]"],
        ["Tensor<[1, 1, 1, 16, 2]> self = ?", "List[int] size = [1, 1, 1, 32]"],
        ["Tensor<[1, 1, 16, 16, 2]> self = ?", "List[int] size = [1, 1, 16, 32]"],
        ["Tensor<[1, 16, 1, 64]> self = ?", "List[int] size = [16, 1, 64]"],
        ["Tensor<[1, 16, 64, 6]> self = ?", "List[int] size = [16, 64, 6]"],
        ["Tensor<[16, 1, 6]> self = ?", "List[int] size = [1, 16, 1, 6]"],
        ["Tensor<[1, 16, 1, 6]> self = ?", "List[int] size = [16, 1, 6]"],
        ["Tensor<[1, 16, 6, 64]> self = ?", "List[int] size = [16, 6, 64]"],
        ["Tensor<[16, 1, 64]> self = ?", "List[int] size = [1, 16, 1, 64]"],
        ["Tensor<[1, 1, 16, 64]> self = ?", "List[int] size = [1, 1, 1024]"],
        ["Tensor<[1, 1024]> self = ?", "List[int] size = [1, 1, 1024]"],
        ["Tensor<[1, 4096]> self = ?", "List[int] size = [1, 1, 4096]"],
        ["Tensor<[1, 1, 4096]> self = ?", "List[int] size = [1, 4096]"],
        ["Tensor<[1, 1, 1024]> self = ?", "List[int] size = [1, 1, 1024]"],
        ["Tensor<[1, 51200]> self = ?", "List[int] size = [1, 1, 51200]"],
        ["Tensor<[1, s10 + 1]> self = ?", "List[int] size = [1, -1]"],
        ["Tensor<[1, 16, 64, s10 + 1]> self = ?", "List[int] size = [16, 64, <s10 + 1>]"],
        ["Tensor<[16, 1, s10 + 1]> self = ?", "List[int] size = [1, 16, 1, <s10 + 1>]"],
        ["Tensor<[1, 16, 1, s10 + 1]> self = ?", "List[int] size = [16, 1, <s10 + 1>]"],
        ["Tensor<[1, 16, s10 + 1, 64]> self = ?", "List[int] size = [16, <s10 + 1>, 64]"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.view.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.view.default", input_strings
    )
    if status == False:
        pytest.skip("Invalid input strings")
    try:
        result_before = m.forward(*input_args, **input_kwargs)
        metric["native_run"] = True
    except Exception as e:
        print(f"Failed to run native. Raised exception: {e}")
        metric["native_run"] = False
    if metric["native_run"] == True:
        option = torch_ttnn.TorchTtnnOption(device=device)
        # option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        try:
            result_after = m.forward(*input_args, **input_kwargs)
            # option._out_fx_graphs[0].print_tabular()
            metric["run"] = True
        except Exception as e:
            print(f"Failed to run. Raised exception: {e}")
            metric["run"] = False

    if metric["run"] == True:
        try:
            # Check inference result
            accuracy = calculate_accuracy(result_before, result_after)
            if accuracy >= 0.99:
                metric["accuracy"] = True
            else:
                metric["accuracy"] = False
        except Exception as e:
            print(f"Failed to check inference result. Raised exception: {e}")

        try:
            # Check the graph has be rewritten and contain ttnn ops
            nodes = list(option._out_fx_graphs[0].nodes)
            if any(["ttnn" in str(node) for node in nodes]):
                metric["convert_to_ttnn"] = True
            else:
                metric["convert_to_ttnn"] = False
        except Exception as e:
            print(f"Failed to check the graph has ttnn op. Raised exception: {e}")

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] == True
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True
