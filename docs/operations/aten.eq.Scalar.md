### aten.eq.Scalar
|    | ATen Input Variations                              | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 16]> self = ?,<br>number other = 0      | None     | Fallback   | True  |
|  1 | Tensor<[1, 1]> self = ?,<br>number other = 0       | None     | Fallback   | True  |
|  2 | Tensor<[1, 7]> self = ?,<br>number other = 1       | None     | Fallback   | True  |
|  3 | Tensor<[1, 7]> self = ?,<br>number other = 50256   | None     | Fallback   | True  |
|  4 | Tensor<[16, 49, 49]> self = ?,<br>number other = 0 | None     | Fallback   | True  |
|  5 | Tensor<[16, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       | True  |
|  6 | Tensor<[1]> self = ?,<br>number other = 1          | None     | Fallback   | True  |
|  7 | Tensor<[1]> self = ?,<br>number other = 50256      | None     | Fallback   | True  |
|  8 | Tensor<[2, 1]> self = ?,<br>number other = 0       | None     | Fallback   | True  |
|  9 | Tensor<[4, 49, 49]> self = ?,<br>number other = 0  | None     | Fallback   | True  |
| 10 | Tensor<[4, 64, 64]> self = ?,<br>number other = 0  | Done     | Done       | True  |
| 11 | Tensor<[64, 49, 49]> self = ?,<br>number other = 0 | None     | Fallback   | True  |
| 12 | Tensor<[64, 64, 64]> self = ?,<br>number other = 0 | Done     | Done       | True  |

