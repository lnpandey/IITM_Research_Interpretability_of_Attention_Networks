### Table 1: Datasets and Architecture
| Dataset | Dataset name | Architecture |
|---------|--------------|---------------|
|<img src= ./plots/dataset1.JPG width="300"> | Dataset 1 | Architecture 1 : Focus is MLP with 2 hidden layers of 50 units and Classification is MLP with 1 hidden layer of 50 units with weights initialised with Xavier norm and bias with zeros. |

### TABLE 2:  Analysis of Entropy and Layer averaging

- Adam Optimizer is used and learning rate is tuned.

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
| 9.  |Dataset1 | second  | architecture1 | 20 | Yes   | 0.005 | 0.001 | - | - | -  | - | - |




























