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

|S.No.| Dataset | Average layer | Architecture | nos_of_runs | Entropy | k-value | LR | avg Acc | avg FTPT | best runs | avg best Acc | avg best FTPT | 
|-----|----|---------------|--------------|-------------|---------|--------|--------|----------|-----------|--------------|---------------|-------------|
| 1.  |Dataset1 | zeroth  | A_1 | 10 | NO    | 0    | 0.001 | 98.16 | 74.72 | 10  | 98.16 | 74.72 |
| 2.  |Dataset1 | zeroth  | A_1 | 10 | Yes   | 0.0005| 0.001 | 95.60 | 70.56 | 9  | 98.45 | 74.02 |
| 3.  |Dataset1 | zeroth  | A_1 | 10 | Yes   | 0.001 | 0.001 | 91.93 | 66.31 | 9  | 98.14  | 73.43   |
| 4.  |Dataset1 | zeroth  | A_1 | 10 | Yes   | 0.005 | 0.001 | 92.48 | 65.95 | 9  | 98.75  | 73.03   |
| 5.  |Dataset1 | zeroth  | A_1 | 10 | Yes   | 0.01  | 0.001 | 92.44 | 69.83 | 9  | 98.63  | 77.35   |
| 6.  |Dataset1 | zeroth  | A_1 | 10 | Yes   | 0.02  | 0.001 | 56.07 | 25.28 | 3  | 99.43  | 78.67   |
| 7.  |Dataset1 | first   | A_1 | 10 | NO    | 0     | 0.001 | 99.64 | 78.51 | 10  | 99.64 | 78.51 |
| 8.  |Dataset1 | first   | A_1 | 10 | Yes   | 0.005 | 0.001 | 99.67 | 82.43 | 10  | 99.67 | 82.43 |
| 9.  |Dataset1 | second  | A_1 | 10 | NO    | 0    | 0.001 | 99.68 | 85.95 | 10  | 99.68 | 85.95 |
| 10.  |Dataset1 | second  | A_1 | 10 | Yes   | 0.001 | 0.001 | 97.71 | 86.63 | 10  | 97.71 | 86.63 |
| 11.  |Dataset1 | second  | A_1 | 10 | Yes   | 0.005 | 0.001 | 99.85  | 87.32 | 10  | 99.85  | 87.32 |
| 12.  |Dataset1 | second  | A_1 | 10 | Yes   | 0.01  | 0.001 | 99.92  | 88.13 | 10  | 99.92  | 88.13 |
| 13.  |Dataset1 | second  | A_1 | 10 | Yes   | 0.02  | 0.001 | 99.93  | 89.97 | 10  | 99.93  | 89.97 |

### TABLE 2: Dataset 2 with Focus net functionally zero (Architecture A_2_1)
- Focus is MLP with 1 hidden layers of 50 units with no bias and weights initialised with Xavier norm. Focus is functionally zero.
- Classification is MLP with 1 hidden layer of 50 units with weights initialised with Xavier norm and bias with zeros.
- Adam Optimizer is used and learning rate is tuned.
- Best runs are those runs in which Accuracy > 90%

|S.No.| Dataset | Average layer | Architecture | nos_of_runs | Entropy | k-value | LR | avg Acc | avg FTPT | best runs | avg best Acc | avg best FTPT | 
|-----|----|---------------|--------------|-------------|---------|--------|--------|----------|-----------|--------------|---------------|-------------|
| 1.  |Dataset2 | zeroth  | A_2_1 | 10 | NO    | 0    | 0.001 | 99.99 | 89.13 | 10  | 99.99 | 89.13 |
| 2.  |Dataset2 | zeroth  | A_2_1 | 10 | Yes   | 0.001| 0.001 | 99.99  |  89.15 | 10  | 99.99 | 89.15  |
| 3.  |Dataset2 | zeroth  | A_2_1 | 10 | Yes   | 0.005| 0.001 | 99.99 | 89.21  | 10 |  99.99 |  89.21  |
| 4.  |Dataset2 | zeroth  | A_2_1 | 10 | Yes   | 0.01 | 0.001 | 99.98  | 89.10  | 10  | 99.98  | 89.10    |
| 5.  |Dataset2 | zeroth  | A_2_1 | 10 | Yes   | 0.02 | 0.001 | 99.99 |  88.65 | 10  | 99.99  | 88.65    |
| 6.  |Dataset2 | first   | A_2_1 | 10 | NO    | 0    | 0.001 | 100 | 93.53 | 10  | 100 | 93.53 |
| 7.  |Dataset2 | first   | A_2_1 | 10 | Yes   | 0.001| 0.001 |  | |  | | |
| 8.  |Dataset2 | first   | A_2_1 | 10 | Yes   | 0.005| 0.001 |  | |  | | |
| 9.  |Dataset2 | first   | A_2_1 | 10 | Yes   | 0.01 | 0.001 |  | |  | | |
| 10. |Dataset2 | first   | A_2_1 | 10 | Yes   | 0.02 | 0.001 |  | |  | | |

### TABLE 3: Dataset 2 with Focus net functionally zero (Architecture A_2_2)
- Focus is MLP with 2 hidden layers of 6,12 units with no bias and weights initialised with Xavier norm. Focus is functionally zero.
- Classification is MLP with 2 hidden layers of 6,12 units with weights initialised with Xavier norm and bias with zeros.
- Adam Optimizer is used and learning rate is tuned.
- Best runs are those runs in which Accuracy > 90%

|S.No.| Dataset | Average layer | Architecture | nos_of_runs | Entropy | k-value | LR | avg Acc | avg FTPT | best runs | avg best Acc | avg best FTPT | 
|-----|----|---------------|--------------|-------------|---------|--------|--------|----------|-----------|--------------|---------------|-------------|
| 1.  |Dataset2 | zeroth  | A_2_2 | 10 | NO    | 0    | 0.001 | 99.89 | 87.62 | 10  | 99.89 | 87.62 |
| 2.  |Dataset2 | zeroth  | A_2_2 | 10 | Yes   | 0.001| 0.001 |  |  |   |  |  |
| 3.  |Dataset2 | zeroth  | A_2_2 | 10 | Yes   | 0.002| 0.001 |  |  |  |   |    |
| 4.  |Dataset2 | zeroth  | A_2_2 | 10 | Yes   | 0.01 | 0.001 |  |  |  |   |    |
| 5.  |Dataset2 | zeroth  | A_2_2 | 10 | Yes   | 0.02 | 0.001 |  |  |  |   |    |
| 6.  |Dataset2 | first   | A_2_2 | 10 | NO    | 0    | 0.001 | 99.74 | 81.11 | 10  | 99.74 | 81.11  |
| 7.  |Dataset2 | first   | A_2_2 | 10 | Yes   | 0.001| 0.001 |  | |  | | |
| 8.  |Dataset2 | first   | A_2_2 | 10 | Yes   | 0.005| 0.001 |  | |  | | |
| 9.  |Dataset2 | first   | A_2_2 | 10 | Yes   | 0.01 | 0.001 |  | |  | | |
| 10. |Dataset2 | first   | A_2_2 | 10 | Yes   | 0.02 | 0.001 |  | |  | | |




























