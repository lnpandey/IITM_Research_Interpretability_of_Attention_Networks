data directory contains script to generate data.

model directory contains script to create Focus Module as well as Classification module.

training directory contains script to train the models.


| \Averaging at | At layer zero | At layer one |  At layer two | At layer three  |
| ------------- | ------------- | ------------ | ------------- | --------------  |
| training loss | <img src= ./layer_zero/plots/training_loss_at_zero.png width="400">  | <img src= ./layer_one/plots/training_loss_at_one.png width="400">  | <img src= ./layer_two/plots/training_loss_at_two.png width="400">  | <img src= ./layer_three/plots/training_loss_at_three.png width="400">  |
| training accuracy | 96.68   |  99.55  | 99.41 | 99.83 |
| test accuracy     | 85.98   |  81.22  | 88.25 | 90.01 |


Table 1: CIFAR data with Loss = CE
| Averaging type | #runs | Train Acc | Train FTPT/ FFPT | Test Acc | Test FTPT/ FFPT |
|-----------------| -----|---|------------|----------|----------------|
| Zeroth Layer | run1 (1234) | 99 | 80 / 19 | 95 | 78 / 17 | 
| Zeroth Layer | run2 (1235) | 99.73 | 83.75 / 15.98 | 95.22 | 79.74 / 15.48 |
| Zeroth Layer | run3 (1236) |  |  |  |   |
| third layer  | run1 (1234) | 99 |  88 / 10 |  95 | 84 /10 |
| third layer  | run2 (1235) | 99.79 | 87.26 / 12.53 | 95.23 | 83.09 / 12.14 |
| third layer  | run3 (1236) |  |   |   |  |
| sixth Layer  | run1 (1234) | 98 | 88 / 10 | 94 | 84 / 10 |
| sixth layer  | run2 (1235) | 99.803 | 88.633 / 11.17  | 95.43  | 84.65 / 10.78 |
| sixth layer  | run3 (1236) |  |   |   |  |

Table 2: CIFAR data with Zeroth Layer Averaging and Loss = (1-k)\*CE + k\*Entropy
| K value | #runs |Train Acc | Train FTPT/ FFPT | Test Acc | Test FTPT/ FFPT |
|---------|--------| --------|------------|----------|----------------|
| 0.005 | run1 (1234) | 99 | 84 / 15 | 95 | 81 / 14 | 
| 0.01  | run1 (1234) | 98 | 86 / 12 | 96 | 84 / 12 |
| 0.01  | run2 (1235) |  99.57 | 87.62 / 11.95 | 95.9 | 84.5 / 11.4 |
|       | run3 (1236) |  |  |  |  |

Table 3: CIFAR data with third Layer Averaging and Loss = (1-k)\*CE + k\*Entropy
| K value | #runs | Train Acc | Train FTPT/ FFPT | Test Acc | Test FTPT/ FFPT |
|---------|--------| --------|------------|----------|----------------|
| 0.005 | run1 (1234) | 99 | 90 / 9 | 96 | 86 / 9 |
| 0.01  | run1 (1234) | 99 | 89 / 10 | 96 | 86 / 9 |
| 0.01  | run2 (1235) | 99.73 | 88.62 / 11.11 | 95.6 | 84.9 / 10.7 |
|       | run3 (1236) |  |  |  |  |

Table 4: CIFAR data with Last Layer Averaging and Loss = (1-k)\*CE + k\*Entropy
| K value | #runs | Train Acc | Train FTPT/ FFPT | Test Acc | Test FTPT/ FFPT |
|---------|--------| --------|------------|----------|----------------|
| 0.005 | run1 (1234) | 99 | 88 / 11 | 94 | 84 / 10 | 
| 0.01  | run1 (1234) | 99 | 89 / 10 | 95 | 85 / 10 | 
| 0.05  | run1 (1234) | 98 | 88 / 10 | 95 | 85 / 10 |
| 0.01  | run2 (1235) | 99.9 | 90.13 / 9.77 | 95.95 | 85.99 / 9.96 |
|       | run3 (1236) |  |  |  |  |
