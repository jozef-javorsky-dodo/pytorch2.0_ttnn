# High Level Operations Status
|    | Operations                                        |   Input Variations |   Converted |   Removed |   Fallback | Completed   |   Score |
|---:|:--------------------------------------------------|-------------------:|------------:|----------:|-----------:|:------------|--------:|
|  0 | aten._native_batch_norm_legit_no_training.default |                  6 |           6 |         0 |          0 | ✅          |    1    |
|  1 | aten._softmax.default                             |                  4 |           4 |         0 |          0 | ✅          |    1    |
|  2 | aten._to_copy.default                             |                 20 |          10 |         0 |          0 | 🚧          |    0.5  |
|  3 | aten._unsafe_index.Tensor                         |                  5 |           0 |         0 |          0 | ✘           |    0    |
|  4 | aten.add.Tensor                                   |                 19 |          18 |         0 |          0 | 🚧          |    0.95 |
|  5 | aten.addmm.default                                |                 15 |          15 |         0 |          0 | ✅          |    1    |
|  6 | aten.arange.default                               |                 10 |           0 |         0 |          0 | ✘           |    0    |
|  7 | aten.bmm.default                                  |                  8 |           8 |         0 |          0 | ✅          |    1    |
|  8 | aten.cat.default                                  |                  3 |           3 |         0 |          0 | ✅          |    1    |
|  9 | aten.ceil.default                                 |                 10 |           0 |         0 |          0 | ✘           |    0    |
| 10 | aten.clamp.default                                |                 20 |           0 |         0 |          0 | ✘           |    0    |
| 11 | aten.clone.default                                |                 19 |          19 |         0 |          0 | ✅          |    1    |
| 12 | aten.convolution.default                          |                 25 |          18 |         0 |          0 | 🚧          |    0.72 |
| 13 | aten.div.Tensor                                   |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 14 | aten.expand.default                               |                 15 |           0 |         0 |          0 | ✘           |    0    |
| 15 | aten.gelu.default                                 |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 16 | aten.mul.Tensor                                   |                 24 |          21 |         0 |          0 | 🚧          |    0.88 |
| 17 | aten.native_layer_norm.default                    |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 18 | aten.permute.default                              |                 21 |          21 |         0 |          0 | ✅          |    1    |
| 19 | aten.relu.default                                 |                  7 |           7 |         0 |          0 | ✅          |    1    |
| 20 | aten.rsub.Scalar                                  |                 10 |          10 |         0 |          0 | ✅          |    1    |
| 21 | aten.select.int                                   |                  6 |           6 |         0 |          0 | ✅          |    1    |
| 22 | aten.sigmoid.default                              |                  4 |           4 |         0 |          0 | ✅          |    1    |
| 23 | aten.slice.Tensor                                 |                  9 |           0 |         0 |          0 | ✘           |    0    |
| 24 | aten.squeeze.dim                                  |                  1 |           1 |         0 |          0 | ✅          |    1    |
| 25 | aten.sub.Tensor                                   |                 20 |          19 |         0 |          0 | 🚧          |    0.95 |
| 26 | aten.t.default                                    |                 12 |          12 |         0 |          0 | ✅          |    1    |
| 27 | aten.transpose.int                                |                 16 |          16 |         0 |          0 | ✅          |    1    |
| 28 | aten.unsqueeze.default                            |                  8 |           7 |         0 |          0 | 🚧          |    0.88 |
| 29 | aten.view.default                                 |                 78 |          78 |         0 |          0 | ✅          |    1    |
***
### aten._native_batch_norm_legit_no_training.default
|    | ATen Input Variations                                                                                                                                                                                                           | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 32, 120, 160]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | True  |
|  1 | Tensor<[1, 32, 30, 40]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | True  |
|  2 | Tensor<[1, 32, 60, 80]> input = ?,<br>Optional[Tensor]<[32]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>Tensor<[32]> running_mean = ?,<br>Tensor<[32]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | True  |
|  3 | Tensor<[1, 64, 120, 160]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05 | Done     | Done       | True  |
|  4 | Tensor<[1, 64, 30, 40]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | True  |
|  5 | Tensor<[1, 64, 60, 80]> input = ?,<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>Tensor<[64]> running_mean = ?,<br>Tensor<[64]> running_var = ?,<br>float momentum = 0.1,<br>float eps = 1e-05   | Done     | Done       | True  |
### aten._softmax.default
|    | ATen Input Variations                                                               | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False | Done     | Done       | True  |
|  1 | Tensor<[1, 2, 4800, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | True  |
|  2 | Tensor<[1, 5, 1200, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False  | Done     | Done       | True  |
|  3 | Tensor<[1, 8, 300, 300]> self = ?,<br>int dim = -1,<br>bool half_to_float = False   | Done     | Done       | True  |
### aten._to_copy.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   | True  |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   | True  |
|  2 | Tensor<[1, 64, 15, 20]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   | True  |
|  3 | Tensor<[1, 64, 240, 320]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   | True  |
|  4 | Tensor<[1, 64, 240, 320]> self = ?,<br>Optional[int] dtype = torch.float32  | Done     | Fallback   | True  |
|  5 | Tensor<[1, 64, 30, 40]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Done     | Fallback   | True  |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   | True  |
|  7 | Tensor<[1, 64, 480, 640]> self = ?,<br>Optional[int] dtype = torch.bfloat16 | Done     | Fallback   | True  |
|  8 | Tensor<[1, 64, 60, 80]> self = ?,<br>Optional[int] dtype = torch.bfloat16   | Done     | Fallback   | True  |
|  9 | Tensor<[1, 64, 60, 80]> self = ?,<br>Optional[int] dtype = torch.float32    | Done     | Fallback   | True  |
| 10 | Tensor<[120]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Fallback   | True  |
| 11 | Tensor<[160]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Fallback   | True  |
| 12 | Tensor<[240]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Fallback   | True  |
| 13 | Tensor<[30]> self = ?,<br>Optional[int] dtype = torch.int64                 | None     | Fallback   | True  |
| 14 | Tensor<[320]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Fallback   | True  |
| 15 | Tensor<[40]> self = ?,<br>Optional[int] dtype = torch.int64                 | None     | Fallback   | True  |
| 16 | Tensor<[480]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Fallback   | True  |
| 17 | Tensor<[60]> self = ?,<br>Optional[int] dtype = torch.int64                 | None     | Fallback   | True  |
| 18 | Tensor<[640]> self = ?,<br>Optional[int] dtype = torch.int64                | None     | Fallback   | True  |
| 19 | Tensor<[80]> self = ?,<br>Optional[int] dtype = torch.int64                 | None     | Fallback   | True  |
### aten._unsafe_index.Tensor
|    | ATen Input Variations                                                                                     | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[240, 1]>, <[320]>] | None     | Unknown    | N/A   |
|  1 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[30, 1]>, <[40]>]     | None     | Unknown    | N/A   |
|  2 | Tensor<[1, 64, 240, 320]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[480, 1]>, <[640]>] | None     | Unknown    | N/A   |
|  3 | Tensor<[1, 64, 30, 40]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[60, 1]>, <[80]>]     | None     | Unknown    | N/A   |
|  4 | Tensor<[1, 64, 60, 80]> self = ?,<br>List[Optional[Tensor]] indices = [None, None, <[120, 1]>, <[160]>]   | None     | Unknown    | N/A   |
### aten.add.Tensor
|    | ATen Input Variations                                                      | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1200, 320]> self = ?,<br>Tensor<[1, 1200, 320]> other = ?       | Done     | Done       | True  |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 19200, 64]> other = ?       | Done     | Done       | True  |
|  2 | Tensor<[1, 300, 512]> self = ?,<br>Tensor<[1, 300, 512]> other = ?         | Done     | Done       | True  |
|  3 | Tensor<[1, 4800, 128]> self = ?,<br>Tensor<[1, 4800, 128]> other = ?       | Done     | Done       | True  |
|  4 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 64, 120, 160]> other = ? | Done     | Done       | True  |
|  5 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[1, 64, 240, 320]> other = ? | Done     | Done       | True  |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 64, 30, 40]> other = ?     | Done     | Done       | True  |
|  7 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[1, 64, 480, 640]> other = ? | Done     | Done       | True  |
|  8 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 64, 60, 80]> other = ?     | Done     | Done       | True  |
|  9 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | True  |
| 10 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | True  |
| 11 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | True  |
| 12 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                               | Done     | Done       | True  |
| 13 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                              | None     | Fallback   | True  |
| 14 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                               | Done     | Done       | True  |
| 15 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | True  |
| 16 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                               | Done     | Done       | True  |
| 17 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | True  |
| 18 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                               | Done     | Done       | True  |
### aten.addmm.default
|    | ATen Input Variations                                                                     | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1280]> self = ?,<br>Tensor<[1200, 320]> mat1 = ?,<br>Tensor<[320, 1280]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[128]> self = ?,<br>Tensor<[300, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?    | Done     | Done       | True  |
|  2 | Tensor<[128]> self = ?,<br>Tensor<[4800, 128]> mat1 = ?,<br>Tensor<[128, 128]> mat2 = ?   | Done     | Done       | True  |
|  3 | Tensor<[128]> self = ?,<br>Tensor<[4800, 512]> mat1 = ?,<br>Tensor<[512, 128]> mat2 = ?   | Done     | Done       | True  |
|  4 | Tensor<[2048]> self = ?,<br>Tensor<[300, 512]> mat1 = ?,<br>Tensor<[512, 2048]> mat2 = ?  | Done     | Done       | True  |
|  5 | Tensor<[256]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 256]> mat2 = ?    | Done     | Done       | True  |
|  6 | Tensor<[320]> self = ?,<br>Tensor<[1200, 1280]> mat1 = ?,<br>Tensor<[1280, 320]> mat2 = ? | Done     | Done       | True  |
|  7 | Tensor<[320]> self = ?,<br>Tensor<[1200, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?   | Done     | Done       | True  |
|  8 | Tensor<[320]> self = ?,<br>Tensor<[300, 320]> mat1 = ?,<br>Tensor<[320, 320]> mat2 = ?    | Done     | Done       | True  |
|  9 | Tensor<[512]> self = ?,<br>Tensor<[300, 2048]> mat1 = ?,<br>Tensor<[2048, 512]> mat2 = ?  | Done     | Done       | True  |
| 10 | Tensor<[512]> self = ?,<br>Tensor<[300, 512]> mat1 = ?,<br>Tensor<[512, 512]> mat2 = ?    | Done     | Done       | True  |
| 11 | Tensor<[512]> self = ?,<br>Tensor<[4800, 128]> mat1 = ?,<br>Tensor<[128, 512]> mat2 = ?   | Done     | Done       | True  |
| 12 | Tensor<[64]> self = ?,<br>Tensor<[19200, 256]> mat1 = ?,<br>Tensor<[256, 64]> mat2 = ?    | Done     | Done       | True  |
| 13 | Tensor<[64]> self = ?,<br>Tensor<[19200, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?      | Done     | Done       | True  |
| 14 | Tensor<[64]> self = ?,<br>Tensor<[300, 64]> mat1 = ?,<br>Tensor<[64, 64]> mat2 = ?        | Done     | Done       | True  |
### aten.arange.default
|    | ATen Input Variations                                                                                                            | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | number end = 120,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  1 | number end = 160,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  2 | number end = 240,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  3 | number end = 30,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Fallback   | True  |
|  4 | number end = 320,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  5 | number end = 40,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Fallback   | True  |
|  6 | number end = 480,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  7 | number end = 60,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Fallback   | True  |
|  8 | number end = 640,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False | None     | Fallback   | True  |
|  9 | number end = 80,<br>Optional[int] dtype = torch.float32,<br>Optional[Device] device = cpu,<br>Optional[bool] pin_memory = False  | None     | Fallback   | True  |
### aten.bmm.default
|    | ATen Input Variations                                              | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 19200, 300]> self = ?,<br>Tensor<[1, 300, 64]> mat2 = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 19200, 64]> self = ?,<br>Tensor<[1, 64, 300]> mat2 = ?  | Done     | Done       | True  |
|  2 | Tensor<[2, 4800, 300]> self = ?,<br>Tensor<[2, 300, 64]> mat2 = ?  | Done     | Done       | True  |
|  3 | Tensor<[2, 4800, 64]> self = ?,<br>Tensor<[2, 64, 300]> mat2 = ?   | Done     | Done       | True  |
|  4 | Tensor<[5, 1200, 300]> self = ?,<br>Tensor<[5, 300, 64]> mat2 = ?  | Done     | Done       | True  |
|  5 | Tensor<[5, 1200, 64]> self = ?,<br>Tensor<[5, 64, 300]> mat2 = ?   | Done     | Done       | True  |
|  6 | Tensor<[8, 300, 300]> self = ?,<br>Tensor<[8, 300, 64]> mat2 = ?   | Done     | Done       | True  |
|  7 | Tensor<[8, 300, 64]> self = ?,<br>Tensor<[8, 64, 300]> mat2 = ?    | Done     | Done       | True  |
### aten.cat.default
|    | ATen Input Variations                                                             | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | List[Tensor] tensors = [<[1, 64, 120, 160]>, <[1, 64, 120, 160]>],<br>int dim = 1 | Done     | Done       | True  |
|  1 | List[Tensor] tensors = [<[1, 64, 30, 40]>, <[1, 64, 30, 40]>],<br>int dim = 1     | Done     | Done       | True  |
|  2 | List[Tensor] tensors = [<[1, 64, 60, 80]>, <[1, 64, 60, 80]>],<br>int dim = 1     | Done     | Done       | True  |
### aten.ceil.default
|    | ATen Input Variations   | Status   | Isolated   | PCC   |
|---:|:------------------------|:---------|:-----------|:------|
|  0 | Tensor<[120]> self = ?  | None     | Fallback   | True  |
|  1 | Tensor<[160]> self = ?  | None     | Fallback   | True  |
|  2 | Tensor<[240]> self = ?  | None     | Fallback   | True  |
|  3 | Tensor<[30]> self = ?   | None     | Fallback   | True  |
|  4 | Tensor<[320]> self = ?  | None     | Fallback   | True  |
|  5 | Tensor<[40]> self = ?   | None     | Fallback   | True  |
|  6 | Tensor<[480]> self = ?  | None     | Fallback   | True  |
|  7 | Tensor<[60]> self = ?   | None     | Fallback   | True  |
|  8 | Tensor<[640]> self = ?  | None     | Fallback   | True  |
|  9 | Tensor<[80]> self = ?   | None     | Fallback   | True  |
### aten.clamp.default
|    | ATen Input Variations                                                              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[120]> self = ?,<br>Optional[number] min = 0.0                              | None     | Fallback   | True  |
|  1 | Tensor<[120]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 59  | None     | Fallback   | True  |
|  2 | Tensor<[160]> self = ?,<br>Optional[number] min = 0.0                              | None     | Fallback   | True  |
|  3 | Tensor<[160]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 79  | None     | Fallback   | True  |
|  4 | Tensor<[240]> self = ?,<br>Optional[number] min = 0.0                              | None     | Fallback   | True  |
|  5 | Tensor<[240]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 119 | None     | Fallback   | True  |
|  6 | Tensor<[30]> self = ?,<br>Optional[number] min = 0.0                               | None     | Fallback   | True  |
|  7 | Tensor<[30]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 14   | None     | Fallback   | True  |
|  8 | Tensor<[320]> self = ?,<br>Optional[number] min = 0.0                              | None     | Fallback   | True  |
|  9 | Tensor<[320]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 159 | None     | Fallback   | True  |
| 10 | Tensor<[40]> self = ?,<br>Optional[number] min = 0.0                               | None     | Fallback   | True  |
| 11 | Tensor<[40]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 19   | None     | Fallback   | True  |
| 12 | Tensor<[480]> self = ?,<br>Optional[number] min = 0.0                              | None     | Fallback   | True  |
| 13 | Tensor<[480]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 239 | None     | Fallback   | True  |
| 14 | Tensor<[60]> self = ?,<br>Optional[number] min = 0.0                               | None     | Fallback   | True  |
| 15 | Tensor<[60]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 29   | None     | Fallback   | True  |
| 16 | Tensor<[640]> self = ?,<br>Optional[number] min = 0.0                              | None     | Fallback   | True  |
| 17 | Tensor<[640]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 319 | None     | Fallback   | True  |
| 18 | Tensor<[80]> self = ?,<br>Optional[number] min = 0.0                               | None     | Fallback   | True  |
| 19 | Tensor<[80]> self = ?,<br>Optional[number] min = ?,<br>Optional[number] max = 39   | None     | Fallback   | True  |
### aten.clone.default
|    | ATen Input Variations                                                                        | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?                                                          | Done     | Done       | True  |
|  1 | Tensor<[1, 1200, 1280]> self = ?                                                             | Done     | Done       | True  |
|  2 | Tensor<[1, 1200, 320]> self = ?                                                              | Done     | Done       | True  |
|  3 | Tensor<[1, 1200, 5, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
|  4 | Tensor<[1, 128, 60, 80]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
|  5 | Tensor<[1, 19200, 256]> self = ?                                                             | Done     | Done       | True  |
|  6 | Tensor<[1, 19200, 64]> self = ?                                                              | Done     | Done       | True  |
|  7 | Tensor<[1, 2, 4800, 300]> self = ?                                                           | Done     | Done       | True  |
|  8 | Tensor<[1, 300, 2048]> self = ?                                                              | Done     | Done       | True  |
|  9 | Tensor<[1, 300, 512]> self = ?                                                               | Done     | Done       | True  |
| 10 | Tensor<[1, 300, 8, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format   | Done     | Done       | True  |
| 11 | Tensor<[1, 320, 30, 40]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
| 12 | Tensor<[1, 4800, 128]> self = ?                                                              | Done     | Done       | True  |
| 13 | Tensor<[1, 4800, 2, 64]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
| 14 | Tensor<[1, 4800, 512]> self = ?                                                              | Done     | Done       | True  |
| 15 | Tensor<[1, 5, 1200, 300]> self = ?                                                           | Done     | Done       | True  |
| 16 | Tensor<[1, 512, 15, 20]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format  | Done     | Done       | True  |
| 17 | Tensor<[1, 64, 120, 160]> self = ?,<br>Optional[int] memory_format = torch.contiguous_format | Done     | Done       | True  |
| 18 | Tensor<[1, 8, 300, 300]> self = ?                                                            | Done     | Done       | True  |
### aten.convolution.default
|    | ATen Input Variations                                                                                                                                                                                                                                                                                 | Status   | Isolated   | PCC   |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 128, 120, 160]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
|  1 | Tensor<[1, 128, 30, 40]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
|  2 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[128, 128, 4, 4]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
|  3 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[320, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
|  4 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[64, 128, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
|  5 | Tensor<[1, 128, 60, 80]> input = ?,<br>Tensor<[64, 128, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
|  6 | Tensor<[1, 1280, 30, 40]> input = ?,<br>Tensor<[1280, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[1280]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1280 | None     | Fallback   | True  |
|  7 | Tensor<[1, 2048, 15, 20]> input = ?,<br>Tensor<[2048, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[2048]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 2048 | None     | Fallback   | True  |
|  8 | Tensor<[1, 256, 120, 160]> input = ?,<br>Tensor<[256, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[256]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 256   | None     | Fallback   | True  |
|  9 | Tensor<[1, 3, 480, 640]> input = ?,<br>Tensor<[64, 3, 7, 7]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [4, 4],<br>List[int] padding = [3, 3],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Fallback   | True  |
| 10 | Tensor<[1, 32, 120, 160]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 11 | Tensor<[1, 32, 30, 40]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | True  |
| 12 | Tensor<[1, 32, 60, 80]> input = ?,<br>Tensor<[2, 32, 3, 3]> weight = ?,<br>Optional[Tensor]<[2]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1           | Done     | Done       | True  |
| 13 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[320, 320, 2, 2]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 14 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[512, 320, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 15 | Tensor<[1, 320, 30, 40]> input = ?,<br>Tensor<[64, 320, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
| 16 | Tensor<[1, 512, 15, 20]> input = ?,<br>Tensor<[64, 512, 1, 1]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
| 17 | Tensor<[1, 512, 60, 80]> input = ?,<br>Tensor<[512, 1, 3, 3]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 512     | None     | Fallback   | True  |
| 18 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[128, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>List[int] stride = [2, 2],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1     | Done     | Done       | True  |
| 19 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
| 20 | Tensor<[1, 64, 120, 160]> input = ?,<br>Tensor<[64, 64, 8, 8]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [8, 8],<br>List[int] padding = [0, 0],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | Done     | Done       | True  |
| 21 | Tensor<[1, 64, 30, 40]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
| 22 | Tensor<[1, 64, 480, 640]> input = ?,<br>Tensor<[1, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[1]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | None     | Fallback   | True  |
| 23 | Tensor<[1, 64, 480, 640]> input = ?,<br>Tensor<[64, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1       | None     | Fallback   | True  |
| 24 | Tensor<[1, 64, 60, 80]> input = ?,<br>Tensor<[32, 64, 3, 3]> weight = ?,<br>Optional[Tensor]<[32]> bias = ?,<br>List[int] stride = [1, 1],<br>List[int] padding = [1, 1],<br>List[int] dilation = [1, 1],<br>bool transposed = False,<br>List[int] output_padding = [0, 0],<br>int groups = 1         | Done     | Done       | True  |
### aten.div.Tensor
|    | ATen Input Variations                                      | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0 | Done     | Done       | True  |
|  1 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0  | Done     | Done       | True  |
|  2 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0  | Done     | Done       | True  |
|  3 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0   | Done     | Done       | True  |
### aten.expand.default
|    | ATen Input Variations                                                       | Status   | Isolated   | PCC   |
|---:|:----------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300] | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]   | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 1, 300, 64]       | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 1, 64, 300]       | Unknown  | Fallback   | True  |
|  4 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [1, 2, 300, 64]       | Unknown  | Fallback   | True  |
|  5 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]   | Unknown  | Fallback   | True  |
|  6 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]     | Unknown  | Fallback   | True  |
|  7 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [1, 2, 64, 300]       | Unknown  | Fallback   | True  |
|  8 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]   | Unknown  | Fallback   | True  |
|  9 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]     | Unknown  | Fallback   | True  |
| 10 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [1, 5, 300, 64]       | Unknown  | Fallback   | True  |
| 11 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [1, 5, 64, 300]       | Unknown  | Fallback   | True  |
| 12 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]     | Unknown  | Fallback   | True  |
| 13 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]       | Unknown  | Fallback   | True  |
| 14 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [1, 8, 64, 300]       | Unknown  | Fallback   | True  |
### aten.gelu.default
|    | ATen Input Variations            | Status   | Isolated   | PCC   |
|---:|:---------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1200, 1280]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 19200, 256]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 300, 2048]> self = ?  | Done     | Done       | True  |
|  3 | Tensor<[1, 4800, 512]> self = ?  | Done     | Done       | True  |
### aten.mul.Tensor
|    | ATen Input Variations                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                   | Done     | Done       | True  |
|  1 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ? | None     | Fallback   | True  |
|  2 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?         | Done     | Done       | True  |
|  3 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?            | Done     | Done       | True  |
|  4 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?         | Done     | Done       | True  |
|  5 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?            | Done     | Done       | True  |
|  6 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?     | None     | Fallback   | True  |
|  7 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?            | Done     | Done       | True  |
|  8 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?               | Done     | Done       | True  |
|  9 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?         | Done     | Done       | True  |
| 10 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?            | Done     | Done       | True  |
| 11 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?     | None     | Fallback   | True  |
| 12 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?            | Done     | Done       | True  |
| 13 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?               | Done     | Done       | True  |
| 14 | Tensor<[120]> self = ?,<br>Tensor other = 0.5                             | Done     | Done       | True  |
| 15 | Tensor<[160]> self = ?,<br>Tensor other = 0.5                             | Done     | Done       | True  |
| 16 | Tensor<[240]> self = ?,<br>Tensor other = 0.5                             | Done     | Done       | True  |
| 17 | Tensor<[30]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | True  |
| 18 | Tensor<[320]> self = ?,<br>Tensor other = 0.5                             | Done     | Done       | True  |
| 19 | Tensor<[40]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | True  |
| 20 | Tensor<[480]> self = ?,<br>Tensor other = 0.5                             | Done     | Done       | True  |
| 21 | Tensor<[60]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | True  |
| 22 | Tensor<[640]> self = ?,<br>Tensor other = 0.5                             | Done     | Done       | True  |
| 23 | Tensor<[80]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | True  |
### aten.native_layer_norm.default
|    | ATen Input Variations                                                                                                                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1200, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |
|  1 | Tensor<[1, 19200, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05    | Done     | Done       | N/A   |
|  2 | Tensor<[1, 300, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | N/A   |
|  3 | Tensor<[1, 300, 320]> input = ?,<br>List[int] normalized_shape = [320],<br>Optional[Tensor]<[320]> weight = ?,<br>Optional[Tensor]<[320]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | N/A   |
|  4 | Tensor<[1, 300, 512]> input = ?,<br>List[int] normalized_shape = [512],<br>Optional[Tensor]<[512]> weight = ?,<br>Optional[Tensor]<[512]> bias = ?,<br>float eps = 1e-05  | Done     | Done       | N/A   |
|  5 | Tensor<[1, 300, 64]> input = ?,<br>List[int] normalized_shape = [64],<br>Optional[Tensor]<[64]> weight = ?,<br>Optional[Tensor]<[64]> bias = ?,<br>float eps = 1e-05      | Done     | Done       | N/A   |
|  6 | Tensor<[1, 4800, 128]> input = ?,<br>List[int] normalized_shape = [128],<br>Optional[Tensor]<[128]> weight = ?,<br>Optional[Tensor]<[128]> bias = ?,<br>float eps = 1e-05 | Done     | Done       | N/A   |
### aten.permute.default
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Unknown    | N/A   |
|  1 | Tensor<[1, 120, 160, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2] | Done     | Unknown    | N/A   |
|  2 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Unknown    | N/A   |
|  3 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Unknown    | N/A   |
|  4 | Tensor<[1, 128, 300]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Unknown    | N/A   |
|  5 | Tensor<[1, 15, 20, 512]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Unknown    | N/A   |
|  6 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3] | Done     | Done       | True  |
|  7 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Done       | True  |
|  8 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Unknown    | N/A   |
|  9 | Tensor<[1, 30, 40, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Unknown    | N/A   |
| 10 | Tensor<[1, 300, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Done       | True  |
| 11 | Tensor<[1, 300, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Unknown    | N/A   |
| 12 | Tensor<[1, 300, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Unknown    | N/A   |
| 13 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Unknown    | N/A   |
| 14 | Tensor<[1, 320, 300]> self = ?,<br>List[int] dims = [0, 2, 1]        | Done     | Unknown    | N/A   |
| 15 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] dims = [0, 2, 1]       | Done     | Unknown    | N/A   |
| 16 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Unknown    | N/A   |
| 17 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]  | Done     | Unknown    | N/A   |
| 18 | Tensor<[1, 60, 80, 128]> self = ?,<br>List[int] dims = [0, 3, 1, 2]  | Done     | Unknown    | N/A   |
| 19 | Tensor<[1, 64, 300]> self = ?,<br>List[int] dims = [0, 2, 1]         | Done     | Done       | True  |
| 20 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]   | Done     | Unknown    | N/A   |
### aten.relu.default
|    | ATen Input Variations              | Status   | Isolated   | PCC   |
|---:|:-----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 32, 120, 160]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 32, 30, 40]> self = ?   | Done     | Done       | True  |
|  2 | Tensor<[1, 32, 60, 80]> self = ?   | Done     | Done       | True  |
|  3 | Tensor<[1, 64, 120, 160]> self = ? | Done     | Done       | True  |
|  4 | Tensor<[1, 64, 30, 40]> self = ?   | Done     | Done       | True  |
|  5 | Tensor<[1, 64, 480, 640]> self = ? | Done     | Done       | True  |
|  6 | Tensor<[1, 64, 60, 80]> self = ?   | Done     | Done       | True  |
### aten.rsub.Scalar
|    | ATen Input Variations                            | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[120, 1]> self = ?,<br>number other = 1.0 | Done     | Done       | True  |
|  1 | Tensor<[160]> self = ?,<br>number other = 1.0    | Done     | Done       | True  |
|  2 | Tensor<[240, 1]> self = ?,<br>number other = 1.0 | Done     | Done       | True  |
|  3 | Tensor<[30, 1]> self = ?,<br>number other = 1.0  | Done     | Done       | True  |
|  4 | Tensor<[320]> self = ?,<br>number other = 1.0    | Done     | Done       | True  |
|  5 | Tensor<[40]> self = ?,<br>number other = 1.0     | Done     | Done       | True  |
|  6 | Tensor<[480, 1]> self = ?,<br>number other = 1.0 | Done     | Done       | True  |
|  7 | Tensor<[60, 1]> self = ?,<br>number other = 1.0  | Done     | Done       | True  |
|  8 | Tensor<[640]> self = ?,<br>number other = 1.0    | Done     | Done       | True  |
|  9 | Tensor<[80]> self = ?,<br>number other = 1.0     | Done     | Done       | True  |
### aten.select.int
|    | ATen Input Variations                                               | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 0 | Done     | Done       | True  |
|  1 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 1 | Done     | Done       | True  |
|  2 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Done       | True  |
|  3 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Done       | True  |
|  4 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Done       | True  |
|  5 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Done       | True  |
### aten.sigmoid.default
|    | ATen Input Variations             | Status   | Isolated   | PCC   |
|---:|:----------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 480, 640]> self = ? | Done     | Done       | True  |
|  1 | Tensor<[1, 2, 120, 160]> self = ? | Done     | Done       | True  |
|  2 | Tensor<[1, 2, 30, 40]> self = ?   | Done     | Done       | True  |
|  3 | Tensor<[1, 2, 60, 80]> self = ?   | Done     | Done       | True  |
### aten.slice.Tensor
|    | ATen Input Variations                                                                                                     | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Fallback   | True  |
|  1 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807    | Unknown  | Fallback   | True  |
|  2 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807 | Unknown  | Fallback   | True  |
|  3 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Fallback   | True  |
|  4 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 0,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807   | Unknown  | Fallback   | True  |
|  5 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Fallback   | True  |
|  6 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Fallback   | True  |
|  7 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Fallback   | True  |
|  8 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 2,<br>Optional[int] start = 0,<br>Optional[int] end = 9223372036854775807      | Unknown  | Fallback   | True  |
### aten.squeeze.dim
|    | ATen Input Variations                             | Status   | Isolated   | PCC   |
|---:|:--------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 480, 640]> self = ?,<br>int dim = 1 | Done     | Done       | True  |
### aten.sub.Tensor
|    | ATen Input Variations                                    | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[120, 1]> self = ?,<br>Tensor<[120, 1]> other = ? | Done     | Done       | True  |
|  1 | Tensor<[120]> self = ?,<br>Tensor other = 0.5            | Done     | Done       | True  |
|  2 | Tensor<[160]> self = ?,<br>Tensor other = 0.5            | Done     | Done       | True  |
|  3 | Tensor<[160]> self = ?,<br>Tensor<[160]> other = ?       | Done     | Done       | True  |
|  4 | Tensor<[240, 1]> self = ?,<br>Tensor<[240, 1]> other = ? | Done     | Done       | True  |
|  5 | Tensor<[240]> self = ?,<br>Tensor other = 0.5            | Done     | Done       | True  |
|  6 | Tensor<[30, 1]> self = ?,<br>Tensor<[30, 1]> other = ?   | Done     | Done       | True  |
|  7 | Tensor<[30]> self = ?,<br>Tensor other = 0.5             | Done     | Done       | True  |
|  8 | Tensor<[320]> self = ?,<br>Tensor other = 0.5            | None     | Fallback   | True  |
|  9 | Tensor<[320]> self = ?,<br>Tensor<[320]> other = ?       | Done     | Done       | True  |
| 10 | Tensor<[40]> self = ?,<br>Tensor other = 0.5             | Done     | Done       | True  |
| 11 | Tensor<[40]> self = ?,<br>Tensor<[40]> other = ?         | Done     | Done       | True  |
| 12 | Tensor<[480, 1]> self = ?,<br>Tensor<[480, 1]> other = ? | Done     | Done       | True  |
| 13 | Tensor<[480]> self = ?,<br>Tensor other = 0.5            | Done     | Done       | True  |
| 14 | Tensor<[60, 1]> self = ?,<br>Tensor<[60, 1]> other = ?   | Done     | Done       | True  |
| 15 | Tensor<[60]> self = ?,<br>Tensor other = 0.5             | Done     | Done       | True  |
| 16 | Tensor<[640]> self = ?,<br>Tensor other = 0.5            | Done     | Done       | True  |
| 17 | Tensor<[640]> self = ?,<br>Tensor<[640]> other = ?       | Done     | Done       | True  |
| 18 | Tensor<[80]> self = ?,<br>Tensor other = 0.5             | Done     | Done       | True  |
| 19 | Tensor<[80]> self = ?,<br>Tensor<[80]> other = ?         | Done     | Done       | True  |
### aten.t.default
|    | ATen Input Variations        | Status   | Isolated   | PCC   |
|---:|:-----------------------------|:---------|:-----------|:------|
|  0 | Tensor<[128, 128]> self = ?  | Done     | Done       | True  |
|  1 | Tensor<[128, 512]> self = ?  | Done     | Done       | True  |
|  2 | Tensor<[1280, 320]> self = ? | Done     | Done       | True  |
|  3 | Tensor<[2048, 512]> self = ? | Done     | Done       | True  |
|  4 | Tensor<[256, 64]> self = ?   | Done     | Done       | True  |
|  5 | Tensor<[320, 1280]> self = ? | Done     | Done       | True  |
|  6 | Tensor<[320, 320]> self = ?  | Done     | Done       | True  |
|  7 | Tensor<[512, 128]> self = ?  | Done     | Done       | True  |
|  8 | Tensor<[512, 2048]> self = ? | Done     | Done       | True  |
|  9 | Tensor<[512, 512]> self = ?  | Done     | Done       | True  |
| 10 | Tensor<[64, 256]> self = ?   | Done     | Done       | True  |
| 11 | Tensor<[64, 64]> self = ?    | Done     | Done       | True  |
### aten.transpose.int
|    | ATen Input Variations                                                | Status   | Isolated   | PCC   |
|---:|:---------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
|  1 | Tensor<[1, 1200, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  2 | Tensor<[1, 128, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
|  3 | Tensor<[1, 1280, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  4 | Tensor<[1, 19200, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  5 | Tensor<[1, 2, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
|  6 | Tensor<[1, 2048, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
|  7 | Tensor<[1, 256, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2   | Done     | Done       | True  |
|  8 | Tensor<[1, 300, 2048]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
|  9 | Tensor<[1, 320, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
| 10 | Tensor<[1, 4800, 512]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
| 11 | Tensor<[1, 5, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
| 12 | Tensor<[1, 512, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2     | Done     | Done       | True  |
| 13 | Tensor<[1, 512, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
| 14 | Tensor<[1, 64, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2    | Done     | Done       | True  |
| 15 | Tensor<[1, 8, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Done     | Done       | True  |
### aten.unsqueeze.default
|    | ATen Input Variations                          | Status   | Isolated   | PCC   |
|---:|:-----------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1 | Done     | Done       | True  |
|  1 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1   | Done     | Done       | True  |
|  2 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1   | Done     | Done       | True  |
|  3 | Tensor<[120]> self = ?,<br>int dim = 1         | Done     | Done       | True  |
|  4 | Tensor<[240]> self = ?,<br>int dim = 1         | None     | Fallback   | True  |
|  5 | Tensor<[30]> self = ?,<br>int dim = 1          | Done     | Done       | True  |
|  6 | Tensor<[480]> self = ?,<br>int dim = 1         | Done     | Done       | True  |
|  7 | Tensor<[60]> self = ?,<br>int dim = 1          | Done     | Done       | True  |
### aten.view.default
|    | ATen Input Variations                                                    | Status   | Isolated   | PCC   |
|---:|:-------------------------------------------------------------------------|:---------|:-----------|:------|
|  0 | Tensor<[1, 1, 19200, 300]> self = ?,<br>List[int] size = [1, 19200, 300] | Done     | Done       | True  |
|  1 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]   | Done     | Done       | True  |
|  2 | Tensor<[1, 1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 64]       | Done     | Done       | True  |
|  3 | Tensor<[1, 1, 64, 300]> self = ?,<br>List[int] size = [1, 64, 300]       | Done     | Done       | True  |
|  4 | Tensor<[1, 1200, 1280]> self = ?,<br>List[int] size = [1200, 1280]       | Done     | Done       | True  |
|  5 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 1200, 5, 64]    | Done     | Done       | True  |
|  6 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1, 30, 40, -1]     | Done     | Done       | True  |
|  7 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] size = [1200, 320]         | Done     | Done       | True  |
|  8 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] size = [1, 1200, 320]    | Done     | Done       | True  |
|  9 | Tensor<[1, 128, 15, 20]> self = ?,<br>List[int] size = [1, 128, 300]     | Done     | Done       | True  |
| 10 | Tensor<[1, 128, 4800]> self = ?,<br>List[int] size = [1, 128, 60, 80]    | Done     | Done       | True  |
| 11 | Tensor<[1, 128, 60, 80]> self = ?,<br>List[int] size = [1, 128, 4800]    | Done     | Done       | True  |
| 12 | Tensor<[1, 1280, 1200]> self = ?,<br>List[int] size = [1, 1280, 30, 40]  | Done     | Done       | True  |
| 13 | Tensor<[1, 1280, 30, 40]> self = ?,<br>List[int] size = [1, 1280, 1200]  | Done     | Done       | True  |
| 14 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] size = [1, 19200, 64]   | Done     | Done       | True  |
| 15 | Tensor<[1, 19200, 256]> self = ?,<br>List[int] size = [19200, 256]       | Done     | Done       | True  |
| 16 | Tensor<[1, 19200, 300]> self = ?,<br>List[int] size = [1, 1, 19200, 300] | Done     | Done       | True  |
| 17 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 1, 19200, 64]   | Done     | Done       | True  |
| 18 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 120, 160, -1]   | Done     | Done       | True  |
| 19 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [1, 19200, 1, 64]   | Done     | Done       | True  |
| 20 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] size = [19200, 64]         | Done     | Done       | True  |
| 21 | Tensor<[1, 2, 300, 64]> self = ?,<br>List[int] size = [2, 300, 64]       | Done     | Done       | True  |
| 22 | Tensor<[1, 2, 4800, 300]> self = ?,<br>List[int] size = [2, 4800, 300]   | Done     | Done       | True  |
| 23 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] size = [2, 4800, 64]     | Done     | Done       | True  |
| 24 | Tensor<[1, 2, 64, 300]> self = ?,<br>List[int] size = [2, 64, 300]       | Done     | Done       | True  |
| 25 | Tensor<[1, 2048, 15, 20]> self = ?,<br>List[int] size = [1, 2048, 300]   | Done     | Done       | True  |
| 26 | Tensor<[1, 2048, 300]> self = ?,<br>List[int] size = [1, 2048, 15, 20]   | Done     | Done       | True  |
| 27 | Tensor<[1, 256, 120, 160]> self = ?,<br>List[int] size = [1, 256, 19200] | Done     | Done       | True  |
| 28 | Tensor<[1, 256, 19200]> self = ?,<br>List[int] size = [1, 256, 120, 160] | Done     | Done       | True  |
| 29 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [1, 300, 2, 64]      | Done     | Done       | True  |
| 30 | Tensor<[1, 300, 128]> self = ?,<br>List[int] size = [300, 128]           | Done     | Done       | True  |
| 31 | Tensor<[1, 300, 2048]> self = ?,<br>List[int] size = [300, 2048]         | Done     | Done       | True  |
| 32 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [1, 300, 5, 64]      | Done     | Done       | True  |
| 33 | Tensor<[1, 300, 320]> self = ?,<br>List[int] size = [300, 320]           | Done     | Done       | True  |
| 34 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 15, 20, -1]      | Done     | Done       | True  |
| 35 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [1, 300, 8, 64]      | Done     | Done       | True  |
| 36 | Tensor<[1, 300, 512]> self = ?,<br>List[int] size = [300, 512]           | Done     | Done       | True  |
| 37 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [1, 300, 1, 64]       | Done     | Done       | True  |
| 38 | Tensor<[1, 300, 64]> self = ?,<br>List[int] size = [300, 64]             | Done     | Done       | True  |
| 39 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] size = [1, 300, 512]      | Done     | Done       | True  |
| 40 | Tensor<[1, 320, 1200]> self = ?,<br>List[int] size = [1, 320, 30, 40]    | Done     | Done       | True  |
| 41 | Tensor<[1, 320, 15, 20]> self = ?,<br>List[int] size = [1, 320, 300]     | Done     | Done       | True  |
| 42 | Tensor<[1, 320, 30, 40]> self = ?,<br>List[int] size = [1, 320, 1200]    | Done     | Done       | True  |
| 43 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 4800, 2, 64]    | Done     | Done       | True  |
| 44 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [1, 60, 80, -1]     | Done     | Done       | True  |
| 45 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] size = [4800, 128]         | Done     | Done       | True  |
| 46 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] size = [1, 4800, 128]    | Done     | Done       | True  |
| 47 | Tensor<[1, 4800, 512]> self = ?,<br>List[int] size = [4800, 512]         | Done     | Done       | True  |
| 48 | Tensor<[1, 5, 1200, 300]> self = ?,<br>List[int] size = [5, 1200, 300]   | Done     | Done       | True  |
| 49 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] size = [5, 1200, 64]     | Done     | Done       | True  |
| 50 | Tensor<[1, 5, 300, 64]> self = ?,<br>List[int] size = [5, 300, 64]       | Done     | Done       | True  |
| 51 | Tensor<[1, 5, 64, 300]> self = ?,<br>List[int] size = [5, 64, 300]       | Done     | Done       | True  |
| 52 | Tensor<[1, 512, 15, 20]> self = ?,<br>List[int] size = [1, 512, 300]     | Done     | Done       | True  |
| 53 | Tensor<[1, 512, 4800]> self = ?,<br>List[int] size = [1, 512, 60, 80]    | Done     | Done       | True  |
| 54 | Tensor<[1, 512, 60, 80]> self = ?,<br>List[int] size = [1, 512, 4800]    | Done     | Done       | True  |
| 55 | Tensor<[1, 64, 120, 160]> self = ?,<br>List[int] size = [1, 64, 19200]   | Done     | Done       | True  |
| 56 | Tensor<[1, 64, 15, 20]> self = ?,<br>List[int] size = [1, 64, 300]       | Done     | Done       | True  |
| 57 | Tensor<[1, 64, 19200]> self = ?,<br>List[int] size = [1, 64, 120, 160]   | Done     | Done       | True  |
| 58 | Tensor<[1, 8, 300, 300]> self = ?,<br>List[int] size = [8, 300, 300]     | Done     | Done       | True  |
| 59 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] size = [8, 300, 64]       | Done     | Done       | True  |
| 60 | Tensor<[1, 8, 64, 300]> self = ?,<br>List[int] size = [8, 64, 300]       | Done     | Done       | True  |
| 61 | Tensor<[1200, 1280]> self = ?,<br>List[int] size = [1, 1200, 1280]       | Done     | Done       | True  |
| 62 | Tensor<[1200, 320]> self = ?,<br>List[int] size = [1, 1200, 320]         | Done     | Done       | True  |
| 63 | Tensor<[19200, 256]> self = ?,<br>List[int] size = [1, 19200, 256]       | Done     | Done       | True  |
| 64 | Tensor<[19200, 64]> self = ?,<br>List[int] size = [1, 19200, 64]         | Done     | Done       | True  |
| 65 | Tensor<[2, 4800, 300]> self = ?,<br>List[int] size = [1, 2, 4800, 300]   | Done     | Done       | True  |
| 66 | Tensor<[2, 4800, 64]> self = ?,<br>List[int] size = [1, 2, 4800, 64]     | Done     | Done       | True  |
| 67 | Tensor<[300, 128]> self = ?,<br>List[int] size = [1, 300, 128]           | Done     | Done       | True  |
| 68 | Tensor<[300, 2048]> self = ?,<br>List[int] size = [1, 300, 2048]         | Done     | Done       | True  |
| 69 | Tensor<[300, 320]> self = ?,<br>List[int] size = [1, 300, 320]           | Done     | Done       | True  |
| 70 | Tensor<[300, 512]> self = ?,<br>List[int] size = [1, 300, 512]           | Done     | Done       | True  |
| 71 | Tensor<[300, 64]> self = ?,<br>List[int] size = [1, 300, 64]             | Done     | Done       | True  |
| 72 | Tensor<[4800, 128]> self = ?,<br>List[int] size = [1, 4800, 128]         | Done     | Done       | True  |
| 73 | Tensor<[4800, 512]> self = ?,<br>List[int] size = [1, 4800, 512]         | Done     | Done       | True  |
| 74 | Tensor<[5, 1200, 300]> self = ?,<br>List[int] size = [1, 5, 1200, 300]   | Done     | Done       | True  |
| 75 | Tensor<[5, 1200, 64]> self = ?,<br>List[int] size = [1, 5, 1200, 64]     | Done     | Done       | True  |
| 76 | Tensor<[8, 300, 300]> self = ?,<br>List[int] size = [1, 8, 300, 300]     | Done     | Done       | True  |
| 77 | Tensor<[8, 300, 64]> self = ?,<br>List[int] size = [1, 8, 300, 64]       | Done     | Done       | True  |

