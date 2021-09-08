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
|  50  |   99.65      | 98.03 | 1.62  |    99.25       | 97.76  | 1.49  |
| 300  |   99.01      | 51.46 | 47.55 |    97.06       | 49.82  | 47.24 |

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
- LR = 0.001 (by default) else \* = 0.0001, \** = 0.0005, ^=0.01
- MLP2 has 50,10 units in respective 2 hidden layer

<!-- |SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 98.80 | 96.30 / 98.80*  |
| 2. | 10   | 96.80 | 93.20 / 95.60* |
| 3. | 20   | 96.40 | 88.40 / 93.10** |
| 4. | 50   | 89.60 | 88.20 / 91.00** |
| 5. | 100  | 79.00 | 99.10 / 97.30* / 85.60** |
| 6. | 250  | 59.90 | 51.90 / 86.60* / 54.70**|
| 7. | 500  | 48.10 | 48.10 |
| 8. | 1000 | 48.10 | 48.10 | -->

Below experiments are done on linear architecture
|SNo | m-value | size 100 | size 500 | size 1000 | size 2000 | size 10000 |
|----|-------|-------|----------------|----------------|----------------|---------|
| 1. | 5     | 95.00 | 100 / 98.80*   | 98.80          | 99.35          | - |
| 2. | 50    | 55.00 | 92.60 / 95.60* | 89.60 / 90.90^ | 98.85          | - |
| 3. | 100   | 50.00 | 92*            | 79.00 / 82.80^ | 91.00 / 96.10^ | 91.70* |
| 4. | 500   | 50.00 | 71.00 / 51.20  | 48.10          | 49.75 / 59.75^ | 90.71 / 92.10* |
| 5. | 1000  | 50.00 | 51.20          | 48.10          | 49.75          | - |
| 6. | 2000  | 50.00 | 51.20          | 48.10          | 49.75          | - |


### Table 2:  CIN on Dataset 2
- Base distribution fg_class = {0,1,2}, bg_class={3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- train_data = (1/m)\*(sum(m_segments))
- test_data = (1/m)\*(fg_segment)
- epochs = 1500
- LR = 0.001 (by default) else \* = 0.0001
- MLP2 has 50,10 units in respective 2 hidden layer

<!-- |SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 100 | 100 |
| 2. | 10   | 100 | 100 |
| 3. | 20   | 100 | 100 |
| 4. | 50   | 100 | 100 |
| 5. | 100  | 100 | 100 |
| 6. | 250  | 100 | 100 |
| 7. | 500  | 100 | 100 |
| 8. | 1000 | 64.50 | 68.50 |
| 9. | 2000 | 64.50 | 34.20 / 64.50* | -->

Below experiments are done on linear architecture
|SNo | m-value | size 100 | size 500 | size 1000 | size 2000 |
|----|-------|-------|----------------|-------|-------|
| 1. | 5     | 100 | 100  | 100  | 100  |
| 2. | 50    | 100 | 100  | 100  | 100  |
| 3. | 100   | 70  | 100  | 100  | 100  |
| 4. | 500   | 34  | 100  | 99.7 | 100  |
| 5. | 1000  | 34  | 100  | 64.5 | 100  |
| 6. | 2000  | 34  | 32.60| 31.5 | 90.80|

### Table 3:  CIN on Dataset 3
- Base distribution fg_class = {0,1,2}, bg_class={3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- train_data = (1/m)\*(sum(m_segments))
- test_data = (1/m)\*(fg_segment)
- epochs = 1500
- LR = 0.001 (by default) else \* = 0.0001, \** = 0.0005, \*** = 0.00001, \**** = 0.00005
- MLP2 has 50,10 units in respective 2 hidden layer

|SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 81.80 | 96.30 / 49.40 / 83.00* / 76.70** |
| 2. | 10   | 81.00 | 71.90 / 84.10* / 69.70** |
| 3. | 20   | 56.80 | 33.90 / 49.70*** / 52**** |
| 4. | 50   | 31.70 | 31.70 |
| 5. | 100  | 31.50 | 33.00 |
| 6. | 1000 | 31.50 | 35.50 |



### Table 4:  CIN on Dataset 4
- Base distribution fg_class = {0,1,2}, bg_class={3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- train_data = (1/m)\*(sum(m_segments))
- test_data = (1/m)\*(fg_segment)
- epochs = 1500
- LR = 0.001 (by default) else \* = 0.0001, \** = 0.00001
- MLP2 has 50,10 units in respective 2 hidden layer

|SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 71.20 | 35.50 / 99.60* |
| 2. | 10   | 64.00 | 35.20 / 65.20** |
| 3. | 20   | 31.50 | 31.50 |
| 4. | 50   | 31.50 | 31.50 |
| 5. | 100  | 31.50 | 31.50 |
| 6. | 1000 | 31.50 | 31.50 |

