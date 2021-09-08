#### Learning Dynamics of Attention Networks

- Cifar data, SDC task for different m values
- initial learning rate for Adam optimizer 0.0005
- focus network CNN 3-layer, classification network CNN 2-layer


| m  | Train Accuracy | FTPT  | FFPT  | Test Accuracy  | FTPT  | FFPT  |
| -  | -------------- | ----  | ---   | -------------- | ---   | ----  |
| 5  | 99.45          | 85.29 | 14.16 |  91.70         | 78.39 | 13.31 |
| 9  | 99.95          | 80.03 | 19.92 |  91.32         | 75.15 | 16.17 | 
| 10 | 99.91          | 77.96 | 21.94 |  91.51         | 73.96 | 17.55 |
| 20 | 99.82          | 72.19 | 27.63 |  90.61         | 66.76 | 23.85 |
| 50 | 99.13          | 60.12 | 39.01 |  82.59         | 55.94 | 26.65 |


- Architecture 2 Focus CNN 3-layer, Classification CNN 1-Layer

| m  | Train Accuracy | FTPT  | FFPT  | Test Accuracy  | FTPT  | FFPT  |
| -  | -------------- | ----  | ---   | -------------- | ---   | ----  |
| 5  | 99.81         | 86.48  | 13.32 |   90.48        | 79.06 | 11.42 |
| 9  | 99.83         | 81.54  | 18.29 |  89.26         | 75.57 | 13.69 | 
| 10 | 99.51         | 79.66  | 19.85 |  89.10         | 72.87 | 16.23 |
| 20 | 98.76         | 73.77  | 24.98 |  87.97         | 67.81 | 20.16 |
| 50 | 99.85         | 61.37  | 38.48 |  80.85         | 56.81 | 24.04 |


- MNIST Data Focus MLP Classify MLP

| m  | Train Accuracy | FTPT  | FFPT  | Test Accuracy  | FTPT  | FFPT  |
| -  | -------------- | ----  | ---   | -------------- | ---   | ----  |
|  50  |   99.65      | 98.03 | 1.62  |    99.25       |97.76  | 1.49  |

- MNIST Data Focus MLP Classify Linear 

| m  | Train Accuracy | FTPT  | FFPT  | Test Accuracy  | FTPT  | FFPT  |
| -  | -------------- | ----  | ---   | -------------- | ---   | ----  |
| 50 |      99.61     | 95.88 | 3.73  |     99.14      | 95.31 | 3.83  |

### Table 1:  CIN on Dataset 1
- Base distribution fg_class = {0,1}, bg_class={2,3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- train_data = (1/m)\*(sum(m_segments))
- test_data = (1/m)\*(fg_segment)
- epochs = 1500
- LR = 0.001 (by default) else \* = 0.0001, \** = 0.0005
- MLP2 has 50,10 units in respective 2 hidden layer

|SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 98.80 | 96.30 / 98.80* |
| 2. | 10   | 96.80 | 93.20 / 95.60* |
| 3. | 20   | 96.40 | 88.40 / 93.10** |
| 4. | 50   | 89.60 | 88.20 / 91.00** |
| 5. | 100  | 79.00 | 99.10 / 97.30* / 85.60** |
| 6. | 250  | 59.90 | 51.90 / 86.60* / 54.70**|
| 7. | 500  | 48.10 | 48.10 |
| 6. | 1000 | 48.10 | 48.10 |

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
- from these base_dist, 2000 Mosaic data is formed with m segments.
- mosaic_data = mosaic_data - mean(mosaic_data[0:1000])/ std_dev(mosaic_data[0:1000])
- mosaic_test = mosaic_data[1000:2000]
- epochs = 1000, LR = 0.001, LR* = 0.0009
- MLP2 has 50,10 units in respective 2 hidden layer and weights are initialised to xavier_normal and bias are initialised to zero.

|SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 100   | 98.20 / 100* |
| 2. | 10   | 100   | 99.30 |
| 3. | 20   | 100   | 76.30 |
| 4. | 50   | 100   | 54.20 |
| 5. | 100  | 61    | 33.30 |
| 6. | 250  | 68.30 | 0     |
| 7. | 500  | 0     | 33.90 |
| 8. | 1000 | 33.50 | 31.40 |

