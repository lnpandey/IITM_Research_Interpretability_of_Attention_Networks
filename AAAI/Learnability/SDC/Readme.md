#### Learning Dynamics of Attention Networks

- Cifar data, SDC task for different m values
- initial learning rate for Adam optimizer 0.0005
- focus network CNN 3-layer, classification network CNN 2-layer


##### Table 1A CIFAR data (cl CNN-2)
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

##### Table 1B CIFAR data (cl CNN-1)
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
##### Table 2A MNIST data (cl MLP)
| m  | Train Accuracy | FTPT  | FFPT  | Test Accuracy  | FTPT  | FFPT  |
| -  | -------------- | ----  | ---   | -------------- | ---   | ----  |
| 5(10k)  |   99.80      | 98.28 | 1.52  |     99.24     | 97.72  | 1.52 |
| 5(1k)  |  100       | 96.4  | 3.6 |       98.24   | 94.81 | 3.43 |
|  50(10k)  |   99.65      | 97.13 | 2.52  |    98.52       | 96.09  | 2.43  |
| 50(1k)  |   99.9    | 89.80   | 10.10  |     94.66     | 86.08 | 8.58  |


- MNIST Data Focus MLP Classify Linear 
##### Table 2B MNIST data (cl Linear)
| m  | Train Accuracy | FTPT  | FFPT  | Test Accuracy  | FTPT  | FFPT  |
| -  | -------------- | ----  | ---   | -------------- | ---   | ----  |
| 5(10k)  | 99.81         |  98.93 | 0.88 |     99.33     | 98.38 | 0.95  |
| 5(1k)  |   100    |  96.4 | 3.6 |    97.92      |  94.07 |  3.85 |
| 50(10k) |      99.61     | 53.05 | 46.56  |     97.47      | 52.13 | 45.34  |
| 50(1k)  |    99.70     | 51.10 | 48.60 |   90.80       | 48.69 | 42.11 |

- SDC on Dataset 1 Focus Linear Classification Linear


##### Table 3A  dataset 1 
|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 98.6  | 98.7 | 100 |  100 |
| 2. | 100    | 99.5 | 99.60 | 99.80 | 100  |
| 3. | 2000   | 99.2 | 100 | 99.90 | 100  |


- SDC on Dataset 1 Focus Linear Classification Non-Linear (50)

##### Table 3B  dataset 1 
|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 99.6  | 99.4 | 100 |  100 |
| 2. | 100    | 99.9 | |  | 100  |
| 3. | 2000   | 98.7 |  |  | 100  |

- SDC on Dataset 2 Focus Linear Classification Linear

##### Table 4A  dataset 2

|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 100  | 100 | 100 | 100  |
| 2. | 100    | 67.70 | 100 | 100 | 100  |
| 3. | 2000   | 67.7 | 67.8 | 68.1 |  100 |  


- SDC on Dataset 2 Focus Linear Classification Non-Linear(50)

##### Table 4B  dataset 2
|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 100  | | |  100 |
| 2. | 100    | 100 |  |  | 100  |
| 3. | 2000   | |  | |   100 |  


- SDC on Dataset 3 Focus Linear Classification Linear

##### Table 5A  dataset 3 

|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 87.3 | 88.5  | 89.2 | 87.5 |
| 2. | 100    | 33.6 | 89.4  | 91.2 | 86.5  |
| 3. | 2000   | 32.0 | 42.8 | 91.1 |  90.4 |  

- SDC on Dataset 3 When Foreground classes are linearly separable Focus Linear Classification Linear

##### Table 5B  dataset 3A 
|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 98.7 |  |  99.90 | 100 |
| 2. | 100    | 100 |   | 99.90 |   100 |
| 3. | 2000   |  32.0 | 100 | 99.90 | 100 |  





- SDC on Dataset 4 Focus 1-hidden(50) classification Linear


##### Table 6A  dataset 4 
|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 100 | 99.80 | 94.90 | 97.30 |
| 2. | 100    | 35.10 | 100 | 100 | 99.90  |
| 3. | 2000   | 32.8 | 34.2 | 37.0 | 29.9  |  


- SDC on Dataset 4 Focus 1-hidden(50) classification Non-Linear(50)


##### Table 6B  dataset 4
|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 97.7 |  |  | 100 |
| 2. | 100    | 95.2 |  |  | 98.5 |
| 3. | 2000   | 33.6 |  |  |  32.0 |  


[Code Links](https://drive.google.com/drive/folders/1e8bDLemg_H2u9k-1hUOSwyUNvhTLadAN?usp=sharing)




