### aten.unsqueeze.default
|     | ATen Input Variations                                 | Status   | Isolated   | PCC   |
|----:|:------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[0]> self = ?,<br>int dim = 1                  | Unknown  | Fallback   | True  |
|   1 | Tensor<[1, 1, 1, 16]> self = ?,<br>int dim = 4        | Unknown  | Done       | True  |
|   2 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2           | Done     | Done       | True  |
|   3 | Tensor<[1, 1, 12]> self = ?,<br>int dim = 2           | Done     | Done       | True  |
|   4 | Tensor<[1, 1, 14]> self = ?,<br>int dim = 2           | Done     | Done       | True  |
|   5 | Tensor<[1, 1, 15]> self = ?,<br>int dim = 2           | Done     | Done       | True  |
|   6 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 2           | Unknown  | Done       | True  |
|   7 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 1           | Unknown  | Done       | True  |
|   8 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 2           | Unknown  | Done       | True  |
|   9 | Tensor<[1, 1, 19]> self = ?,<br>int dim = 2           | Done     | Done       | True  |
|  10 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 1            | Done     | Done       | True  |
|  11 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2            | Done     | Done       | True  |
|  12 | Tensor<[1, 1, 2048]> self = ?,<br>int dim = 2         | Done     | Done       | True  |
|  13 | Tensor<[1, 1, 24]> self = ?,<br>int dim = 2           | Done     | Done       | True  |
|  14 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 2          | Done     | Done       | True  |
|  15 | Tensor<[1, 1, 25]> self = ?,<br>int dim = 2           | Done     | Done       | True  |
|  16 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 1            | Unknown  | Done       | True  |
|  17 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 2            | Unknown  | Done       | True  |
|  18 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2           | Done     | Done       | True  |
|  19 | Tensor<[1, 1, 45]> self = ?,<br>int dim = 2           | Unknown  | Done       | True  |
|  20 | Tensor<[1, 1, 46]> self = ?,<br>int dim = 2           | Unknown  | Done       | True  |
|  21 | Tensor<[1, 1, 59]> self = ?,<br>int dim = 2           | Done     | Done       | True  |
|  22 | Tensor<[1, 1, 5]> self = ?,<br>int dim = 2            | Unknown  | Done       | True  |
|  23 | Tensor<[1, 1, 60]> self = ?,<br>int dim = 2           | Unknown  | Done       | True  |
|  24 | Tensor<[1, 1, 6]> self = ?,<br>int dim = 2            | Unknown  | Done       | True  |
|  25 | Tensor<[1, 1, 7]> self = ?,<br>int dim = 2            | Done     | Done       | True  |
|  26 | Tensor<[1, 1, 8]> self = ?,<br>int dim = 2            | Done     | Done       | True  |
|  27 | Tensor<[1, 1, 9]> self = ?,<br>int dim = 2            | Done     | Done       | True  |
|  28 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 1       | Unknown  | Unknown    | N/A   |
|  29 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 2       | Unknown  | Unknown    | N/A   |
|  30 | Tensor<[1, 1, s10 + 1]> self = ?,<br>int dim = 2      | Unknown  | Unknown    | N/A   |
|  31 | Tensor<[1, 1024]> self = ?,<br>int dim = 1            | Done     | Done       | True  |
|  32 | Tensor<[1, 10]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
|  33 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1        | Done     | Done       | True  |
|  34 | Tensor<[1, 1280, 1]> self = ?,<br>int dim = 3         | Unknown  | Done       | True  |
|  35 | Tensor<[1, 1280]> self = ?,<br>int dim = 2            | Unknown  | Done       | True  |
|  36 | Tensor<[1, 12]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
|  37 | Tensor<[1, 14]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
|  38 | Tensor<[1, 15]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
|  39 | Tensor<[1, 17]> self = ?,<br>int dim = 1              | Unknown  | Done       | True  |
|  40 | Tensor<[1, 19, 19]> self = ?,<br>int dim = 1          | Done     | Done       | True  |
|  41 | Tensor<[1, 192]> self = ?,<br>int dim = 1             | Done     | Done       | True  |
|  42 | Tensor<[1, 19]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
|  43 | Tensor<[1, 1]> self = ?,<br>int dim = 1               | Done     | Done       | True  |
|  44 | Tensor<[1, 1]> self = ?,<br>int dim = 2               | Done     | Done       | True  |
|  45 | Tensor<[1, 2048, 2048]> self = ?,<br>int dim = 1      | Done     | Done       | True  |
|  46 | Tensor<[1, 2048]> self = ?,<br>int dim = 1            | Done     | Done       | True  |
|  47 | Tensor<[1, 224, 224]> self = ?,<br>int dim = 1        | Done     | Done       | True  |
|  48 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 3          | Done     | Done       | True  |
|  49 | Tensor<[1, 24]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
|  50 | Tensor<[1, 256]> self = ?,<br>int dim = 1             | Done     | Done       | True  |
|  51 | Tensor<[1, 25]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
|  52 | Tensor<[1, 2]> self = ?,<br>int dim = 1               | Unknown  | Done       | True  |
|  53 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1          | Done     | Done       | True  |
|  54 | Tensor<[1, 32, 32]> self = ?,<br>int dim = 1          | Done     | Done       | True  |
|  55 | Tensor<[1, 320, 1]> self = ?,<br>int dim = 3          | Unknown  | Done       | True  |
|  56 | Tensor<[1, 320]> self = ?,<br>int dim = 2             | Unknown  | Done       | True  |
|  57 | Tensor<[1, 32]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
|  58 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 1        | Done     | Done       | True  |
|  59 | Tensor<[1, 45, 45]> self = ?,<br>int dim = 1          | Done     | Done       | True  |
|  60 | Tensor<[1, 45]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
|  61 | Tensor<[1, 46]> self = ?,<br>int dim = 1              | Unknown  | Done       | True  |
|  62 | Tensor<[1, 5, 1, 16]> self = ?,<br>int dim = 4        | Unknown  | Done       | True  |
|  63 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 2           | Unknown  | Done       | True  |
|  64 | Tensor<[1, 512]> self = ?,<br>int dim = 2             | Done     | Done       | True  |
|  65 | Tensor<[1, 59, 59]> self = ?,<br>int dim = 1          | Done     | Done       | True  |
|  66 | Tensor<[1, 59]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
|  67 | Tensor<[1, 5]> self = ?,<br>int dim = 1               | Unknown  | Done       | True  |
|  68 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1          | Done     | Done       | True  |
|  69 | Tensor<[1, 60]> self = ?,<br>int dim = 1              | Unknown  | Done       | True  |
|  70 | Tensor<[1, 640, 1]> self = ?,<br>int dim = 3          | Unknown  | Done       | True  |
|  71 | Tensor<[1, 640]> self = ?,<br>int dim = 2             | Unknown  | Done       | True  |
|  72 | Tensor<[1, 64]> self = ?,<br>int dim = 2              | Done     | Done       | True  |
|  73 | Tensor<[1, 6]> self = ?,<br>int dim = 1               | Unknown  | Done       | True  |
|  74 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1           | Done     | Done       | True  |
|  75 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1            | Done     | Done       | True  |
|  76 | Tensor<[1, 720, 1280]> self = ?,<br>int dim = 0       | Done     | Done       | True  |
|  77 | Tensor<[1, 768]> self = ?,<br>int dim = 1             | Done     | Done       | True  |
|  78 | Tensor<[1, 7]> self = ?,<br>int dim = 1               | Done     | Done       | True  |
|  79 | Tensor<[1, 8]> self = ?,<br>int dim = 1               | Done     | Done       | True  |
|  80 | Tensor<[1, 9]> self = ?,<br>int dim = 1               | Done     | Done       | True  |
|  81 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1          | Unknown  | Unknown    | N/A   |
|  82 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1         | Unknown  | Unknown    | N/A   |
|  83 | Tensor<[100, 256]> self = ?,<br>int dim = 1           | Done     | Done       | True  |
|  84 | Tensor<[100]> self = ?,<br>int dim = -1               | Done     | Done       | True  |
|  85 | Tensor<[10]> self = ?,<br>int dim = 0                 | Done     | Done       | True  |
|  86 | Tensor<[10]> self = ?,<br>int dim = 1                 | Done     | Done       | True  |
|  87 | Tensor<[12, 1, 1]> self = ?,<br>int dim = 0           | Done     | Done       | True  |
|  88 | Tensor<[12, 10, 10]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
|  89 | Tensor<[12, 197, 197]> self = ?,<br>int dim = 0       | Done     | Done       | True  |
|  90 | Tensor<[12, 2, 2]> self = ?,<br>int dim = 0           | Unknown  | Done       | True  |
|  91 | Tensor<[12, 49, 49]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
|  92 | Tensor<[12, 64, 64]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
|  93 | Tensor<[12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   |
|  94 | Tensor<[120]> self = ?,<br>int dim = 1                | Done     | Done       | True  |
|  95 | Tensor<[128]> self = ?,<br>int dim = 1                | Done     | Done       | True  |
|  96 | Tensor<[12]> self = ?,<br>int dim = -1                | Done     | Done       | True  |
|  97 | Tensor<[1370, 1, 3, 1280]> self = ?,<br>int dim = 0   | Done     | Done       | True  |
|  98 | Tensor<[14]> self = ?,<br>int dim = -1                | Done     | Done       | True  |
|  99 | Tensor<[15]> self = ?,<br>int dim = 0                 | Done     | Done       | True  |
| 100 | Tensor<[15]> self = ?,<br>int dim = 1                 | Done     | Done       | True  |
| 101 | Tensor<[16, 1, 1]> self = ?,<br>int dim = 0           | Done     | Done       | True  |
| 102 | Tensor<[16, 1, 49, 49]> self = ?,<br>int dim = 0      | Done     | Done       | True  |
| 103 | Tensor<[16, 1, 64, 64]> self = ?,<br>int dim = 0      | Done     | Done       | True  |
| 104 | Tensor<[16, 10, 10]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
| 105 | Tensor<[16, 197, 197]> self = ?,<br>int dim = 0       | Done     | Done       | True  |
| 106 | Tensor<[16, 2, 2]> self = ?,<br>int dim = 0           | Unknown  | Done       | True  |
| 107 | Tensor<[16, 49, 49]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
| 108 | Tensor<[16, 49, 49]> self = ?,<br>int dim = 1         | Done     | Done       | True  |
| 109 | Tensor<[16, 49]> self = ?,<br>int dim = 1             | Done     | Done       | True  |
| 110 | Tensor<[16, 49]> self = ?,<br>int dim = 2             | Done     | Done       | True  |
| 111 | Tensor<[16, 64, 64]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
| 112 | Tensor<[16, 64, 64]> self = ?,<br>int dim = 1         | Done     | Done       | True  |
| 113 | Tensor<[16, 64]> self = ?,<br>int dim = 1             | Done     | Done       | True  |
| 114 | Tensor<[16, 64]> self = ?,<br>int dim = 2             | Done     | Done       | True  |
| 115 | Tensor<[16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   |
| 116 | Tensor<[160]> self = ?,<br>int dim = 0                | Unknown  | Done       | True  |
| 117 | Tensor<[16]> self = ?,<br>int dim = -1                | Unknown  | Done       | True  |
| 118 | Tensor<[16]> self = ?,<br>int dim = 1                 | Removed  | Done       | True  |
| 119 | Tensor<[17]> self = ?,<br>int dim = 0                 | Unknown  | Done       | True  |
| 120 | Tensor<[17]> self = ?,<br>int dim = 1                 | Unknown  | Done       | True  |
| 121 | Tensor<[19, 19]> self = ?,<br>int dim = 0             | Done     | Done       | True  |
| 122 | Tensor<[197, 1, 3, 1024]> self = ?,<br>int dim = 0    | Done     | Done       | True  |
| 123 | Tensor<[197, 1, 3, 768]> self = ?,<br>int dim = 0     | Done     | Done       | True  |
| 124 | Tensor<[19]> self = ?,<br>int dim = 0                 | Done     | Done       | True  |
| 125 | Tensor<[1]> self = ?,<br>int dim = 0                  | Done     | Done       | True  |
| 126 | Tensor<[1]> self = ?,<br>int dim = 1                  | Done     | Done       | True  |
| 127 | Tensor<[2, 1, 7]> self = ?,<br>int dim = 2            | Done     | Done       | True  |
| 128 | Tensor<[2, 7]> self = ?,<br>int dim = 1               | Done     | Done       | True  |
| 129 | Tensor<[2048, 2048]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
| 130 | Tensor<[23]> self = ?,<br>int dim = -1                | Done     | Done       | True  |
| 131 | Tensor<[24, 49, 49]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
| 132 | Tensor<[24, 64, 64]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
| 133 | Tensor<[240]> self = ?,<br>int dim = 1                | None     | Fallback   | True  |
| 134 | Tensor<[24]> self = ?,<br>int dim = 0                 | Removed  | Done       | True  |
| 135 | Tensor<[24]> self = ?,<br>int dim = 1                 | Done     | Done       | True  |
| 136 | Tensor<[25]> self = ?,<br>int dim = 1                 | Unknown  | Done       | True  |
| 137 | Tensor<[28]> self = ?,<br>int dim = -1                | Done     | Done       | True  |
| 138 | Tensor<[2]> self = ?,<br>int dim = 0                  | Unknown  | Done       | True  |
| 139 | Tensor<[2]> self = ?,<br>int dim = 1                  | Unknown  | Done       | True  |
| 140 | Tensor<[3, 1]> self = ?,<br>int dim = 2               | Done     | Done       | True  |
| 141 | Tensor<[3, 320, 320]> self = ?,<br>int dim = 0        | Done     | Done       | True  |
| 142 | Tensor<[3, 480, 640]> self = ?,<br>int dim = 0        | Done     | Done       | True  |
| 143 | Tensor<[3, 49, 49]> self = ?,<br>int dim = 0          | Done     | Done       | True  |
| 144 | Tensor<[3, 64, 64]> self = ?,<br>int dim = 0          | Done     | Done       | True  |
| 145 | Tensor<[300]> self = ?,<br>int dim = 1                | None     | Fallback   | True  |
| 146 | Tensor<[30]> self = ?,<br>int dim = 1                 | Done     | Done       | True  |
| 147 | Tensor<[32, 32]> self = ?,<br>int dim = 0             | Done     | Done       | True  |
| 148 | Tensor<[32, 49, 49]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
| 149 | Tensor<[32, 64, 64]> self = ?,<br>int dim = 0         | Done     | Done       | True  |
| 150 | Tensor<[320]> self = ?,<br>int dim = 1                | None     | Fallback   | True  |
| 151 | Tensor<[3234]> self = ?,<br>int dim = 1               | Unknown  | Done       | True  |
| 152 | Tensor<[32]> self = ?,<br>int dim = -1                | Done     | Done       | True  |
| 153 | Tensor<[32]> self = ?,<br>int dim = 0                 | Removed  | Done       | True  |
| 154 | Tensor<[3]> self = ?,<br>int dim = 1                  | Done     | Done       | True  |
| 155 | Tensor<[4, 1, 49, 49]> self = ?,<br>int dim = 0       | Done     | Done       | True  |
| 156 | Tensor<[4, 1, 64, 64]> self = ?,<br>int dim = 0       | Done     | Done       | True  |
| 157 | Tensor<[4, 49, 49]> self = ?,<br>int dim = 0          | Done     | Done       | True  |
| 158 | Tensor<[4, 49, 49]> self = ?,<br>int dim = 1          | Done     | Done       | True  |
| 159 | Tensor<[4, 49]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
| 160 | Tensor<[4, 49]> self = ?,<br>int dim = 2              | Done     | Done       | True  |
| 161 | Tensor<[4, 64, 64]> self = ?,<br>int dim = 0          | Done     | Done       | True  |
| 162 | Tensor<[4, 64, 64]> self = ?,<br>int dim = 1          | Done     | Done       | True  |
| 163 | Tensor<[4, 64]> self = ?,<br>int dim = 1              | Done     | Done       | True  |
| 164 | Tensor<[4, 64]> self = ?,<br>int dim = 2              | Done     | Done       | True  |
| 165 | Tensor<[45, 45]> self = ?,<br>int dim = 0             | Done     | Done       | True  |
| 166 | Tensor<[480]> self = ?,<br>int dim = 1                | Done     | Done       | True  |
| 167 | Tensor<[50, 1, 3, 1024]> self = ?,<br>int dim = 0     | Done     | Done       | True  |
| 168 | Tensor<[50, 1, 3, 768]> self = ?,<br>int dim = 0      | Done     | Done       | True  |
| 169 | Tensor<[50]> self = ?,<br>int dim = -1                | Done     | Done       | True  |
| 170 | Tensor<[56]> self = ?,<br>int dim = -1                | Done     | Done       | True  |
| 171 | Tensor<[59, 59]> self = ?,<br>int dim = 0             | Done     | Done       | True  |
| 172 | Tensor<[6, 1, 1]> self = ?,<br>int dim = 0            | Done     | Done       | True  |
| 173 | Tensor<[6, 15, 15]> self = ?,<br>int dim = 0          | Done     | Done       | True  |
| 174 | Tensor<[6, 17, 17]> self = ?,<br>int dim = 0          | Unknown  | Done       | True  |
| 175 | Tensor<[6, 2, 2]> self = ?,<br>int dim = 0            | Unknown  | Done       | True  |
| 176 | Tensor<[6, 49, 49]> self = ?,<br>int dim = 0          | Done     | Done       | True  |
| 177 | Tensor<[6, 64, 64]> self = ?,<br>int dim = 0          | Done     | Done       | True  |
| 178 | Tensor<[6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0  | Unknown  | Unknown    | N/A   |
| 179 | Tensor<[60]> self = ?,<br>int dim = 1                 | Done     | Done       | True  |
| 180 | Tensor<[64, 1, 49, 49]> self = ?,<br>int dim = 0      | Done     | Done       | True  |
| 181 | Tensor<[64, 1, 64, 64]> self = ?,<br>int dim = 0      | Done     | Done       | True  |
| 182 | Tensor<[64, 49, 49]> self = ?,<br>int dim = 1         | Done     | Done       | True  |
| 183 | Tensor<[64, 49]> self = ?,<br>int dim = 1             | Done     | Done       | True  |
| 184 | Tensor<[64, 49]> self = ?,<br>int dim = 2             | Done     | Done       | True  |
| 185 | Tensor<[64, 64, 64]> self = ?,<br>int dim = 1         | Done     | Done       | True  |
| 186 | Tensor<[64, 64]> self = ?,<br>int dim = 1             | Done     | Done       | True  |
| 187 | Tensor<[64, 64]> self = ?,<br>int dim = 2             | Done     | Done       | True  |
| 188 | Tensor<[64]> self = ?,<br>int dim = -1                | Done     | Done       | True  |
| 189 | Tensor<[64]> self = ?,<br>int dim = 0                 | Done     | Done       | True  |
| 190 | Tensor<[7, 7]> self = ?,<br>int dim = 0               | Done     | Done       | True  |
| 191 | Tensor<[7]> self = ?,<br>int dim = -1                 | Done     | Done       | True  |
| 192 | Tensor<[7]> self = ?,<br>int dim = 0                  | Removed  | Done       | True  |
| 193 | Tensor<[8, 1, 1]> self = ?,<br>int dim = 0            | Done     | Done       | True  |
| 194 | Tensor<[8, 10, 10]> self = ?,<br>int dim = 0          | Done     | Done       | True  |
| 195 | Tensor<[8, 2, 2]> self = ?,<br>int dim = 0            | Unknown  | Done       | True  |
| 196 | Tensor<[8, 49, 49]> self = ?,<br>int dim = 0          | Done     | Done       | True  |
| 197 | Tensor<[8, 64, 64]> self = ?,<br>int dim = 0          | Done     | Done       | True  |
| 198 | Tensor<[8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0  | Unknown  | Unknown    | N/A   |
| 199 | Tensor<[800]> self = ?,<br>int dim = 1                | None     | Fallback   | True  |
| 200 | Tensor<[8732]> self = ?,<br>int dim = 1               | Unknown  | Done       | True  |
| 201 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0             | Unknown  | Unknown    | N/A   |
| 202 | Tensor<[s0 + 1]> self = ?,<br>int dim = 1             | Unknown  | Unknown    | N/A   |

