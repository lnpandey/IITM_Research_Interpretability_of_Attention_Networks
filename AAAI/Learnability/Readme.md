#### Learning Dynamics of Attention Networks

- Cifar data, SDC task for different m values
- initial learning rate for Adam optimizer 0.0005
- focus network CNN 3-layer, classification network CNN 2-layer


| m  | Train Accuracy | FTPT  | FFPT  | Test Accuracy  | FTPT  | FFPT  |
| -  | -------------- | ----  | ---   | -------------- | ---   | ----  |
| 5 (30k) | 99.45          | 85.29 | 14.16 |  91.70         | 78.39 | 13.31 |
| 5(10k)  |  99.48       | 76.66      |   22.82    |     75.98           |  60.06     |    15.92  |
| 9  | 99.95          | 80.03 | 19.92 |  91.32         | 75.15 | 16.17 | 
| 10 | 99.91          | 77.96 | 21.94 |  91.51         | 73.96 | 17.55 |
| 20 | 99.82          | 72.19 | 27.63 |  90.61         | 66.76 | 23.85 |
| 50 (30k) | 99.13          | 60.12 | 39.01 |  82.59         | 55.94 | 26.65 |
| 50(10k)  |  99.90       |  46.10   |   53.80    |    60.50            |   34.08    |   26.42    |



- Architecture 2 Focus CNN 3-layer, Classification CNN 1-Layer

| m  | Train Accuracy | FTPT  | FFPT  | Test Accuracy  | FTPT  | FFPT  |
| -  | -------------- | ----  | ---   | -------------- | ---   | ----  |
| 5(30k)  | 99.81   | 86.48  | 13.32 |   90.48        | 79.06 | 11.42 |
| 5(10k)  | 99.94      |  75.71      |   24.23    |      75.48          |     58.90  |    16.58   |
| 9  | 99.83         | 81.54  | 18.29 |  89.26         | 75.57 | 13.69 | 
| 10 | 99.51         | 79.66  | 19.85 |  89.10         | 72.87 | 16.23 |
| 20 | 98.76         | 73.77  | 24.98 |  87.97         | 67.81 | 20.16 |
| 50(30k) | 99.85         | 61.37  | 38.48 |  80.85         | 56.81 | 24.04 |
| 50(10k) | 99.99        |  43.13 |  56.86 | 57.32 | 31.96  |


- MNIST Data Focus MLP Classify MLP

| m  | Train Accuracy | FTPT  | FFPT  | Test Accuracy  | FTPT  | FFPT  |
| -  | -------------- | ----  | ---   | -------------- | ---   | ----  |
| 5(10k)  |   99.80      | 98.28 | 1.52  |     99.24     | 97.72  | 1.52 |
| 5(1k)  |  100       | 96.4  | 3.6 |       98.24   | 94.81 | 3.43 |
|  50(10k)  |   99.65      | 97.13 | 2.52  |    98.52       | 96.09  | 2.43  |
| 50(1k)  |   99.9    | 89.80   | 10.10  |     94.66     | 86.08 | 8.58  |


- MNIST Data Focus MLP Classify Linear 

| m  | Train Accuracy | FTPT  | FFPT  | Test Accuracy  | FTPT  | FFPT  |
| -  | -------------- | ----  | ---   | -------------- | ---   | ----  |
| 5(10k)  | 99.81         |  98.93 | 0.88 |     99.33     | 98.38 | 0.95  |
| 5(1k)  |   100    |  96.4 | 3.6 |    97.92      |  94.07 |  3.85 |
| 50(10k) |      99.61     | 53.05 | 46.56  |     97.47      | 52.13 | 45.34  |
| 50(1k)  |    99.70     | 51.10 | 48.60 |   90.80       | 48.69 | 42.11 |

- SDC on Dataset 1 Focus Linear Classification Linear

|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 99.5  | 99.80 | 100 |  100 |
| 2. | 100    | 99.5 | 99.60 | 99.80 | 100  |
| 3. | 2000   | 99.5 | 100 | 99.90 | 100  |


- SDC on Dataset 1 Focus Linear Classification Non-Linear (50)

|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 99.6  | 99.4 | 100 |  100 |
| 2. | 100    | 99.9 | |  | 100  |
| 3. | 2000   | 98.7 |  |  | 100  |

- SDC on Dataset 2 Focus Linear Classification Linear

|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 100  | 100 | 100 | 100  |
| 2. | 100    | 67.70 | 100 | 100 | 100  |
| 3. | 2000   | 67.7 | 67.8 | 68.1 |  100 |  


- SDC on Dataset 2 Focus Linear Classification Non-Linear(50)

|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 100  | | |  100 |
| 2. | 100    | 100 |  |  | 100  |
| 3. | 2000   | |  | |   100 |  


- SDC on Dataset 3 Focus Linear Classification Linear

|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 87.3 | 88.5  | 89.2 | 87.5 |
| 2. | 100    | 33.6 | 89.4  | 91.2 | 86.5  |
| 3. | 2000   | 32.0 | 42.8 | 91.1 |  90.4 |  

- SDC on Dataset 3 When Foreground classes are linearly separable Focus Linear Classification Linear


|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 98.7 |  |  99.90 | 100 |
| 2. | 100    | 100 |   | 99.90 |   100 |
| 3. | 2000   |  32.0 | 100 | 99.90 | 100 |  

- SDC on Dataset 4 Focus 1-hidden(50) classification Linear

|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 100 | 99.80 | 94.90 | 97.30 |
| 2. | 100    | 34.80 | 66.70 | 99.50 | 99.90  |
| 3. | 2000   | 32.0 | 32.3 | 30.7 | 29.9  |  


- SDC on Dataset 4 Focus 1-hidden(50) classification Non-Linear(50)

|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 97.7 |  |  | 100 |
| 2. | 100    | 95.2 |  |  | 98.5 |
| 3. | 2000   | 33.6 |  |  |  32.0 |  


[Code Links](https://drive.google.com/drive/folders/1e8bDLemg_H2u9k-1hUOSwyUNvhTLadAN?usp=sharing)

### Table A1: CIN on cifar using CNN2 
| SNo. | m-value | Size | Train Acc | Test Acc |
|----|---------|-------|------------|----------|
|1. | 5  | 10k | 100 | 61.94 |
|2. | 10 | 10k | 100 | 52.56 |
|3. | 20 | 10k | 100 | 42.69 |
|4. | 50 | 10k | 100 | 36.07 |
|5. | 5  | 30k | 100 | 59.47 |
|6. | 10 | 30k | 100 | 44.72 |
|7. | 20 | 30k | 100 | 43.61 |
|8. | 50 | 30k | 100 | 32.67 |

### Table A2: CIN on MNIST using Linear 
| SNo. | m-value | Size | Train Acc | Test Acc |
|----|---------|-------|------------|----------|
|1. | 5  | 10k | 96.79 | 99.58 |
|2. | 10 | 10k | 99.58 | 99.43 |
|3. | 20 | 10k | 83.69 | 99.28 |
|4. | 50 | 10k | 74.52 | 98.25 |
|5. |100 | 10k | 68.03 | 92.46 |
|6. | 5  | 30k | 96.12 | 99.59 |
|7. | 50 | 30k | 72.99 | 98.64 |
|8. | 100| 30k | 67.44 | 93.46 |
|9. | 5  | 1k  | 97.6 | 99.50 |
|10.| 50 | 1k  | 75.8 | 95.43 |

|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 99.06 | 99.60 | 99.54 | 99.50  |
| 2. | 100    | 74.30 | 84.5  | 91.09 | 98.88  |
| 3. | 2000   | 46.72 | 53.28 | 53.28 | 53.28  |



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
| 1. | 5     | 95.00 | 100 / 98.80*   | 98.80          | 99.35          | 99.50 |
| 2. | 50    | 55.00 | 92.60 / 95.60* | 89.60 / 90.90^ | 98.85          | 98.70 / 100* |
| 3. | 100   | 50.00 | 92*            | 79.00 / 82.80^ | 91.00 / 96.10^ | 99.50 |
| 4. | 500   | 50.00 | 71.00 / 51.20  | 48.10          | 49.75 / 59.75^ | 90.71 / 92.10* |
| 5. | 1000  | 50.00 | 51.20          | 48.10          | 49.75          | 87.30 / 91.70* / 89.50** |
| 6. | 2000  | 50.00 | 51.20          | 48.10          | 49.75          | 80.90 / 88.60* / 81.30** |


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

<!-- |SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 81.80 | 96.30 / 49.40 / 83.00* / 76.70** |
| 2. | 10   | 81.00 | 71.90 / 84.10* / 69.70** |
| 3. | 20   | 56.80 | 33.90 / 49.70*** / 52**** |
| 4. | 50   | 31.70 | 31.70 |
| 5. | 100  | 31.50 | 33.00 |
| 6. | 1000 | 31.50 | 35.50 | -->
Below experiments are done on linear architecture
|SNo | m-value | size 100 | size 500 | size 1000 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------|-------|---------|
| 1. | 5     | 34.00 | 86.60  | 78.70  | 90.00  | 87.60 |
| 2. | 10    | 34.00 | 89.20  | 79.60  | 89.30  | - |
| 3. | 20    | 34.00 | 86.80  | 55.20  | 84.35 | - |
| 4. | 50    | 34.00 | 74.80  | 31.60  | 72.70 | - |
| 5. | 100   | 34.00 | 35.40  | 31.50  | 67.15 | 35.50 |
| 6. | 500   | 34.00 | 34.60  | 31.50  | 35.85 | - |
| 7. | 2000 | - | - | - | - | 35.50 |


### Table 4:  CIN on Dataset 4
- Base distribution fg_class = {0,1,2}, bg_class={3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- train_data = (1/m)\*(sum(m_segments))
- test_data = (1/m)\*(fg_segment)
- epochs = 1500
- LR = 0.001 (by default) else \* = 0.0001, \** = 0.00001
- MLP2 has 50,10 units in respective 2 hidden layer
<!-- 
|SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 71.20 | 35.50 / 99.60* |
| 2. | 10   | 64.00 | 35.20 / 65.20** |
| 3. | 20   | 31.50 | 31.50 |
| 4. | 50   | 31.50 | 31.50 |
| 5. | 100  | 31.50 | 31.50 |
| 6. | 1000 | 31.50 | 31.50 | -->

Below experiments are done on linear architecture
|SNo | m-value | size 100 | size 500 | size 1000 | size 2000 |
|----|-------|-------|----------------|----------------|---------|
| 1. | 5     | 34.00 | 100    | 70.20  | 100   | 
| 2. | 10    | 34.00 | 100    | 64.00  | 100   | 
| 3. | 20    | 34.00 | 70.00  | 31.50  | 97.2 / 98.75* |
| 4. | 100   | 34.00 | 37.40  | 31.50  | 31.50 | 
| 5. | 500   | 34.00 | 37.40  | 31.50  | 33.15 |
| 6. | 1000  | 34.00 | 37.40  | 31.50  | 33.15 | 



