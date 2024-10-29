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
        return torch.ops.aten.clone.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/swin_v2_t", "aten.clone.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[3, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 3, 64, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 3, 32, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 3, 64, 64]> self = ?"],
        ["Tensor<[64, 64, 3, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 64, 96]> self = ?"],
        ["Tensor<[1, 64, 64, 384]> self = ?"],
        ["Tensor<[1, 64, 64, 96]> self = ?"],
        ["Tensor<[8, 8, 8, 8]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[6, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 4, 4, 8, 8, 192]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 6, 64, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 6, 32, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 6, 64, 64]> self = ?"],
        ["Tensor<[16, 64, 6, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 64, 192]> self = ?"],
        ["Tensor<[1, 4, 8, 4, 8, 192]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 32, 32, 768]> self = ?"],
        ["Tensor<[1, 32, 32, 192]> self = ?"],
        ["Tensor<[4, 4, 8, 8]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[12, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 2, 2, 8, 8, 384]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 12, 64, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 12, 32, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 12, 64, 64]> self = ?"],
        ["Tensor<[4, 64, 12, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 64, 384]> self = ?"],
        ["Tensor<[1, 2, 8, 2, 8, 384]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 16, 16, 1536]> self = ?"],
        ["Tensor<[1, 16, 16, 384]> self = ?"],
        ["Tensor<[2, 2, 8, 8]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[24, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 24, 64, 64]> self = ?"],
        ["Tensor<[1, 64, 24, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 64, 768]> self = ?"],
        ["Tensor<[1, 8, 8, 3072]> self = ?"],
        ["Tensor<[1, 8, 8, 768]> self = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.clone.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.clone.default", input_strings
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