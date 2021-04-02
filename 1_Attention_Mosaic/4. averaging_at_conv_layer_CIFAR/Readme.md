data directory contains script to generate data.

model directory contains script to create Focus Module as well as Classification module.

training directory contains script to train the models.


| \Averaging at | At layer zero | At layer one |  At layer two | At layer three  |
| ------------- | ------------- | ------------ | ------------- | --------------  |
| training loss | <img src= ./layer_zero/plots/training_loss_at_zero.png width="400">  | <img src= ./layer_one/plots/training_loss_at_one.png width="400">  | <img src= ./layer_two/plots/training_loss_at_two.png width="400">  | <img src= ./layer_three/plots/training_loss_at_three.png width="400">  |
| training accuracy | 96.68   |  99.55  | 99.41 | 99.83 |
| test accuracy     | 85.98   |  81.22  | 88.25 | 90.01 |


Table 1.1: CIFAR data with  with Zeroth Layer and Loss = CE
| Averaging type | #runs | Train Acc | Train FTPT/ FFPT | Test Acc | Test FTPT/ FFPT |
|-----------------| -----|---|------------|----------|----------------|
| Zeroth Layer | run1 (1234) | 99.57 | 80.15 / 19.42 | 95.76 | 78.02 / 17.74 | 
| Zeroth Layer | run2 (1235) | 99.73 | 83.75 / 15.98 | 95.22 | 79.74 / 15.48 |
| Zeroth Layer | run3 (1236) | 99.82 | 79.91 / 19.93 | 95.98  | 77.90 /18.08   |
| Zeroth Layer | run4 (1237) | 99.44  | 84.40 / 15.06  | 95.45  | 81 / 14.45   |
| Zeroth Layer | run5 (1238) | 99.64 | 78.25 / 21.39 | 95.87 | 76.30 / 19.57   |

Table 1.2: CIFAR data with  with Third Layer and Loss = CE
| Averaging type | #runs | Train Acc | Train FTPT/ FFPT | Test Acc | Test FTPT/ FFPT |
|-----------------| -----|---|------------|----------|----------------|
| third layer  | run1 (1234) | 99.80 |  88.83 / 10.97 |  95.74 | 84.99 /10.75 |
| third layer  | run2 (1235) | 99.79 | 87.26 / 12.53 | 95.23 | 83.09 / 12.14 |
| third layer  | run3 (1236) | 99.84  | 88.59 / 11.24  | 95.57  | 84.84 / 10.73  |
| third Layer | run4 (1237) | 99.81 | 88.93 / 10.87 | 96.15 | 86.55 / 9.60   |
| third Layer | run5 (1238) | 99.71  | 88 / 11.71 | 95.24 | 83.63 / 11.61  |

Table 1.3: CIFAR data with  with Sixth Layer and Loss = CE
| Averaging type | #runs | Train Acc | Train FTPT/ FFPT | Test Acc | Test FTPT/ FFPT |
|-----------------| -----|---|------------|----------|----------------|
| sixth Layer  | run1 (1234) | 99.70 | 88.73 / 10.97 | 94.85 | 84.32 / 10.53 |
| sixth layer  | run2 (1235) | 99.803 | 88.633 / 11.17  | 95.43  | 84.65 / 10.78 |
| sixth layer  | run3 (1236) | 99.76  | 89.61 / 10.14   |  95.83 | 86.04 / 9.79  |
| sixth Layer | run4 (1237) | 99.67 | 85.7 / 13.97 | 95.53 | 82.48 / 13.05  |
| sixth Layer | run5 (1238) | 99.39 | 85.24 / 14.15 | 94.24 | 80.80 / 13.44  |

Table 2: CIFAR data with Zeroth Layer Averaging and Loss = (1-k)\*CE + k\*Entropy
| K value | #runs |Train Acc | Train FTPT/ FFPT | Test Acc | Test FTPT/ FFPT |
|---------|--------| --------|------------|----------|----------------|
| 0.005 | run1 (1234) | 99 | 84 / 15 | 95 | 81 / 14 | 
| 0.01  | run1 (1234) | 99.6 | 86.87 / 12.73 | 96.78 | 84.46 / 12.32 |
| 0.01  | run2 (1235) |  99.57 | 87.62 / 11.95 | 95.9 | 84.5 / 11.4 |
|  0.01     | run3 (1236) | 99.72 |  86.11 / 13.61  | 96.19 |  82.91 / 13.28 |
|  0.01     | run4 (1237) | 99.75 | 86.84 / 12.91  |  96.53 | 84.30 / 12.23 |
| 0.01  | run5 (1238) | 99.677 | 85.487 / 14.190 | 96.08 | 82.690 / 13.39 |

Table 3: CIFAR data with third Layer Averaging and Loss = (1-k)\*CE + k\*Entropy
| K value | #runs | Train Acc | Train FTPT/ FFPT | Test Acc | Test FTPT/ FFPT |
|---------|--------| --------|------------|----------|----------------|
| 0.005 | run1 (1234) | 99 | 90 / 9 | 96 | 86 / 9 |
| 0.01  | run1 (1234) | 99.82 | 89.48 / 10.34 | 96. | 86.14 / 9.86 |
| 0.01  | run2 (1235) | 99.73 | 88.62 / 11.11 | 95.6 | 84.9 / 10.7 |
|  0.01     | run3 (1236) | 99.81 | 89.36 / 10.44 | 95.72 | 85.68 / 10.04 |
|   0.01    | run4 (1237) | 99.76  | 90.19 / 9.56 | 95.80  | 86.24 / 9.56 |
|   0.01    | run5 (1238) | 99.83  | 90.83/ 9  | 96.43  | 86.94 / 9.49  |

Table 4: CIFAR data with Last Layer Averaging and Loss = (1-k)\*CE + k\*Entropy
| K value | #runs | Train Acc | Train FTPT/ FFPT | Test Acc | Test FTPT/ FFPT |
|---------|--------| --------|------------|----------|----------------|
| 0.005 | run1 (1234) | 99 | 88 / 11 | 94 | 84 / 10 | 
| 0.05  | run1 (1234) | 98 | 88 / 10 | 95 | 85 / 10 |
| 0.01  | run1 (1234) | 99.82 | 89.69 / 10.13 | 95.87 | 85.48 / 10.39 | 
| 0.01  | run2 (1235) | 99.9 | 90.13 / 9.77 | 95.95 | 85.99 / 9.96 |
|  0.01     | run3 (1236) | 99.89 | 90.49 / 9.4 |  96.44 | 86.91 / 9.53 |
|  0.01     | run4 (1237) | 99.84 | 90.02 / 9.81 | 96.10  | 86.26 / 9.84 |
|   0.01    | run5 (1238) | 99.80 | 89.64 / 10.16 | 96.06  | 85.80 / 10.26 |

