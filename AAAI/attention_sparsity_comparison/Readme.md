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
 |1.1 | zeroth    |  0     | 0.001 | 98.88 | 81.34 | 3.9187 | 94.34 | 78.38 | 4.1388 |
 |1.2 | zeroth    |  0     | 0.0005| 98.79 | 83.69 | 3.7232 | 95.03 | 80.26 | 3.9465 |
 |2.1 | zeroth    |  0.001 | 0.001 | 98.83 | 84.18 | 3.8682 | 95.15 | 81.02 | 4.0746 |
 |2.2 | zeroth    |  0.001 | 0.0005| 99.09 | 80.69 | 4.1593 | 95.29 | 77.63 | 4.4181 |
 |3.1 | zeroth    |  0.003 | 0.001 | 99.06 | 82.25 | 4.1836 | 95.41 | 79.21 | 4.4451 |
 |3.2 | zeroth    |  0.003 | 0.0005| 99.32 | 86.49 | 3.3545 | 95.49 | 83.13 | 3.5912 |
 |4.1 | zeroth    |  0.005 | 0.001 | 98.52 | 86.10 | 2.4659 | 94.99 | 82.57 | 2.5934 |
 |4.2 | zeroth    |  0.005 | 0.0005| 99.04 | 85.39 | 3.1548 | 95.40 | 82.30 | 3.3495 |
 |5.1 | sixth     |  0     | 0.001 | 98.77 | 85.92 | 4.6685 | 94.73 | 82.35 | 4.8302 |
 |5.2 | sixth     |  0     | 0.0005| 98.90 | 86.10 | 5.4152 | 93.85 | 82.01 | 5.4931 |
 |6.1 | sixth     |  0.001 | 0.001 | 99.46 | 78.03 | 3.9369 | 94.65 | 74.54 | 4.0924 |
 |6.2 | sixth     |  0.001 | 0.0005| 99.29 | 87.61 | 3.9897 | 94.99 | 83.82 | 4.1308 |
 |7.1 | sixth     |  0.003 | 0.001 | 99.33 | 75.30 | 2.9134 | 94.33 | 72.64 | 2.9869 |
 |7.2 | sixth     |  0.003 | 0.0005| 99.47 | 88.57 | 4.4092 | 94.64 | 84.55 | 4.5881 |
 | 8  | sixth     |  0.005 | 0.0005| 99.59 | 88.35 | 3.6379 | 94.85 | 84.21 | 3.7670 |
 
 #### Table 3: CIFAR - SparseMax / Spherical softmax / Softmax 
 - Focus net has no bias and weights are initialised to xavier norm, Classification weights are initialised to xavier norm and bias with zeros.
 - seed = 0
 
 |SNo | Seed |avg layer | Attention |  Learning Rate | Train Acc  | Train FTPT | Train avg sparsity | Smplx dist | Test Acc  | Test FTPT | Test avg sparsity | Smplx dist |
 |----|-----------|----------------------|-------|-------|-------|--------| --------- |-------|-------|--------| --------- | ------ |
 | 1 | 0 |zeroth   | SparseMax         | 0.0005 | 99.01 | 86.06 | 1.89 | - | 94.7 | 82.88 | 1.98 | - |
 | 2 | 0 |zeroth   | SparseMax         | 0.001  | 98.75 | 80.03 | 3.25  | - | 95.22 | 76.87 | 3.39 | - |
 |   | 0 |sixth    | SparseMax         | 0.0005 | 98.95 | 86.33 | 2.33 | - |94.39 | 82.26 | 2.44 | -  |
 |   | 1 | sixth   | SparseMax         | 0.0005 | 98.9  | 83.00 | 2.35 | 0.224 | 94.59 | 79.82 | 2.45 | 0.2412 | 
 |   | 2 | sixth   | SparseMax         | 0.0005 | 99.15 | 86.94 | 2.37 | 0.230 | 94.55 | 82.56 | 2.49 | 0.2538 | 
 |   | 0 | sixth   | SparseMax         | 0.001  | 99.29 | 87.48 | 2.17 |  -    | 95.56 | 84.39 | 2.25 | -      | 
 |   | 2 | sixth   | SparseMax         | 0.001  | 99.10 | 78.37 | 2.25 | 0.24 | 95.47 | 75.52 | 2.31 | 0.2618 |
 |   | 0 |zeroth   | Spherical softmax | 0.0005 | 99.26 | 85.08 | 4.78 | -  |94.77 | 81.62 | 5.05 | | 
 |   | 0 |zeroth   | Spherical softmax | 0.001  | 98.41 | 81.21 | 4.34 | -  | 93.89   | 77.84    | 4.58 | |
 |   | 0 | sixth   | Spherical softmax | 0.0005 | 99.34 | 87.80 | 6.19 | -  | 94.17 | 83.13 | 6.31 | |
 |   | 1 | sixth   | Spherical softmax | 0.0005 | 98.97 | 87.77 | 4.75 | 0.262 | 94.72 | 83.78 | 4.86 | 0.2810 | 
 |   | 2 | sixth   | Spherical softmax | 0.0005 | 99.09 | 85.81 | 4.77 | 0.260 | 93.34 | 81.60 | 4.95 | 0.2777 |
 |   | 0 | sixth   | Spherical softmax | 0.001  | 99.32 | 88.69 |  4.29 | | 95.26  | 85.00 | 4.40  | | 
 |   | 1 | sixth   | Spherical softmax | 0.001  | 98.92 | 87.43 |  5.02 | 0.26 | 95.63 | 84.38 | 5.15 | 0.280 |
 |   | 2 | sixth   | Spherical softmax | 0.001  | 99.25 | 87.83 | 4.40  | 0.24 | 95.08 | 84.38 | 4.53 | 0.263 |


<!---| 13  | zeroth    | Softmax (no entropy) | 0.0005 | 98.79 | 83.69 | 3.72 | 95.03 | 80.26 | 3.94 |
 | 14  | zeroth    | Softmax (no entropy) | 0.001 | - | - | - | - | - | - |
 | 15  | zeroth    | Softmax (no entropy) | 0.003 | - | - | - | - | - | - |
 | 16  | sixth     | Softmax (no entropy) | 0.0005 | 98.97 | 86.43 | 6.31 | 93.76 | 82.33 | 6.38 |
 | 17  | sixth     | Softmax (no entropy) | 0.001 | 98.35 | 87.69 | 4.92 | 94.41 | 83.65 | 5.07 |
 | 18  | sixth     | Softmax (no entropy) | 0.003 |  45.43 | 13.48 | 1.006 | 44.42 | 13.47 | 1.004 | 
 | 6  | 0 |sixth     | SparseMax            | 0.003 | 33.79 | 4.55 | 1.003 | 33.53 | 4.54 | 1.003 |
 | 3  | 0 |zeroth    | SparseMax            | 0.003 | 46.38 | 14.69 | 1.003 | 44.92 | 15.37 | 1.00 |
| 9 | 0|zeroth    | Spherical softmax    | 0.003 | 99.44 | 87.53  | 3.71 | 95.62 | 84.84 | 3.89  |
 | 12 |  0|sixth     | Spherical softmax    | 0.003 | 99.39 | 87.51  | 4.66 | 95.41 | 83.80 | 4.78 |
--->

 
 
  
 
