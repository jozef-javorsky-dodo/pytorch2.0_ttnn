### aten.split.Tensor
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1        | Unknown  | Done       | True  |
|  1 | Tensor<[1, 1, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1   | Unknown  | Done       | True  |
|  2 | Tensor<[1, 1024, 5120]> self = ?,<br>int split_size = 2560,<br>int dim = -1 | Unknown  | Done       | True  |
|  3 | Tensor<[1, 14, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1         | Done     | Done       | True  |
|  4 | Tensor<[1, 25, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1         | Done     | Done       | True  |
|  5 | Tensor<[1, 256, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1 | Unknown  | Done       | True  |
|  6 | Tensor<[1, 256, 2]> self = ?,<br>int split_size = 1,<br>int dim = -1        | Done     | Done       | True  |
|  7 | Tensor<[1, 4096, 2560]> self = ?,<br>int split_size = 1280,<br>int dim = -1 | Unknown  | Done       | True  |
|  8 | Tensor<[1, 5, 32]> self = ?,<br>int split_size = 16,<br>int dim = -1        | Unknown  | Done       | True  |
|  9 | Tensor<[1, 5, 4, 768]> self = ?,<br>int split_size = 256,<br>int dim = -1   | Unknown  | Done       | True  |
| 10 | Tensor<[1, 64, 10240]> self = ?,<br>int split_size = 5120,<br>int dim = -1  | Unknown  | Done       | True  |
| 11 | Tensor<[1, 7, 2304]> self = ?,<br>int split_size = 768,<br>int dim = 2      | None     | Fallback   | True  |
| 12 | Tensor<[768, 256]> self = ?,<br>int split_size = 256                        | None     | Fallback   | True  |
| 13 | Tensor<[768]> self = ?,<br>int split_size = 256                             | None     | Fallback   | True  |

