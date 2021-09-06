#### Learning Dynamics of Attention Networks

- Cifar data, SDC task for different m values
- initial learning rate for Adam optimizer 0.0005
- focus network CNN 3-layer, classification network CNN 2-layer


| m  | Train Accuracy | FTPT  | FFPT  | Test Accuracy  | FTPT  | FFPT  |
| -  | -------------- | ----  | ---   | -------------- | ---   | ----  |
| 5  | 99.45          | 85.29 | 14.16 |  91.70         | 78.39 | 13.31 |
| 9  | 99.86          | 79.42 | 20.43 |  90.69         | 74.03 | 16.66 |
| 10 | 99.60          | 77.01 | 22.59 |  90.85         | 72.54 | 18.31 |
| 20 | 98.72          | 71.01 | 27.71 |  87.95         | 64.46 | 23.49 |
| 50 | 99.13          | 60.12 | 39.01 |  82.59         | 55.94 | 26.65 |

### Table 1:  CIN on Dataset 1
- Base distribution fg_class = {0,1}, bg_class={2,3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- mosaic_train = mosaic_train - mean(mosaic_train)/ std_dev(mosaic_train)
- mosaic_test = mosaic_test - mean(mosaic_test)/ std_dev(mosaic_test). Note that test mean and std_dev is used to make the dataset same transform numerically.
- epochs = 1000, LR = 0.001
- MLP2 has 50,10 units in respective 2 hidden layer

|SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 98.4  | 99.70 |
| 2. | 10   | 96.5  | 99.70 |
| 3. | 20   | 98.00 | 97.70 |
| 4. | 50   | 95.30 | 92.20 |
| 5. | 100  | 93.00 | 75.70 |
| 6. | 1000 | 85.80 | 56.60 |

### Table 2:  CIN on Dataset 2
- Base distribution fg_class = {0,1,2}, bg_class={3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- mosaic_train = mosaic_train - mean(mosaic_train)/ std_dev(mosaic_train)
- mosaic_test = mosaic_test - mean(mosaic_test)/ std_dev(mosaic_test). Note that test mean and std_dev is used to make the dataset same transform numerically.
- epochs = 1000, LR = 0.001
- MLP2 has 50,10 units in respective 2 hidden layer

|SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | -  | - |
| 2. | 10   | -  | - |
| 3. | 20   | -  | - |
| 4. | 50   | -  | - |
| 5. | 100  | -  | - |
| 6. | 1000 | -  | - |

### Table 3:  CIN on Dataset 3
- Base distribution fg_class = {0,1,2}, bg_class={3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- mosaic_train = mosaic_train - mean(mosaic_train)/ std_dev(mosaic_train)
- mosaic_test = mosaic_test - mean(mosaic_test)/ std_dev(mosaic_test). Note that test mean and std_dev is used to make the dataset same transform numerically.
- epochs = 1000, LR = 0.001
- MLP2 has 50,10 units in respective 2 hidden layer

|SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | -  | - |
| 2. | 10   | -  | - |
| 3. | 20   | -  | - |
| 4. | 50   | -  | - |
| 5. | 100  | -  | - |
| 6. | 1000 | -  | - |

### Table 4:  CIN on Dataset 4
- Base distribution fg_class = {0,1,2}, bg_class={3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- mosaic_train = mosaic_train - mean(mosaic_train)/ std_dev(mosaic_train)
- mosaic_test = mosaic_test - mean(mosaic_test)/ std_dev(mosaic_test). Note that test mean and std_dev is used to make the dataset same transform numerically.
- epochs = 1000, LR = 0.001
- MLP2 has 50,10 units in respective 2 hidden layer

|SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 100   | 84.20 |
| 2. | 10   | 100   | 65.80 |
| 3. | 20   | 99.90 | 64.30 |
| 4. | 50   | 64.50 | 57.90 |
| 5. | 100  | 31.60 | 32.30 |
| 6. | 1000 | 42.30 | 27.80 |

