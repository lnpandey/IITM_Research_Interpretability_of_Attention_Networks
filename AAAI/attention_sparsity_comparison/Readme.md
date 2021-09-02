### Compare different algorithms

- Dataset 2 (elliptical blob 5d data) Architecture 2 (6,12)
- Adam optimizer with initial learning rate 0.001 (specified if some other is used)
- zeroth layer averaging

 #### Table A1
 |Focus Function | Attention Activation | Avg Accuracy  | Avg FTPT | Avg FFPT | Best Runs | Avg Best Acc | Avg Best FTPT | Average Best FFPT|
 | ---- | -----------------    | ---------     | -------  | -----    | ---       |        ----- |   ---------   | --------                  |
 | zero | softmax  |  99.89 |84.41 | 15.48 | 10 | 99.89 | 84.41 | 15.48 | 
 | zero |  sparsemax (lr 0.01 just checked)|  80.81 | 67.19 | 13.61 |  7 | 99.90 | 94.90 | 5.08 | 
 | zero | sparsemax  |   99.85 | 76.86 | 22.99 | 10 | 99.85 | 76.86 | 22.99 |
 | not-zero| softmax | 93.7 | 68.83 | 24.87 | 9 | 99.86 |76.47 | 23.39 |
 | not-zero| sparsemax | 93.45 | 84.21 | 9.24  | 9 | 99.976 | 93.48 | 6.49 |   
 
 #### Table 2: CIFAR - Entropy
 - Focus net has no bias and weights are initialised to xavier norm, Classification weights are initialised to xavier norm and bias with zeros.
 - Attention is softmax
 - seed = 0
 
 |SNo | avg layer | k-value | Learning Rate | Train Acc  | Train FTPT | Train avg sparsity | Test Acc  | Test FTPT | Test avg sparsity |
 |----|-----------|--------|-------|-------|--------|-------|-------|-------|--------|
 | 1  | zeroth    |  0     | 0.001 | 98.88 | 81.34 | 3.9187 | 94.34 | 78.38 | 4.1388 |
 | 2  | zeroth    |  0.001 | 0.001 | 98.83 | 84.18 | 3.8682 | 95.15 | 81.02 | 4.0746 |
 | 3  | zeroth    |  0.003 | 0.001 | 99.06 | 82.25 | 4.1836 | 95.41 | 79.21 | 4.4451 |
 | 4  | zeroth    |  0.005 | 0.001 | 98.52 | 86.10 | 2.4659 | 94.99 | 82.57 | 2.5934 |
 | 5  | sixth     |  0     | 0.001 | 98.77 | 85.92 | 4.6685 | 94.73 | 82.35 | 4.8302 |
 | 6  | sixth     |  0.001 | 0.001 | 99.46 | 78.03 | 3.9369 | 94.65 | 74.54 | 4.0924 |
 | 7  | sixth     |  0.003 | 0.001 | 99.33 | 75.30 | 2.9134 | 94.33 | 72.64 | 2.9869 |
 | 8  | sixth     |  0.005 | 0.0005| 99.59 | 88.35 | 3.6379 | 94.85 | 84.21 | 3.7670 |
 
 #### Table 3: CIFAR - SparseMax / Spherical softmax / Softmax 
 - Focus net has no bias and weights are initialised to xavier norm, Classification weights are initialised to xavier norm and bias with zeros.
 - seed = 0
 - LR = 0.001
 
 |SNo | avg layer | Attention | Train Acc  | Train FTPT | Train avg sparsity | Test Acc  | Test FTPT | Test avg sparsity |
 |----|-----------|--------|-------|-------|--------|-------|-------|--------|
 | 1  | zeroth    | SparseMax            | - | - | - | - | - | - |
 | 2  | sixth     | SparseMax            | - | - | - | - | - | - |
 | 3  | zeroth    | Spherical softmax    | - | - | - | - | - | - |
 | 4  | sixth     | Spherical softmax    | - | - | - | - | - | - |
 | 5  | zeroth    | Softmax (no entropy) | - | - | - | - | - | - |
 | 6  | sixth     | Softmax (no entropy) | - | - | - | - | - | - |

 
 
  
 
