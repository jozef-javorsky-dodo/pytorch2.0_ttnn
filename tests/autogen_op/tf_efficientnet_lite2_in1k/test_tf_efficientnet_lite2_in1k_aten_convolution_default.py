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
        return torch.ops.aten.convolution.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/tf_efficientnet_lite2.in1k", "aten.convolution.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        [
            "Tensor<[1, 3, 261, 261]> input = ?",
            "Tensor<[32, 3, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 32, 130, 130]> input = ?",
            "Tensor<[32, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 32",
        ],
        [
            "Tensor<[1, 32, 130, 130]> input = ?",
            "Tensor<[16, 32, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 16, 130, 130]> input = ?",
            "Tensor<[96, 16, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 96, 131, 131]> input = ?",
            "Tensor<[96, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 96",
        ],
        [
            "Tensor<[1, 96, 65, 65]> input = ?",
            "Tensor<[24, 96, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 24, 65, 65]> input = ?",
            "Tensor<[144, 24, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 144, 65, 65]> input = ?",
            "Tensor<[144, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 144",
        ],
        [
            "Tensor<[1, 144, 65, 65]> input = ?",
            "Tensor<[24, 144, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 144, 69, 69]> input = ?",
            "Tensor<[144, 1, 5, 5]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 144",
        ],
        [
            "Tensor<[1, 144, 33, 33]> input = ?",
            "Tensor<[48, 144, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 48, 33, 33]> input = ?",
            "Tensor<[288, 48, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 288, 33, 33]> input = ?",
            "Tensor<[288, 1, 5, 5]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [2, 2]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 288",
        ],
        [
            "Tensor<[1, 288, 33, 33]> input = ?",
            "Tensor<[48, 288, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 288, 35, 35]> input = ?",
            "Tensor<[288, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 288",
        ],
        [
            "Tensor<[1, 288, 17, 17]> input = ?",
            "Tensor<[88, 288, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 88, 17, 17]> input = ?",
            "Tensor<[528, 88, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 528, 17, 17]> input = ?",
            "Tensor<[528, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 528",
        ],
        [
            "Tensor<[1, 528, 17, 17]> input = ?",
            "Tensor<[88, 528, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 528, 17, 17]> input = ?",
            "Tensor<[528, 1, 5, 5]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [2, 2]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 528",
        ],
        [
            "Tensor<[1, 528, 17, 17]> input = ?",
            "Tensor<[120, 528, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 120, 17, 17]> input = ?",
            "Tensor<[720, 120, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 720, 17, 17]> input = ?",
            "Tensor<[720, 1, 5, 5]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [2, 2]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 720",
        ],
        [
            "Tensor<[1, 720, 17, 17]> input = ?",
            "Tensor<[120, 720, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 720, 21, 21]> input = ?",
            "Tensor<[720, 1, 5, 5]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [2, 2]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 720",
        ],
        [
            "Tensor<[1, 720, 9, 9]> input = ?",
            "Tensor<[208, 720, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 208, 9, 9]> input = ?",
            "Tensor<[1248, 208, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 1248, 9, 9]> input = ?",
            "Tensor<[1248, 1, 5, 5]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [2, 2]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1248",
        ],
        [
            "Tensor<[1, 1248, 9, 9]> input = ?",
            "Tensor<[208, 1248, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 1248, 9, 9]> input = ?",
            "Tensor<[1248, 1, 3, 3]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [1, 1]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1248",
        ],
        [
            "Tensor<[1, 1248, 9, 9]> input = ?",
            "Tensor<[352, 1248, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
        [
            "Tensor<[1, 352, 9, 9]> input = ?",
            "Tensor<[1280, 352, 1, 1]> weight = ?",
            "Optional[Tensor] bias = ?",
            "List[int] stride = [1, 1]",
            "List[int] padding = [0, 0]",
            "List[int] dilation = [1, 1]",
            "bool transposed = False",
            "List[int] output_padding = [0, 0]",
            "int groups = 1",
        ],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.convolution.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.convolution.default", input_strings
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
