# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  9 |           9 |         0 |          0 | ✅          |    1    |
|  1 | aten.add.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten.addmm.default                                |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  3 | aten.convolution.default                          |                 34 |          32 |         0 |          0 | 🚧          |    0.94 |
|  4 | aten.mean.dim                                     |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  5 | aten.mul.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  6 | aten.relu.default                                 |                 13 |          13 |         0 |          0 | ✅          |    1    |
|  7 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  8 | aten.t.default                                    |                  1 |           1 |         0 |          0 | ✅          |    1    |
|  9 | aten.view.default                                 |                  1 |           1 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1512, 14, 14]> input = ?,<br>Optional[Tensor]<[1512]> weight = ?,<br>Optional[Tensor]<[1512]> bias = ?,<br>Tensor<[1512]> running_mean = ?,<br>Tensor<[1512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | True  |
|  1 | Tensor<[1, 1512, 7, 7]> input = ?,<br>Optional[Tensor]<[1512]> weight = ?,<br>Optional[Tensor]<[1512]> bias = ?,<br>Tensor<[1512]> running_mean = ?,<br>Tensor<[1512]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | True  |
|  2 | Tensor<[1, 216, 28, 28]> input = ?,<br>Optional[Tensor]<[216]> weight = ?,<br>Optional[Tensor]<[216]> bias = ?,<br>Tensor<[216]> running_mean = ?,<br>Tensor<[216]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | True  |
|  3 | Tensor<[1, 216, 56, 56]> input = ?,<br>Optional[Tensor]<[216]> weight = ?,<br>Optional[Tensor]<[216]> bias = ?,<br>Tensor<[216]> running_mean = ?,<br>Tensor<[216]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | True  |
|  4 | Tensor<[1, 32, 112, 112]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | True  |
|  5 | Tensor<[1, 576, 14, 14]> input = ?,<br>Optional[Tensor]<[576]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>Tensor<[576]> running_mean = ?,<br>Tensor<[576]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | True  |
|  6 | Tensor<[1, 576, 28, 28]> input = ?,<br>Optional[Tensor]<[576]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>Tensor<[576]> running_mean = ?,<br>Tensor<[576]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05      | Done     | Done       | True  |
|  7 | Tensor<[1, 72, 112, 112]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05         | Done     | Done       | True  |
|  8 | Tensor<[1, 72, 56, 56]> input = ?,<br>Optional[Tensor]<[72]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>Tensor<[72]> running_mean = ?,<br>Tensor<[72]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05           | Done     | Done       | True  |
### aten.add.Tensor
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?   | Done     | Done       | True  |
|  1 | Tensor<[1, 216, 28, 28]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 576, 14, 14]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ? | Done     | Done       | True  |
|  3 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?   | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                    | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000]> self = ?,<br>Tensor<[1, 1512]> mat1 = ?,<br>Tensor<[1512, 1000]> mat2 = ? | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                             | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 144, 1, 1]> input = ?,<br>Tensor<[1512, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<[1512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
|  1 | Tensor<[1, 144, 1, 1]> input = ?,<br>Tensor<[576, 144, 1, 1]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
|  2 | Tensor<[1, 1512, 1, 1]> input = ?,<br>Tensor<[144, 1512, 1, 1]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | Done     | Done       | True  |
|  3 | Tensor<[1, 1512, 14, 14]> input = ?,<br>Tensor<[1512, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 63      | Done     | Done       | True  |
|  4 | Tensor<[1, 1512, 7, 7]> input = ?,<br>Tensor<[1512, 1512, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Fallback   | True  |
|  5 | Tensor<[1, 18, 1, 1]> input = ?,<br>Tensor<[216, 18, 1, 1]> weight = ?,<br>Optional[Tensor]<[216]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
|  6 | Tensor<[1, 18, 1, 1]> input = ?,<br>Tensor<[72, 18, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
|  7 | Tensor<[1, 216, 1, 1]> input = ?,<br>Tensor<[18, 216, 1, 1]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
|  8 | Tensor<[1, 216, 1, 1]> input = ?,<br>Tensor<[54, 216, 1, 1]> weight = ?,<br>Optional[Tensor]<[54]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
|  9 | Tensor<[1, 216, 28, 28]> input = ?,<br>Tensor<[216, 216, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | True  |
| 10 | Tensor<[1, 216, 28, 28]> input = ?,<br>Tensor<[216, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9         | Done     | Done       | True  |
| 11 | Tensor<[1, 216, 28, 28]> input = ?,<br>Tensor<[576, 216, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | True  |
| 12 | Tensor<[1, 216, 28, 28]> input = ?,<br>Tensor<[576, 216, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | None     | Fallback   | True  |
| 13 | Tensor<[1, 216, 56, 56]> input = ?,<br>Tensor<[216, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 9         | Done     | Done       | True  |
| 14 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[32, 3, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | True  |
| 15 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[72, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 16 | Tensor<[1, 32, 112, 112]> input = ?,<br>Tensor<[72, 32, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 17 | Tensor<[1, 54, 1, 1]> input = ?,<br>Tensor<[216, 54, 1, 1]> weight = ?,<br>Optional[Tensor]<[216]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 18 | Tensor<[1, 54, 1, 1]> input = ?,<br>Tensor<[576, 54, 1, 1]> weight = ?,<br>Optional[Tensor]<[576]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 19 | Tensor<[1, 576, 1, 1]> input = ?,<br>Tensor<[144, 576, 1, 1]> weight = ?,<br>Optional[Tensor]<[144]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1   | Done     | Done       | True  |
| 20 | Tensor<[1, 576, 1, 1]> input = ?,<br>Tensor<[54, 576, 1, 1]> weight = ?,<br>Optional[Tensor]<[54]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 21 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[1512, 576, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
| 22 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[1512, 576, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
| 23 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24        | Done     | Done       | True  |
| 24 | Tensor<[1, 576, 14, 14]> input = ?,<br>Tensor<[576, 576, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1        | Done     | Done       | True  |
| 25 | Tensor<[1, 576, 28, 28]> input = ?,<br>Tensor<[576, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 24        | Done     | Done       | True  |
| 26 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[18, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[18]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
| 27 | Tensor<[1, 72, 1, 1]> input = ?,<br>Tensor<[8, 72, 1, 1]> weight = ?,<br>Optional[Tensor]<[8]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 28 | Tensor<[1, 72, 112, 112]> input = ?,<br>Tensor<[72, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3         | Done     | Done       | True  |
| 29 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[216, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | True  |
| 30 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[216, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1          | Done     | Done       | True  |
| 31 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 24, 3, 3]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 3           | Done     | Done       | True  |
| 32 | Tensor<[1, 72, 56, 56]> input = ?,<br>Tensor<[72, 72, 1, 1]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | True  |
| 33 | Tensor<[1, 8, 1, 1]> input = ?,<br>Tensor<[72, 8, 1, 1]> weight = ?,<br>Optional[Tensor]<[72]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
### aten.mean.dim
|    | ATen Input Variations                                                                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1512, 7, 7]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | False |
|  1 | Tensor<[1, 216, 28, 28]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | False |
|  2 | Tensor<[1, 576, 14, 14]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True | Done     | Done       | False |
|  3 | Tensor<[1, 72, 56, 56]> self = ?,<br>Optional[List[int]] dim = [-1, -2],<br>bool keepdim = True  | Done     | Done       | False |
### aten.mul.Tensor
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ? | Done     | Done       | True  |
|  3 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?   | Done     | Done       | True  |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 144, 1, 1]> self = ?    | Done     | Done       | True  |
|  1 | Tensor<[1, 1512, 14, 14]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 1512, 7, 7]> self = ?   | Done     | Done       | True  |
|  3 | Tensor<[1, 18, 1, 1]> self = ?     | Done     | Done       | True  |
|  4 | Tensor<[1, 216, 28, 28]> self = ?  | Done     | Done       | True  |
|  5 | Tensor<[1, 216, 56, 56]> self = ?  | Done     | Done       | True  |
|  6 | Tensor<[1, 32, 112, 112]> self = ? | Done     | Done       | True  |
|  7 | Tensor<[1, 54, 1, 1]> self = ?     | Done     | Done       | True  |
|  8 | Tensor<[1, 576, 14, 14]> self = ?  | Done     | Done       | True  |
|  9 | Tensor<[1, 576, 28, 28]> self = ?  | Done     | Done       | True  |
| 10 | Tensor<[1, 72, 112, 112]> self = ? | Done     | Done       | True  |
| 11 | Tensor<[1, 72, 56, 56]> self = ?   | Done     | Done       | True  |
| 12 | Tensor<[1, 8, 1, 1]> self = ?      | Done     | Done       | True  |
### aten.sigmoid.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   |
|---:|:---------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1512, 1, 1]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 216, 1, 1]> self = ?  | Done     | Done       | True  |
|  2 | Tensor<[1, 576, 1, 1]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[1, 72, 1, 1]> self = ?   | Done     | Done       | True  |
### aten.t.default
|    | ATen Input Variations         | Status   | Isolated   | PCC   |
|---:|:------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1000, 1512]> self = ? | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1512, 1, 1]> self = ?,<br>List[int] size = [1, 1512] | Done     | Done       | True  |

