# Reference: https://pytorch.org/hub/pytorch_vision_hardnet/
# Reference: https://github.com/PingoLH/Pytorch-HarDNet

from PIL import Image
from torchvision import transforms
import requests
import torch
import pytest


@pytest.mark.compilation_xfail
def test_hardnet(record_property):
    record_property("model_name", "HardNet")

    model = torch.hub.load("PingoLH/Pytorch-HarDNet", "hardnet68", pretrained=False)
    checkpoint = "https://ping-chao.com/hardnet/hardnet68-5d684880.pth"
    model.load_state_dict(torch.hub.load_state_dict_from_url(checkpoint, progress=False, map_location="cpu"))
    model.eval()

    url = "https://github.com/mateuszbuda/brain-segmentation-pytorch/raw/master/assets/TCGA_CS_4944.png"
    input_image = Image.open(requests.get(url, stream=True).raw)
    preprocess = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model

    with torch.no_grad():
        output = model(input_batch)

    # Tensor of shape 1000, with confidence scores over ImageNet's 1000 classes
    print(output[0])
    # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    print(probabilities)

    record_property("torch_ttnn", (model, input_batch, output))