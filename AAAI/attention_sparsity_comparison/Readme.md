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
