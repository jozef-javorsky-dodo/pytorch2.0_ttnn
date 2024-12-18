# High Level Operations Status
|    | Operations                              |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:----------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._softmax.default                   |                  2 |           2 |         0 |          0 | ✅          |    1    |
|  1 | aten._softmax_backward_data.default     |                  2 |           0 |         0 |          0 | ✘           |    0    |
|  2 | aten._to_copy.default                   |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
|  3 | aten._unsafe_view.default               |                  4 |           2 |         0 |          0 | 🚧          |    0.5  |
|  4 | aten.add.Tensor                         |                  9 |           4 |         0 |          0 | 🚧          |    0.44 |
|  5 | aten.addmm.default                      |                  6 |           6 |         0 |          0 | ✅          |    1    |
|  6 | aten.arange.default                     |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.argmax.default                     |                  1 |           0 |         0 |          0 | ✘           |    0    |
|  8 | aten.bmm.default                        |                  6 |           4 |         0 |          0 | 🚧          |    0.67 |
|  9 | aten.cat.default                        |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 10 | aten.clone.default                      |                  7 |           6 |         0 |          0 | 🚧          |    0.86 |
| 11 | aten.convolution.default                |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 12 | aten.convolution_backward.default       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 13 | aten.detach.default                     |                  7 |           0 |         0 |          0 | ✘           |    0    |
| 14 | aten.div.Tensor                         |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 15 | aten.embedding.default                  |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 16 | aten.embedding_dense_backward.default   |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 17 | aten.eq.Scalar                          |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 18 | aten.exp.default                        |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 19 | aten.expand.default                     |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 20 | aten.full.default                       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 21 | aten.index.Tensor                       |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 22 | aten.index_put.default                  |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 23 | aten.linalg_vector_norm.default         |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 24 | aten.masked_fill.Scalar                 |                  3 |           1 |         0 |          0 | 🚧          |    0.33 |
| 25 | aten.mm.default                         |                 20 |           3 |         0 |          0 | 🚧          |    0.15 |
| 26 | aten.mul.Tensor                         |                 13 |           6 |         0 |          0 | 🚧          |    0.46 |
| 27 | aten.native_layer_norm.default          |                  3 |           3 |         0 |          0 | ✅          |    1    |
| 28 | aten.native_layer_norm_backward.default |                  3 |           0 |         0 |          0 | ✘           |    0    |
| 29 | aten.neg.default                        |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 30 | aten.new_zeros.default                  |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 31 | aten.rsub.Scalar                        |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 32 | aten.select.int                         |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 33 | aten.select_backward.default            |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 34 | aten.sigmoid.default                    |                  2 |           2 |         0 |          0 | ✅          |    1    |
| 35 | aten.sigmoid_backward.default           |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 36 | aten.slice.Tensor                       |                 10 |           1 |         0 |          0 | 🚧          |    0.1  |
| 37 | aten.slice_backward.default             |                  2 |           0 |         0 |          0 | ✘           |    0    |
| 38 | aten.sum.default                        |                  1 |           0 |         0 |          0 | ✘           |    0    |
| 39 | aten.sum.dim_IntList                    |                  8 |           0 |         0 |          0 | ✘           |    0    |
| 40 | aten.t.default                          |                 16 |           9 |         0 |          0 | 🚧          |    0.56 |
| 41 | aten.transpose.int                      |                 12 |           6 |         0 |          0 | 🚧          |    0.5  |
| 42 | aten.unsqueeze.default                  |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 43 | aten.view.default                       |                 29 |          20 |         0 |          0 | 🚧          |    0.69 |
***
### aten._softmax.default
|    | ATen Input Variations                                                         | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 50, 50]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  1 | Tensor<[16, 7, 7]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | True  |
### aten._softmax_backward_data.default
|    | ATen Input Variations                                                                                                          | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 50, 50]> grad_output = ?,<br>Tensor<[12, 50, 50]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16 | Unknown  | Fallback   | True  |
|  1 | Tensor<[16, 7, 7]> grad_output = ?,<br>Tensor<[16, 7, 7]> output = ?,<br>int dim = -1,<br>int input_dtype = torch.bfloat16     | Unknown  | Fallback   | True  |
### aten._to_copy.default
|    | ATen Input Variations                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                          | Done     | Fallback   | True  |
|  1 | Tensor<[2, 1, 7, 7]> self = ?,<br>Optional[int] dtype = torch.bool                              | None     | Fallback   | True  |
|  2 | Tensor<[2, 7]> self = ?,<br>Optional[int] dtype = torch.int32,<br>Optional[Device] device = cpu | Unknown  | Fallback   | True  |
|  3 | Tensor<[7, 7]> self = ?,<br>Optional[int] dtype = torch.bfloat16                                | Done     | Fallback   | True  |
### aten._unsafe_view.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768] | Done     | Done       | True  |
|  1 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]        | Unknown  | Done       | True  |
|  2 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]    | Done     | Done       | True  |
|  3 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, 7, 64]    | Unknown  | Done       | True  |
### aten.add.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ? | Unknown  | Done       | True  |
|  1 | Tensor<[1, 50, 768]> self = ?,<br>Tensor<[1, 50, 768]> other = ?   | Done     | Done       | True  |
|  2 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?           | Unknown  | Done       | True  |
|  3 | Tensor<[1, 768]> self = ?,<br>Tensor<[1, 768]> other = ?           | Unknown  | Done       | True  |
|  4 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?           | Unknown  | Done       | True  |
|  5 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?   | Unknown  | Done       | True  |
|  6 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[1, 7, 512]> other = ?     | Done     | Done       | True  |
|  7 | Tensor<[2, 7, 512]> self = ?,<br>Tensor<[2, 7, 512]> other = ?     | Done     | Done       | True  |
|  8 | Tensor<[2, 8, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> other = ?   | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                   | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2048]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[3072]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 3072]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[512]> self = ?,<br>Tensor<[14, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ? | Done     | Done       | True  |
|  3 | Tensor<[512]> self = ?,<br>Tensor<[14, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?   | Done     | Done       | True  |
|  4 | Tensor<[768]> self = ?,<br>Tensor<[50, 3072]> mat1 = ?,<br>Tensor<[3072, 768]> mat2 = ? | Done     | Done       | True  |
|  5 | Tensor<[768]> self = ?,<br>Tensor<[50, 768]> mat1 = ?,<br>Tensor<[768, 768]> mat2 = ?   | Done     | Done       | True  |
### aten.arange.default
|    | ATen Input Variations                                                                  | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number end = 2,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.argmax.default
|    | ATen Input Variations                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 7]> self = ?,<br>Optional[int] dim = -1 | None     | Fallback   | True  |
### aten.bmm.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[12, 50, 50]> self = ?,<br>Tensor<[12, 50, 64]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[12, 50, 64]> self = ?,<br>Tensor<[12, 64, 50]> mat2 = ? | Done     | Done       | True  |
|  2 | Tensor<[12, 64, 50]> self = ?,<br>Tensor<[12, 50, 50]> mat2 = ? | Unknown  | Done       | True  |
|  3 | Tensor<[16, 64, 7]> self = ?,<br>Tensor<[16, 7, 7]> mat2 = ?    | Unknown  | Done       | True  |
|  4 | Tensor<[16, 7, 64]> self = ?,<br>Tensor<[16, 64, 7]> mat2 = ?   | Done     | Done       | True  |
|  5 | Tensor<[16, 7, 7]> self = ?,<br>Tensor<[16, 7, 64]> mat2 = ?    | Done     | Done       | True  |
### aten.cat.default
|    | ATen Input Variations                                                  | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 1, 768]>, <[1, 49, 768]>],<br>int dim = 1 | Done     | Done       | True  |
### aten.clone.default
|    | ATen Input Variations                                                                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  1 | Tensor<[1, 50, 12, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
|  2 | Tensor<[12, 50, 50]> self = ?                                                              | Done     | Done       | True  |
|  3 | Tensor<[16, 7, 7]> self = ?                                                                | Done     | Done       | True  |
|  4 | Tensor<[2, 7, 512]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format     | Unknown  | Done       | True  |
|  5 | Tensor<[2, 7, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
|  6 | Tensor<[2, 8, 7, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                        | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[Tensor] bias = ?,<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1 | None     | Fallback   | True  |
### aten.convolution_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                                                                                                               | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768, 7, 7]> grad_output = ?,<br>Tensor<[1, 3, 224, 224]> input = ?,<br>Tensor<[768, 3, 32, 32]> weight = ?,<br>Optional[List[int]] bias_sizes = [0],<br>List[int] stride = [32, 32],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1,<br>List[bool] output_mask = [True, True, False] | Unknown  | Fallback   | True  |
### aten.detach.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   |
|---:|:-------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?        | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 50, 3072]> self = ? | Unknown  | Fallback   | True  |
|  2 | Tensor<[12, 50, 50]> self = ?  | Unknown  | Fallback   | True  |
|  3 | Tensor<[16, 7, 7]> self = ?    | Unknown  | Fallback   | True  |
|  4 | Tensor<[2, 1]> self = ?        | Unknown  | Fallback   | True  |
|  5 | Tensor<[2, 7, 2048]> self = ?  | Unknown  | Fallback   | True  |
|  6 | Tensor<[]> self = ?            | Unknown  | Fallback   | True  |
### aten.div.Tensor
|    | ATen Input Variations                                  | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ? | Done     | Done       | True  |
### aten.embedding.default
|    | ATen Input Variations                                          | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[49408, 512]> weight = ?,<br>Tensor<[2, 7]> indices = ? | Done     | Done       | True  |
|  1 | Tensor<[50, 768]> weight = ?,<br>Tensor<[1, 50]> indices = ?   | Done     | Done       | True  |
|  2 | Tensor<[77, 512]> weight = ?,<br>Tensor<[1, 7]> indices = ?    | Done     | Done       | True  |
### aten.embedding_dense_backward.default
|    | ATen Input Variations                                                                                                                                       | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> grad_output = ?,<br>Tensor<[1, 50]> indices = ?,<br>int num_weights = 50,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False  | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 7, 512]> grad_output = ?,<br>Tensor<[1, 7]> indices = ?,<br>int num_weights = 77,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False    | Unknown  | Fallback   | True  |
|  2 | Tensor<[2, 7, 512]> grad_output = ?,<br>Tensor<[2, 7]> indices = ?,<br>int num_weights = 49408,<br>int padding_idx = -1,<br>bool scale_grad_by_freq = False | Unknown  | Fallback   | True  |
### aten.eq.Scalar
|    | ATen Input Variations                        | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?,<br>number other = 0 | Unknown  | Done       | True  |
|  1 | Tensor<[2, 1]> self = ?,<br>number other = 0 | Unknown  | Done       | True  |
### aten.exp.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor<[]> self = ?     | None     | Fallback   | True  |
### aten.expand.default
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Done     | Done       | True  |
|  1 | Tensor<[2, 1, 1, 7]> self = ?,<br>List[int] size = [2, 1, 7, 7] | Done     | Done       | True  |
|  2 | Tensor<[768]> self = ?,<br>List[int] size = [1, 1, -1]          | Done     | Done       | True  |
### aten.full.default
|    | ATen Input Variations                                                                                                                           | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[int] size = [7, 7],<br>number fill_value = -3.3895313892515355e+38,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
### aten.index.Tensor
|    | ATen Input Variations                                                            | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [<[2]>, <[2]>] | None     | Fallback   | True  |
### aten.index_put.default
|    | ATen Input Variations                                                                                                                       | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 7, 512]> self = ?,<br>List[Optional[Tensor]] indices = [<[2]>, <[2]>],<br>Tensor<[2, 512]> values = ?,<br>bool accumulate = True | Unknown  | Fallback   | True  |
### aten.linalg_vector_norm.default
|    | ATen Input Variations                                                                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 512]> self = ?,<br>number ord = 2,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   | True  |
|  1 | Tensor<[2, 512]> self = ?,<br>number ord = 2,<br>Optional[List[int]] dim = [-1],<br>bool keepdim = True | None     | Fallback   | True  |
### aten.masked_fill.Scalar
|    | ATen Input Variations                                                                                      | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> mask = ?,<br>number value = 0                                 | Unknown  | Fallback   | True  |
|  1 | Tensor<[2, 1, 7, 7]> self = ?,<br>Tensor<[2, 1, 7, 7]> mask = ?,<br>number value = -3.3895313892515355e+38 | Done     | Done       | True  |
|  2 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> mask = ?,<br>number value = 0                                 | Unknown  | Fallback   | True  |
### aten.mm.default
|    | ATen Input Variations                                        | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?        | Unknown  | Done       | True  |
|  1 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 768]> mat2 = ?    | Unknown  | Done       | True  |
|  2 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ?    | Done     | Done       | True  |
|  3 | Tensor<[14, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ? | Unknown  | Done       | True  |
|  4 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Unknown  | Done       | True  |
|  5 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?   | Unknown  | Done       | True  |
|  6 | Tensor<[2, 1]> self = ?,<br>Tensor<[1, 512]> mat2 = ?        | Unknown  | Done       | True  |
|  7 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 1]> mat2 = ?      | Done     | Done       | True  |
|  8 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?    | Done     | Done       | True  |
|  9 | Tensor<[2048, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?   | Unknown  | Done       | True  |
| 10 | Tensor<[3072, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?   | Unknown  | Done       | True  |
| 11 | Tensor<[50, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ? | Unknown  | Done       | True  |
| 12 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?  | Unknown  | Done       | True  |
| 13 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?   | Unknown  | Done       | True  |
| 14 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 2048]> mat2 = ?   | Unknown  | Done       | True  |
| 15 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?    | Unknown  | Done       | True  |
| 16 | Tensor<[512, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?      | Unknown  | Done       | True  |
| 17 | Tensor<[512, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?      | Unknown  | Done       | True  |
| 18 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 3072]> mat2 = ?   | Unknown  | Done       | True  |
| 19 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?    | Unknown  | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?             | Unknown  | Done       | True  |
|  1 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702            | Done     | Done       | True  |
|  2 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ? | Done     | Done       | True  |
|  3 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125             | Done     | Done       | True  |
|  4 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?           | Unknown  | Done       | True  |
|  5 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?               | Unknown  | Done       | True  |
|  6 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?             | Unknown  | Done       | True  |
|  7 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                   | None     | Fallback   | True  |
|  8 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?           | Unknown  | Done       | True  |
|  9 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702             | Done     | Done       | True  |
| 10 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?   | Done     | Done       | True  |
| 11 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125              | Done     | Done       | True  |
| 12 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                       | Unknown  | Fallback   | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |
|  1 | Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>float eps = 1e-05     | Done     | Done       | N/A   |
|  2 | Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | N/A   |
### aten.native_layer_norm_backward.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                   | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> grad_out = ?,<br>Tensor<[1, 50, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Tensor<[1, 50, 1]> mean = ?,<br>Tensor<[1, 50, 1]> rstd = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[bool] output_mask = [True, True, True] | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 768]> grad_out = ?,<br>Tensor<[1, 768]> input = ?,<br>List[int] normalized_shape = [768],<br>Tensor<[1, 1]> mean = ?,<br>Tensor<[1, 1]> rstd = ?,<br>Optional[Tensor]<[768]> weight = ?,<br>Optional[Tensor]<[768]> bias = ?,<br>List[bool] output_mask = [True, True, True]                 | Unknown  | Fallback   | True  |
|  2 | Tensor<[2, 7, 512]> grad_out = ?,<br>Tensor<[2, 7, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Tensor<[2, 7, 1]> mean = ?,<br>Tensor<[2, 7, 1]> rstd = ?,<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[bool] output_mask = [True, True, True]     | Unknown  | Fallback   | True  |
### aten.neg.default
|    | ATen Input Variations     | Status   | Isolated   | PCC   |
|---:|:--------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 512]> self = ? | Unknown  | Done       | True  |
|  1 | Tensor<[2, 512]> self = ? | Unknown  | Done       | True  |
### aten.new_zeros.default
|    | ATen Input Variations                                                                                                                                                          | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 512]> self = ?,<br>List[int] size = [2, 7, 512],<br>Optional[int] dtype = torch.bfloat16,<br>Optional[int] layout = torch.strided,<br>Optional[Device] device = cpu | Unknown  | Fallback   | True  |
### aten.rsub.Scalar
|    | ATen Input Variations                                | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 1, 7, 7]> self = ?,<br>number other = 1.0 | Done     | Done       | True  |
### aten.select.int
|    | ATen Input Variations                                           | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       | True  |
### aten.select_backward.default
|    | ATen Input Variations                                                                                       | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 50, 768],<br>int dim = 1,<br>int index = 0 | Unknown  | Fallback   | True  |
### aten.sigmoid.default
|    | ATen Input Variations          | Status   | Isolated   | PCC   |
|---:|:-------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 3072]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[2, 7, 2048]> self = ?  | Done     | Done       | True  |
### aten.sigmoid_backward.default
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 3072]> grad_output = ?,<br>Tensor<[1, 50, 3072]> output = ? | Unknown  | Fallback   | True  |
|  1 | Tensor<[2, 7, 2048]> grad_output = ?,<br>Tensor<[2, 7, 2048]> output = ?   | Unknown  | Fallback   | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                 | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 1, 7, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 1                   | Unknown  | Done       | True  |
|  4 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 1,<br>Optional[int] end = 50                  | Unknown  | Done       | True  |
|  5 | Tensor<[1, 768]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807     | Unknown  | Fallback   | True  |
|  6 | Tensor<[1, 77]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Fallback   | True  |
|  7 | Tensor<[1, 77]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 7                        | Done     | Done       | True  |
|  8 | Tensor<[2, 1, 1, 7]> self = ?,<br>int dim = 3,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Fallback   | True  |
|  9 | Tensor<[2, 7]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807       | Unknown  | Fallback   | True  |
### aten.slice_backward.default
|    | ATen Input Variations                                                                                                                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 50, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 50, 768],<br>int dim = 0,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1 | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 768]> grad_output = ?,<br>List[int] input_sizes = [1, 768],<br>int dim = 1,<br>int start = 0,<br>int end = 9223372036854775807,<br>int step = 1         | Unknown  | Fallback   | True  |
### aten.sum.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor<[2, 1]> self = ? | Unknown  | Done       | False |
### aten.sum.dim_IntList
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>Optional[List[int]] dim = [0, 1],<br>bool keepdim = True | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 512]> self = ?,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True       | Unknown  | Fallback   | True  |
|  2 | Tensor<[14, 2048]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True     | Unknown  | Fallback   | True  |
|  3 | Tensor<[14, 512]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True      | Unknown  | Fallback   | True  |
|  4 | Tensor<[2, 512]> self = ?,<br>Optional[List[int]] dim = [1],<br>bool keepdim = True       | Unknown  | Fallback   | True  |
|  5 | Tensor<[2, 7, 512]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True    | Unknown  | Fallback   | True  |
|  6 | Tensor<[50, 3072]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True     | Unknown  | Fallback   | True  |
|  7 | Tensor<[50, 768]> self = ?,<br>Optional[List[int]] dim = [0],<br>bool keepdim = True      | Unknown  | Fallback   | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 512]> self = ?    | Done     | Done       | True  |
|  1 | Tensor<[14, 2048]> self = ?  | Unknown  | Done       | True  |
|  2 | Tensor<[14, 512]> self = ?   | Unknown  | Done       | True  |
|  3 | Tensor<[2, 1]> self = ?      | Done     | Done       | True  |
|  4 | Tensor<[2, 512]> self = ?    | Unknown  | Done       | True  |
|  5 | Tensor<[2048, 512]> self = ? | Done     | Done       | True  |
|  6 | Tensor<[3072, 768]> self = ? | Done     | Done       | True  |
|  7 | Tensor<[50, 3072]> self = ?  | Unknown  | Done       | True  |
|  8 | Tensor<[50, 768]> self = ?   | Unknown  | Done       | True  |
|  9 | Tensor<[512, 1]> self = ?    | Unknown  | Done       | True  |
| 10 | Tensor<[512, 2048]> self = ? | Done     | Done       | True  |
| 11 | Tensor<[512, 512]> self = ?  | Done     | Done       | True  |
| 12 | Tensor<[512, 768]> self = ?  | Done     | Done       | True  |
| 13 | Tensor<[768, 3072]> self = ? | Done     | Done       | True  |
| 14 | Tensor<[768, 512]> self = ?  | Unknown  | Done       | True  |
| 15 | Tensor<[768, 768]> self = ?  | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       | True  |
|  1 | Tensor<[1, 49, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       | True  |
|  2 | Tensor<[1, 50, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2 | Done     | Done       | True  |
|  3 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | None     | Unknown    | N/A   |
|  4 | Tensor<[12, 50, 50]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       | True  |
|  5 | Tensor<[12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
|  6 | Tensor<[12, 64, 50]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Unknown  | Done       | True  |
|  7 | Tensor<[16, 64, 7]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Unknown  | Fallback   | True  |
|  8 | Tensor<[16, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       | True  |
|  9 | Tensor<[16, 7, 7]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | Fallback   | True  |
| 10 | Tensor<[2, 7, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
| 11 | Tensor<[2, 8, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                      | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1 | Done     | Done       | True  |
|  1 | Tensor<[2, 1, 7]> self = ?,<br>int dim = 2 | Done     | Done       | True  |
|  2 | Tensor<[2, 7]> self = ?,<br>int dim = 1    | Done     | Done       | True  |
|  3 | Tensor<[7, 7]> self = ?,<br>int dim = 0    | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 768]> self = ?,<br>List[int] size = [768]            | Unknown  | Done       | True  |
|  1 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, -1, 64] | Done     | Done       | True  |
|  2 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] size = [12, 50, 64] | Unknown  | Done       | True  |
|  3 | Tensor<[1, 2048]> self = ?,<br>List[int] size = [2048]             | Unknown  | Done       | True  |
|  4 | Tensor<[1, 3072]> self = ?,<br>List[int] size = [3072]             | Unknown  | Done       | True  |
|  5 | Tensor<[1, 50, 12, 64]> self = ?,<br>List[int] size = [1, 50, 768] | Unknown  | Done       | True  |
|  6 | Tensor<[1, 50, 3072]> self = ?,<br>List[int] size = [50, 3072]     | Done     | Done       | True  |
|  7 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, -1, 12, 64] | Done     | Done       | True  |
|  8 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [1, 50, 12, 64] | Done     | Done       | True  |
|  9 | Tensor<[1, 50, 768]> self = ?,<br>List[int] size = [50, 768]       | Done     | Done       | True  |
| 10 | Tensor<[1, 512]> self = ?,<br>List[int] size = [512]               | Unknown  | Done       | True  |
| 11 | Tensor<[1, 768, 49]> self = ?,<br>List[int] size = [1, 768, 7, 7]  | Unknown  | Done       | True  |
| 12 | Tensor<[1, 768, 7, 7]> self = ?,<br>List[int] size = [1, 768, 49]  | Done     | Done       | True  |
| 13 | Tensor<[1, 768]> self = ?,<br>List[int] size = [768]               | Unknown  | Done       | True  |
| 14 | Tensor<[12, 50, 64]> self = ?,<br>List[int] size = [1, 12, 50, 64] | Done     | Done       | True  |
| 15 | Tensor<[14, 2048]> self = ?,<br>List[int] size = [2, 7, 2048]      | Done     | Done       | True  |
| 16 | Tensor<[14, 512]> self = ?,<br>List[int] size = [2, 7, 512]        | Done     | Done       | True  |
| 17 | Tensor<[16, 7, 64]> self = ?,<br>List[int] size = [2, 8, 7, 64]    | Done     | Done       | True  |
| 18 | Tensor<[16, 7, 7]> self = ?,<br>List[int] size = [2, 8, 7, 7]      | Done     | Done       | True  |
| 19 | Tensor<[2, 7, 2048]> self = ?,<br>List[int] size = [14, 2048]      | Done     | Done       | True  |
| 20 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [14, 512]        | Done     | Done       | True  |
| 21 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, -1, 8, 64]   | Done     | Done       | True  |
| 22 | Tensor<[2, 7, 512]> self = ?,<br>List[int] size = [2, 7, 8, 64]    | Done     | Done       | True  |
| 23 | Tensor<[2, 7, 8, 64]> self = ?,<br>List[int] size = [2, 7, 512]    | Unknown  | Done       | True  |
| 24 | Tensor<[2, 7]> self = ?,<br>List[int] size = [-1, 7]               | Done     | Done       | True  |
| 25 | Tensor<[2, 8, 7, 64]> self = ?,<br>List[int] size = [16, -1, 64]   | Done     | Done       | True  |
| 26 | Tensor<[2, 8, 7, 7]> self = ?,<br>List[int] size = [16, 7, 7]      | Done     | Done       | True  |
| 27 | Tensor<[50, 3072]> self = ?,<br>List[int] size = [1, 50, 3072]     | Done     | Done       | True  |
| 28 | Tensor<[50, 768]> self = ?,<br>List[int] size = [1, 50, 768]       | Done     | Done       | True  |

