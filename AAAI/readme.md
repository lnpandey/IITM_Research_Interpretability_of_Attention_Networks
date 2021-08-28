### Table 1: Datasets and Architecture
| Dataset | Dataset name | Architecture |
|---------|--------------|---------------|
|<img src= ./plots/dataset1.JPG width="300"> | Dataset 1 | Architecture 1 : Focus is MLP with 2 hidden layers of 50 units with no bias and weights initialised with Xavier norm. Focus is functionally zero. Classification is MLP with 1 hidden layer of 50 units with weights initialised with Xavier norm and bias with zeros. |

<!-- 
### TABLE 2:  Analysis of Entropy and Layer averaging 
- Adam Optimizer is used and learning rate is tuned.
- Best runs are those runs in which FTPT > 95%

|S.No.| Dataset | Average layer | Architecture | nos_of_runs | Entropy | k-value | LR | avg Acc | avg FTPT | best runs | avg best Acc | avg best FTPT | 
|-----|----|---------------|--------------|-------------|---------|--------|--------|----------|-----------|--------------|---------------|-------------|
| 1.  |Dataset1 | zeroth  | architecture1 | 20 | NO    | -     | 0.001 | 99.98 | 87.02 | 6  | 100   | 100   |
| 2.  |Dataset1 | zeroth  | architecture1 | 20 | Yes   | 0.001 | 0.001 | 99.99 | 89.68 | 9  | 100   | 100   |
| 3.  |Dataset1 | zeroth  | architecture1 | 20 | Yes   | 0.005 | 0.001 | 90.73 | 82.93 | 15 | 100   | 100   |
| 4.  |Dataset1 | first   | architecture1 | 20 | NO    | -     | 0.001 | 99.90 | 73.79 | 0  | -     | -     |
| 5.  |Dataset1 | first   | architecture1 | 20 | Yes   | 0.001 | 0.001 | 99.99 | 85.70 | 9  | 99.99 | 97.65 |
| 6.  |Dataset1 | first   | architecture1 | 20 | Yes   | 0.005 | 0.001 | 99.99 | 85.62 | 8  | 99.99 | 99.98 |
| 7.  |Dataset1 | second  | architecture1 | 20 | NO    | -     | 0.001 | 99.85 | 74.40 | 1  | 99.83 | 96.03 |
| 8.  |Dataset1 | second  | architecture1 | 20 | Yes   | 0.001 | 0.001 | 99.99 | 78.01 | 2  | 99.99 | 99.23 |
| 9.  |Dataset1 | second  | architecture1 | 20 | Yes   | 0.005 | 0.001 | 100   | 82.59 | 7  | 100   | 100   | -->


### TABLE 2:  Analysis of Entropy and Layer averaging on Dataset 1 with Focus net functionally zero
- Focus is MLP with 2 hidden layers of 50 units with no bias and weights initialised with Xavier norm. Focus is functionally zero.
- Classification is MLP with 1 hidden layer of 50 units with weights initialised with Xavier norm and bias with zeros.
- Adam Optimizer is used and learning rate is tuned.
- Best runs are those runs in which Accuracy > 95%

|S.No.| Dataset | Average layer | Architecture | nos_of_runs | Entropy | k-value | LR | avg Acc | avg FTPT | best runs | avg best Acc | avg best FTPT | 
|-----|----|---------------|--------------|-------------|---------|--------|--------|----------|-----------|--------------|---------------|-------------|
| 1.  |Dataset1 | zeroth  | architecture1 | 10 | NO    | -     | 0.001 | 98.89 | 78.34 | 10  | 98.89 | 78.34 |
| 2.  |Dataset1 | zeroth  | architecture1 | 10 | Yes   | 0.0005| 0.001 | 95.60 | 70.56 | 9  | 98.45 | 74.02 |
| 3.  |Dataset1 | zeroth  | architecture1 | 10 | Yes   | 0.001 | 0.001 | 91.93 | 66.31 | 9  | 98.14  | 73.43   |
| 4.  |Dataset1 | zeroth  | architecture1 | 10 | Yes   | 0.005 | 0.001 | 92.48 | 65.95 | 9  | 98.75  | 73.03   |
| 5.  |Dataset1 | zeroth  | architecture1 | 10 | Yes   | 0.01  | 0.001 | 92.44 | 69.83 | 9  | 98.63  | 77.35   |
| 6.  |Dataset1 | first   | architecture1 | 10 | NO    | -     | 0.001 | 99.64 | 78.68 | 10  | 99.64 | 78.68 |
| 7.  |Dataset1 | first   | architecture1 | 10 | Yes   | 0.005 | 0.001 | 99.67 | 82.43 | 10  | 99.67 | 82.43 |
| 8.  |Dataset1 | second  | architecture1 | 10 | NO    | -     | 0.001 | 99.68 | 85.95 | 10  | 99.68 | 85.95 |
| 9.  |Dataset1 | second  | architecture1 | 10 | Yes   | 0.001 | 0.001 | 97.71 | 86.63 | 10  | 97.71 | 86.63 |
| 10.  |Dataset1 | second  | architecture1 | 10 | Yes   | 0.005 | 0.001 | 99.85  | 87.32 | 10  | 99.85  | 87.32 |
| 11.  |Dataset1 | second  | architecture1 | 10 | Yes   | 0.01  | 0.001 | 99.92  | 88.13 | 10  | 99.92  | 88.13 |
| 11.  |Dataset1 | second  | architecture1 | 10 | Yes   | 0.02  | 0.001 | 99.93  | 89.97 | 10  | 99.93  | 89.97 |



























