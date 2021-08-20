### Table 1: Datasets and Architecture
| Dataset | Dataset name | Architecture |
|---------|--------------|---------------|
|<img src= ./plots/dataset1.JPG width="300"> | Dataset 1 | Architecture 1 : Focus is MLP with 2 hidden layers of 50 units and Classification is MLP with 1 hidden layer of 50 units with weights initialised with Xavier norm and bias with zeros. |

### TABLE 2:  Analysis of Entropy and Layer averaging

- Architecture 1 : Focus is MLP with 2 hidden layers of 50 units and Classification is MLP with 1 hidden layer of 50 units with weights initialised with Xavier norm and bias with zeros.

| Dataset | Average layer | Architecture | nos_of_runs | Entropy | Optimizer | avg Acc | avg FTPT | best runs | avg best Acc | avg best FTPT | 
|---------|---------------|--------------|-------------|---------|--------|--------|----------|-----------|--------------|---------------|
| Dataset1 | zeroth layer | architecture1 | 20 | NO | Adam(lr=0.001) | 99.98 | 87.02 | 6 | 100 | 100 |
| Dataset1 | zeroth layer | architecture1 | 20 | Yes k = 0.005|  Adam(lr=0.001) | 99.99 | 89.68 | 15 | 100 | 100 |




























