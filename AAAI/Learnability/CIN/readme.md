


<!---### Table 6: CIN on Dataset1 with MLP-1(50) classification---> 
- LR = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5 ]
- Grid search for Best LR
### Table 1A:  CIN on Dataset 1 (Non-Linear)

|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 92.20 | 99.70 | 99.60 | 99.70  |
| 2. | 50     | 83    | 98.90 | 99.40 | 99.00  |
| 2. | 100    | 79.9  | 74.30 | 100   | 99.50  |
| 2. | 500    | 50.20 | 50.10 | 52.3  | -  |
| 3. | 2000   | 50.20 | 50.10 | 52.3  | -  |
<!---
- Base distribution fg_class = {0,1}, bg_class={2,3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- train_data = (1/m)\*(sum(m_segments))
- test_data = (1/m)\*(fg_segment)
- epochs = 1500
- LR = 0.001 (by default) else \* = 0.0001, \** = 0.0005, ^=0.01
- MLP2 has 50,10 units in respective 2 hidden layer -->

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


### Table 1B:  CIN on Dataset 1 (Linear)
<!---Below experiments are done on linear architecture --->
|SNo | m-value | size 100 | size 500 | size 1000 | size 2000 | size 10000 |
|----|-------|-------|----------------|----------------|----------------|---------|
| 1. | 5     | 95.00 | 100 / 98.80*   | 98.80          | 99.35          | 99.50 |
| 2. | 50    | 55.00 | 92.60 / 95.60* | 89.60 / 90.90^ | 98.85          | 98.70 / 100* |
| 3. | 100   | 50.00 | 92*            | 79.00 / 82.80^ | 91.00 / 96.10^ | 99.50 |
| 4. | 500   | 50.00 | 71.00 / 51.20  | 48.10          | 49.75 / 59.75^ | 90.71 / 92.10* |
| 5. | 1000  | 50.00 | 51.20          | 48.10          | 49.75          | 87.30 / 91.70* / 89.50** |
| 6. | 2000  | 50.00 | 51.20          | 48.10          | 49.75          | 80.90 / 88.60* / 81.30** |


<!---  ### Table 2:  CIN on Dataset 2
- Base distribution fg_class = {0,1,2}, bg_class={3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- train_data = (1/m)\*(sum(m_segments))
- test_data = (1/m)\*(fg_segment)
- epochs = 1500
- LR = 0.001 (by default) else \* = 0.0001
- MLP2 has 50,10 units in respective 2 hidden layer --->

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
| 9. | 2000 | 64.50 | 34.20 / 64.50* | 

Below experiments are done on linear architecture -->

### Table 2B:  CIN on Dataset 2 (Linear)
|SNo | m-value | size 100 | size 500 | size 1000 | size 2000 |
|----|-------|-------|----------------|-------|-------|
| 1. | 5     | 100 | 100  | 100  | 100  |
| 2. | 50    | 100 | 100  | 100  | 100  |
| 3. | 100   | 70  | 100  | 100  | 100  |
| 4. | 500   | 34  | 100  | 99.7 | 100  |
| 5. | 1000  | 34  | 100  | 64.5 | 100  |
| 6. | 2000  | 34  | 32.60| 31.5 | 90.80|

<!--- ### Table 3:  CIN on Dataset 3
- Base distribution fg_class = {0,1,2}, bg_class={3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- train_data = (1/m)\*(sum(m_segments))
- test_data = (1/m)\*(fg_segment)
- epochs = 1500
- LR = 0.001 (by default) else \* = 0.0001, \** = 0.0005, \*** = 0.00001, \**** = 0.00005
- MLP2 has 50,10 units in respective 2 hidden layer --->

<!-- |SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 81.80 | 96.30 / 49.40 / 83.00* / 76.70** |
| 2. | 10   | 81.00 | 71.90 / 84.10* / 69.70** |
| 3. | 20   | 56.80 | 33.90 / 49.70*** / 52**** |
| 4. | 50   | 31.70 | 31.70 |
| 5. | 100  | 31.50 | 33.00 |
| 6. | 1000 | 31.50 | 35.50 | 
Below experiments are done on linear architecture -->

### Table 3B:  CIN on Dataset 3 (Linear)
|SNo | m-value | size 100 | size 500 | size 1000 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------|-------|---------|
| 1. | 5     | 34.00 | 86.60  | 78.70  | 90.00  | 87.60 |
| 2. | 10    | 34.00 | 89.20  | 79.60  | 89.30  | - |
| 3. | 20    | 34.00 | 86.80  | 55.20  | 84.35 | - |
| 4. | 50    | 34.00 | 74.80  | 31.60  | 72.70 | - |
| 5. | 100   | 34.00 | 35.40  | 31.50  | 67.15 | 35.50 |
| 6. | 500   | 34.00 | 34.60  | 31.50  | 35.85 | - |
| 7. | 2000 | - | - | - | - | 35.50 |

### Table 3A1: CIN on Dataset 3A (Non-Linear)
|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5    | 100   | 100   | 100   | 100  |
| 2. | 10   | 88.80 | 99.70 | 99.80 | 100  |
| 3. | 20   | 68.60 | 83.30 | 100   | 100  |
| 4. | 50   | 40.00 | 51.50 | 69.00 | 98.80  |
| 5. | 100  | 33.10 | 42.00 | 34    | 36.20  |
| 6. | 2000 | 35.50 | 31.40 | 34    | -      |


<!--- ### Table 4:  CIN on Dataset 4
- Base distribution fg_class = {0,1,2}, bg_class={3,4,5,6,7,8,9}
- base_dist = ( base_dist - bg_mean(bg_class) ) / std_dev(bg_class)
- from these base_dist, Mosaic data is formed with m segments.
- train_data = (1/m)\*(sum(m_segments))
- test_data = (1/m)\*(fg_segment)
- epochs = 1500
- LR = 0.001 (by default) else \* = 0.0001, \** = 0.00001
- MLP2 has 50,10 units in respective 2 hidden layer --->
<!-- 
|SNo | m-value | Linear | MLP2 |
|----|----------|---------|-------|
| 1. | 5    | 71.20 | 35.50 / 99.60* |
| 2. | 10   | 64.00 | 35.20 / 65.20** |
| 3. | 20   | 31.50 | 31.50 |
| 4. | 50   | 31.50 | 31.50 |
| 5. | 100  | 31.50 | 31.50 |
| 6. | 1000 | 31.50 | 31.50 | 

Below experiments are done on linear architecture -->

### Table 4B:  CIN on Dataset 4 (Linear)
|SNo | m-value | size 100 | size 500 | size 1000 | size 2000 |
|----|-------|-------|----------------|----------------|---------|
| 1. | 5     | 34.00 | 100    | 70.20  | 100   | 
| 2. | 10    | 34.00 | 100    | 64.00  | 100   | 
| 3. | 20    | 34.00 | 70.00  | 31.50  | 97.2 / 98.75* |
| 4. | 100   | 34.00 | 37.40  | 31.50  | 31.50 | 
| 5. | 500   | 34.00 | 37.40  | 31.50  | 33.15 |
| 6. | 1000  | 34.00 | 37.40  | 31.50  | 33.15 | 

### Table 5A: CIN on MNIST with MLP-1(50) classification
- LR = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5 ]
- Grid search for Best LR

|SNo | m-value | size 100 | size 500 | size 1000 | size 2000 | size 10000 |
|----|-------|-------|---------------|-----------|----|---------|
| 1. | 5      | 99.54 | 99.75 | 99.65 | 99.68 | 99.66  |
| 2. | 50     | -     | -     | 99.24 | -     | 46.77  |
| 3. | 100    | 85.93 | 98.86 | -     | 98.62 | 46.72  |
| 4. | 2000   | 46.72 | 86.57 | -     | 46.72 | 46.72  |

### Table 5B: CIN on MNIST (Linear)
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
<!-- 
|SNo | m-value | size 100 | size 500 | size 2000 | size 10000 |
|----|-------|-------|----------------|---------------|---------|
| 1. | 5      | 99.06 | 99.60 | 99.54 | 99.50  |
| 2. | 100    | 74.30 | 84.5  | 91.09 | 98.88  |
| 3. | 2000   | 46.72 | 53.28 | 53.28 | 53.28  | -->


### Table 6A: CIN on cifar using CNN2 
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

### Table 6B: CIN on CIFAR using CNN1


<!-- ### Table : CIN on Dataset3 (modified fg non-overlaping) with MLP-1(50) classification
- LR = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5 ]
- Grid search for Best LR -->


