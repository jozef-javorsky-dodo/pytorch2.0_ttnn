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
        return torch.ops.aten.constant_pad_nd.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.constant_pad_nd.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 56, 56, 128]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 28, 28, 256]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 14, 14, 512]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 7, 7, 1024]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 56, 56, 96]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 28, 28, 192]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 14, 14, 384]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 7, 7, 768]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 64, 64, 128]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 32, 32, 256]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 16, 16, 512]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 8, 8, 1024]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 64, 64, 96]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 32, 32, 192]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 16, 16, 384]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 8, 8, 768]> self = ?", "List[int] pad = [0, 0, 0, 0, 0, 0]", "number value = 0.0"],
        ["Tensor<[1, 3, 224, 224]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 96, 112, 112]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 144, 56, 56]> self = ?", "List[int] pad = [1, 2, 1, 2]", "number value = 0.0"],
        ["Tensor<[1, 240, 28, 28]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 672, 14, 14]> self = ?", "List[int] pad = [1, 2, 1, 2]", "number value = 0.0"],
        ["Tensor<[1, 672, 17, 17]> self = ?", "List[int] pad = [-1, -2, -1, -2]"],
        ["Tensor<[1, 240, 29, 29]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 144, 59, 59]> self = ?", "List[int] pad = [-1, -2, -1, -2]"],
        ["Tensor<[1, 96, 113, 113]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 3, 225, 225]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 3, 240, 240]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 96, 120, 120]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 144, 60, 60]> self = ?", "List[int] pad = [1, 2, 1, 2]", "number value = 0.0"],
        ["Tensor<[1, 240, 30, 30]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 672, 15, 15]> self = ?", "List[int] pad = [2, 2, 2, 2]", "number value = 0.0"],
        ["Tensor<[1, 672, 19, 19]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
        ["Tensor<[1, 240, 31, 31]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 144, 63, 63]> self = ?", "List[int] pad = [-1, -2, -1, -2]"],
        ["Tensor<[1, 96, 121, 121]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 3, 241, 241]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 3, 260, 260]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 96, 130, 130]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 144, 65, 65]> self = ?", "List[int] pad = [2, 2, 2, 2]", "number value = 0.0"],
        ["Tensor<[1, 288, 33, 33]> self = ?", "List[int] pad = [1, 1, 1, 1]", "number value = 0.0"],
        ["Tensor<[1, 720, 17, 17]> self = ?", "List[int] pad = [2, 2, 2, 2]", "number value = 0.0"],
        ["Tensor<[1, 720, 21, 21]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
        ["Tensor<[1, 288, 35, 35]> self = ?", "List[int] pad = [-1, -1, -1, -1]"],
        ["Tensor<[1, 144, 69, 69]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
        ["Tensor<[1, 96, 131, 131]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 3, 261, 261]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 3, 300, 300]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 144, 150, 150]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 192, 75, 75]> self = ?", "List[int] pad = [2, 2, 2, 2]", "number value = 0.0"],
        ["Tensor<[1, 288, 38, 38]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 816, 19, 19]> self = ?", "List[int] pad = [2, 2, 2, 2]", "number value = 0.0"],
        ["Tensor<[1, 816, 23, 23]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
        ["Tensor<[1, 288, 39, 39]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 192, 79, 79]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
        ["Tensor<[1, 144, 151, 151]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 3, 301, 301]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 3, 380, 380]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 144, 190, 190]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 192, 95, 95]> self = ?", "List[int] pad = [2, 2, 2, 2]", "number value = 0.0"],
        ["Tensor<[1, 336, 48, 48]> self = ?", "List[int] pad = [0, 1, 0, 1]", "number value = 0.0"],
        ["Tensor<[1, 960, 24, 24]> self = ?", "List[int] pad = [1, 2, 1, 2]", "number value = 0.0"],
        ["Tensor<[1, 960, 27, 27]> self = ?", "List[int] pad = [-1, -2, -1, -2]"],
        ["Tensor<[1, 336, 49, 49]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 192, 99, 99]> self = ?", "List[int] pad = [-2, -2, -2, -2]"],
        ["Tensor<[1, 144, 191, 191]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
        ["Tensor<[1, 3, 381, 381]> self = ?", "List[int] pad = [0, -1, 0, -1]"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.constant_pad_nd.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.constant_pad_nd.default", input_strings
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
