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
        return torch.ops.aten.mul.Tensor(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/retinanet_resnet50_fpn", "aten.mul.Tensor")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[800]> self = ?", "Tensor other = 0.6"],
        ["Tensor<[1066]> self = ?", "Tensor other = 0.600375234521576"],
        ["Tensor<[1, 3, 800, 1066]> self = ?", "Tensor<[800, 1]> other = ?"],
        ["Tensor<[1, 3, 800, 1066]> self = ?", "Tensor<[1066]> other = ?"],
        ["Tensor<[1, 64, 1, 1]> self = ?", "Tensor<[1, 64, 1, 1]> other = ?"],
        ["Tensor<[1, 64, 400, 544]> self = ?", "Tensor<[1, 64, 1, 1]> other = ?"],
        ["Tensor<[1, 64, 200, 272]> self = ?", "Tensor<[1, 64, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 1, 1]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 200, 272]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 128, 1, 1]> self = ?", "Tensor<[1, 128, 1, 1]> other = ?"],
        ["Tensor<[1, 128, 200, 272]> self = ?", "Tensor<[1, 128, 1, 1]> other = ?"],
        ["Tensor<[1, 128, 100, 136]> self = ?", "Tensor<[1, 128, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 1, 1]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 100, 136]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 100, 136]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 256, 50, 68]> self = ?", "Tensor<[1, 256, 1, 1]> other = ?"],
        ["Tensor<[1, 1024, 1, 1]> self = ?", "Tensor<[1, 1024, 1, 1]> other = ?"],
        ["Tensor<[1, 1024, 50, 68]> self = ?", "Tensor<[1, 1024, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 50, 68]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 512, 25, 34]> self = ?", "Tensor<[1, 512, 1, 1]> other = ?"],
        ["Tensor<[1, 2048, 1, 1]> self = ?", "Tensor<[1, 2048, 1, 1]> other = ?"],
        ["Tensor<[1, 2048, 25, 34]> self = ?", "Tensor<[1, 2048, 1, 1]> other = ?"],
        ["Tensor<[50]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[68]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[100]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[136]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[136]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[100]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[68]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[50]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[34]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[25]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[17]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[13]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[9]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[7]> self = ?", "Tensor<[]> other = ?"],
        ["Tensor<[0]> self = ?", "Tensor other = 0.5"],
        ["Tensor<[0, 1]> self = ?", "Tensor<[0, 1]> other = ?"],
        ["Tensor<[]> self = ?", "Tensor<[0, 1]> other = ?"],
        ["Tensor<[0]> self = ?", "Tensor<[]> other = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.mul.Tensor",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs("aten.mul.Tensor", input_strings)
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
