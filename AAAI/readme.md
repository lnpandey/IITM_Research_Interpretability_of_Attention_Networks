### Table 1: Datasets and Architecture
| Dataset | Dataset name | Architecture |
|---------|--------------|---------------|
|<img src= ./plots/dataset1.JPG width="300"> | Dataset 1 - Architecture A_1 | Focus is MLP with 2 hidden layers of 50 units with no bias and weights initialised with Xavier norm. Focus is functionally zero. Classification is MLP with 1 hidden layer of 50 units with weights initialised with Xavier norm and bias with zeros. |
| 5D elliptical blob data | Dataset 2 - Architecture A_2_1 | Focus is MLP with 1 hidden layer of 50 units with no bias and weights initialised with Xavier norm. Focus is functionally zero. Classification is MLP with 1 hidden layer of 50 units with weights initialised with Xavier norm and bias with zeros.  |
| 5D elliptical blob data | Dataset 2 - Architecture A_2_2 | Focus is MLP with 2 hidden layers of 6, 12 units with no bias and weights initialised with Xavier norm. Focus is functionally zero. Classification is MLP with 2 hidden layers of 6, 12 units with weights initialised with Xavier norm and bias with zeros.  |

# Analysis of Entropy and Layer averaging on different Datasets

### TABLE 2: Dataset 1 with Focus net functionally zero (Architecture A_1)
- Focus is MLP with 2 hidden layers of 50 units with no bias and weights initialised with Xavier norm. Focus is functionally zero.
- Classification is MLP with 1 hidden layer of 50 units with weights initialised with Xavier norm and bias with zeros.
- Adam Optimizer is used and learning rate is tuned.
- Best runs are those runs in which Accuracy > 90%
- LR = 0.001

|S.No.| Dataset | Average layer | Architecture | nos_of_runs | Entropy | k-value | avg Acc | avg FTPT | best runs | avg best Acc | avg best FTPT | 
|-----|----|---------------|--------------|-------------|---------|-------|----------|-----------|--------------|---------------|-------------|
| 1.  |Dataset1 | zeroth  | A_1 | 10 | NO    | 0     |  98.16 | 74.72 | 10  | 98.16 | 74.72 |
| 2.  |Dataset1 | zeroth  | A_1 | 10 | Yes   | 0.0005|  95.60 | 70.56 | 9  | 98.45 | 74.02 |
| 3.  |Dataset1 | zeroth  | A_1 | 10 | Yes   | 0.001 |  91.93 | 66.31 | 9  | 98.14  | 73.43   |
| 4.  |Dataset1 | zeroth  | A_1 | 10 | Yes   | 0.005 |  92.48 | 65.95 | 9  | 98.75  | 73.03   |
| 5.  |Dataset1 | zeroth  | A_1 | 10 | Yes   | 0.01  |  92.44 | 69.83 | 9  | 98.63  | 77.35   |
| 6.  |Dataset1 | zeroth  | A_1 | 10 | Yes   | 0.02  |  56.07 | 25.28 | 3  | 99.43  | 78.67   |
| 7.  |Dataset1 | first   | A_1 | 10 | NO    | 0     |  99.64 | 78.51 | 10  | 99.64 | 78.51 |
| 8.  |Dataset1 | first   | A_1 | 10 | Yes   | 0.0005|  99.61 | 79.06 | 10  | 99.61 | 79.06 |
| 9.  |Dataset1 | first   | A_1 | 10 | Yes   | 0.001 |  99.33 | 72.87 | 10  | 99.33 | 72.87 |
| 8.  |Dataset1 | first   | A_1 | 10 | Yes   | 0.005 |  99.67 | 82.43 | 10  | 99.67 | 82.43 |
| 9.  |Dataset1 | second  | A_1 | 10 | NO    | 0     |  99.68 | 85.95 | 10  | 99.68 | 85.95 |
| 11. |Dataset1 | second  | A_1 | 10 | Yes   | 0.0005|  99.69 | 86.55 | 10  | 99.69 | 86.55 |
| 10. |Dataset1 | second  | A_1 | 10 | Yes   | 0.001 |  97.71 | 86.63 | 10  | 97.71 | 86.63 |
| 11. |Dataset1 | second  | A_1 | 10 | Yes   | 0.005 |  99.85 | 87.32 | 10  | 99.85  | 87.32 |
| 12. |Dataset1 | second  | A_1 | 10 | Yes   | 0.01  |  99.92 | 88.13 | 10  | 99.92  | 88.13 |
| 13. |Dataset1 | second  | A_1 | 10 | Yes   | 0.02  |  99.93 | 89.97 | 10  | 99.93  | 89.97 |

### TABLE 3: Dataset 2 with Focus net functionally zero (Architecture A_2_1)
- Focus is MLP with 1 hidden layers of 50 units with no bias and weights initialised with Xavier norm. Focus is functionally zero.
- Classification is MLP with 1 hidden layer of 50 units with weights initialised with Xavier norm and bias with zeros.
- Adam Optimizer is used and learning rate is tuned.
- Best runs are those runs in which Accuracy > 90%

|S.No.| Dataset | Average layer | Architecture | nos_of_runs | Entropy | k-value | LR | avg Acc | avg FTPT | best runs | avg best Acc | avg best FTPT | 
|-----|----|---------------|--------------|-------------|---------|--------|--------|----------|-----------|--------------|---------------|-------------|
| 1.  |Dataset2 | zeroth  | A_2_1 | 10 | NO    | 0    | 0.001 | 99.99 | 89.13 | 10  | 99.99 | 89.13 |
| 2.  |Dataset2 | zeroth  | A_2_1 | 10 | Yes   | 0.001| 0.001 | 99.99 | 89.15 | 10  | 99.99 | 89.15  |
| 3.  |Dataset2 | zeroth  | A_2_1 | 10 | Yes   | 0.005| 0.001 | 99.99 | 89.21 | 10  | 99.99 |  89.21  |
| 4.  |Dataset2 | zeroth  | A_2_1 | 10 | Yes   | 0.01 | 0.001 | 99.98 | 89.10 | 10  | 99.98 | 89.10    |
| 5.  |Dataset2 | zeroth  | A_2_1 | 10 | Yes   | 0.02 | 0.001 | 99.99 | 88.65 | 10  | 99.99 | 88.65    |
| 6   |Dataset2 | zeroth  | A_2_1 | 10 | Yes   | 0.04 | 0.001 | 77.86 | 60.19 |  6  | 99.98 | 94.65   |
| 7.  |Dataset2 | zeroth  | A_2_1 | 10 | Yes   | 0.05 | 0.001 | 89.35 | 76.67 | 8   | 99.96 |  93.03  |
| 8.  |Dataset2 | first   | A_2_1 | 10 | NO    | 0    | 0.001 | 100   | 93.53 | 10  | 100   | 93.53 |
| 9.  |Dataset2 | first   | A_2_1 | 10 | Yes   | 0.001| 0.001 | 99.99 | 93.54 | 10  | 99.99 | 93.54 |
| 10. |Dataset2 | first   | A_2_1 | 10 | Yes   | 0.005| 0.001 | 99.99 | 93.68 | 10  | 99.99 | 93.68 |
| 11. |Dataset2 | first   | A_2_1 | 10 | Yes   | 0.01 | 0.001 | 99.99 | 94.10 | 10  | 99.99 | 94.10 |
| 12. |Dataset2 | first   | A_2_1 | 10 | Yes   | 0.02 | 0.001 | 100   | 93.56 | 10  | 100   |  93.56 |
| 13. |Dataset2 | first   | A_2_1 | 10 | Yes   | 0.04 | 0.001 | 83.60 | 71.05 | 7   | 99.99 | 99.98    |
| 14. |Dataset2 | first   | A_2_1 | 10 | Yes   | 0.05 | 0.001 | 83.65 | 70.96 | 7   | 100   |  100 |


[Saved Files](https://drive.google.com/drive/folders/1BtHNtq39RXX4r2Cg4KzIMj6haQs4bjX7?usp=sharing)


### TABLE 4: Dataset 2 with Focus net functionally zero (Architecture A_2_2)
- Focus is MLP with 2 hidden layers of 6,12 units with no bias and weights initialised with Xavier norm. Focus is functionally zero.
- Classification is MLP with 2 hidden layers of 6,12 units with weights initialised with Xavier norm and bias with zeros.
- Adam Optimizer is used and learning rate is tuned.
- Best runs are those runs in which Accuracy > 90%

|S.No.| Dataset | Average layer | Architecture | nos_of_runs | Entropy | k-value | LR | avg Acc | avg FTPT | best runs | avg best Acc | avg best FTPT | 
|-----|----|---------------|--------------|-------------|---------|--------|--------|----------|-----------|--------------|---------------|-------------|
| 1.  |Dataset2 | Zeroth  | A_2_2 | 10 | NO    | 0    | 0.001 | 99.89 | 87.62 | 10  | 99.89 | 87.62 |
| 2.  |Dataset2 | Zeroth  | A_2_2 | 10 | Yes   | 0.001| 0.001 |  95.33 | 80.06  | 9  | 99.84  |   85.68 |
| 3.  |Dataset2 | Zeroth  | A_2_2 | 10 | Yes   | 0.002| 0.001 | 89.46  | 74.46 |  8 | 99.97  | 89.375   |
| 4.  |Dataset2 | Zeroth  | A_2_2 | 10 | Yes   | 0.01 | 0.001 | 83.41 | 66.29 | 7 |   99.97 | 89.80   |
| 5.  |Dataset2 | Zeroth  | A_2_2 | 10 | Yes   | 0.02 | 0.001 | 76.67 | 58.12 | 6 | 99.98  | 92.09   |
| 6.  |Dataset2 | First   | A_2_2 | 10 | NO    | 0    | 0.001 | 99.74 | 81.11 | 10  | 99.74 | 81.11 |
| 7.  |Dataset2 | First   | A_2_2 | 10 | Yes   | 0.001| 0.001 | 99.73 | 78.49 | 10  |  99.73 | 78.49|
| 8.  |Dataset2 | First   | A_2_2 | 10 | Yes   | 0.005| 0.001 | 93.59 | 69.97 | 9  | 99.86 | 77.65 |
| 9.  |Dataset2 | First   | A_2_2 | 10 | Yes   | 0.01 | 0.001 | 82.75 | 58.24 | 7 | 99.90 | 80.22 |
| 10. |Dataset2 | First   | A_2_2 | 10 | Yes   | 0.02 | 0.001 | 65.34 | 35.81 | 4 | 99.93 | 80.25 |
| 11. |Dataset2 | First   | A_2_2 | 10 | Yes   | 0.03 | 0.001 | 64.02 | 37.27 | 4 | 99.97 | 85.60 |
| 12.  |Dataset2 | Second  | A_2_2 | 10 | NO    | 0    | 0.001 | 99.89 | 93.89 | 10  | 99.89 | 93.89 |
| 13.  |Dataset2 | Second  | A_2_2 | 10 | Yes   | 0.001| 0.001 | 99.52 | 90.26 | 10 | 99.52 | 90.26  |
| 14.  |Dataset2 | Second  | A_2_2 | 10 | Yes   | 0.005| 0.001 | 88.05 | 72.14 | 8 | 99.65 | 88.44 |
| 15.  |Dataset2 | Second  | A_2_2 | 10 | Yes   | 0.01 | 0.001 | 81.26 | 63.9 | 7 | 99.98 | 91.09 |
| 16. |Dataset2 | Second  | A_2_2 | 10 | Yes   | 0.02 | 0.001 | 69.12  | 47.9 | 5  | 99.9 | 94.14 |



### Table 5: Cifar data with zeroth layer averaging No Entropy

| Seed | Run_  | train Accuracy  | train FTPT |  train FFPT | test Accuracy | test FTPT | test FFPT |   
| ---- | ----  | ---             | ---        | ----        |   -----       | ----      | ----      | 
|   0  |  1    |     99.15            |       80.05   |  19.10           |    95.22      | 77.15  | 18.07  |
|   1  |  2    |    99.29        |    82.51     |   16.78    |      95.26    |  79.96 | 15.30   |
|   2  |  3   |       98.79          |    80.43        |        18.36     |   94.65       | 77.34  | 17.31  |


### Table 7: Cifar data with zeroth layer (last) averaging Entropy

|S.NO| Seed | Run_  | k value |  train Accuracy  | train FTPT |  train FFPT | test Accuracy | test FTPT | test FFPT |   
|-| ---- | ----  | --      |---             | ---        | ----        |   -----       | ----      | ----      | 
|1|   0  |  1    | 0.001 |   99.28        | 79.34   | 19.93 |       95.37 |  76.59 |  18.78  |
|2|   1  |  2    | 0.001 |  99.21      |  84.23   |  14.98      |    94.76      | 81.26  |  13.5 |
|3|   2  |  3   |  0.001 |   99.04      |   80.40   |  18.64           |    94.15      |  77.13 | 17.02  |
|4|   0  |  1    | 0.005 |      99.38      |  82   | 17.38  |    95.64     | 79.07  |  16.57   |
|5|   1  |  2    | 0.005 |   99.23     |  87.19   |   12.04    |   96.04       |  84.10 |  11.94 |
|6|   2  |  3   |  0.005 |     98.88    |   83.45   |     15.43        |     95.58     | 81.06  | 14.52   |
|7|   0  | 1    | 0.01   |   65.40      |   27.91   |     37.49        |   54.62      |   27.61 |  27.01 |
|8|   1  | 2    | 0.01   |  99.24        |  87.67    |      11.57       |   95.13      |  84.76  | 10.37  |
|9|   2  | 3    | 0.01   |    68.76     |    27.48  |  41.28            |  53.11       | 27.51    |  25.6 |



### Table 6: Cifar data with sixth layer (last) averaging No Entropy

| Seed | Run_  | train Accuracy  | train FTPT |  train FFPT | test Accuracy | test FTPT | test FFPT |   
| ---- | ----  | ---             | ---        | ----        |   -----       | ----      | ----      | 
|   0  |  1    |     98.43       |    86.14   |   12.31     |   94.40       |  82.25 | 12.15   |
|   1  |  2    |        99.32    |     89.21  |  10.10     |   96.05       | 85.99  | 10.06  |
|   2  |  3   |      99.27       |   88.26    |     11.01        |   94.92       |  83.75 |  11.17 |


### Table 7: Cifar data with sixth layer (last) averaging Entropy

|S.NO| Seed | Run_  | k value |  train Accuracy  | train FTPT |  train FFPT | test Accuracy | test FTPT | test FFPT |   
|-| ---- | ----  | --      |---             | ---        | ----        |   -----       | ----      | ----      | 
|1|   0  |  1    | 0.001 |  99.14 | 87.44 | 11.70 | 94.75 | 84.17 | 10.58 |
|2|   1  |  2    | 0.001 |  99.15 | 87.98 | 11.16 | 95.10 | 84.62 | 10.48 |
|3|   2  |  3   |  0.001 |  99.09 | 88.69 | 10.40 | 94.81 | 84.44 | 10.37 |
|4|   0  |  1    | 0.005 |   99.13       |  87.55  | 11.58 |   95.39      | 84.22  |  11.17  |
|5|   1  |  2    | 0.005 |     98.98   |   87.31  |   11.67    |   95.32       |  83.67 |  11.65 |
|6|   2  |  3   |  0.005 |     99.20    |    79.98  |      19.22       |  95.48        |  77.35 | 18.13  |
|7|   0  | 1    | 0.01   |   99.28      |    77.70  |      21.58       |   95.87      | 75.21   | 20.66  |
|8|   1  | 2    | 0.01   |   99.46      |  87.63    |    11.83         |       96.12  | 84.57   | 11.55  |
|9|   2  | 3    | 0.01   |   99.13      |   78.93    |    20.19         |    95.02     |  76.21  |  18.81  |


