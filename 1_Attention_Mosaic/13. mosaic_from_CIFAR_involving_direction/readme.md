## Experiment 1 setup:
1. In CIFAR 10 Dataset (shape: 50000x32x32x3), Reshape it to Matrix A : 50000x3072 then apply SVD on A to get the USV^T, Where V is Orthogonal vectors in row space(A).
2. Consider the last 3 row vectors in V^T (or last 3 column vectors in V) which have least variance (as S has eigen values in descending order).
3. Let these 3 vectors be u1,u2,u3. Now consider Foregorund classes as fg1,fg2,fg3 out of 10 classes of CIFAR 10.
4. Update the Train and Test Dataset as following:

    for all img in CIFAR10 s.t label(img) == fg1 , img = img + gamma * |img| * u1  ; 
    
    for all img in CIFAR10 s.t label(img) == fg2 , img = img + gamma * |img| * u2  ; 
    
    for all img in CIFAR10 s.t label(img) == fg3 , img = img + gamma * |img| * u3  ; 
    
5. Now Create the Train Mosaic Dataset from updated Train CIFAR10 Dataset and Test Mosaic Dataset from updated Test CIFAR10 Dataset.
6. Train on this training Mosaic dataset and report the FTPT, FFPT, FTPF, FFPF on train and test mosaic dataset.

## Table 1 gamma = 0.1 for Experiment 1:
    
|Sno.|FG classes| #run | train/ test | on Dataset | FTPT | FFPT | FTPF | FFPF | alpha>0.5 | Epochs req for training|
|----|----------|------|----|------|------|-----|------|--------------|--------------|---------|
| 1. | 0,1,2 | run1 | trained | 30k mosaic from 50k training | 27.21 | 71.59 | 0.31 | 0.89 | 0 | 27 |
|    |       |      | test    | 10k mosaic from 50k training | 26.33 | 72.63 | 0.25 | 0.79 | 0 |    |
|    |       |      | test    | 10k mosaic from 10k testing  | 26.48 | 72.33 | 0.41 | 0.78 | 0 |    |
| 2. | 0,1,2 | run2 | trained | 30k mosaic from 50k training | 59.97 | 39.31 | 0.69 | 0.02 | 221 | 29 |
|    |       |      | test    | 10k mosaic from 50k training | 59.64 | 39.6  | 0.71 | 0.05 | 78 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 59.81 | 38.7  | 1.49 | 0    | 109 |  |
| 3. | 0,1,2 | run3 | trained | 30k mosaic from 50k training | 99.44 | 0.03  | 0.51 | 0.01 | 29989 | 27 |
|    |       |      | test    | 10k mosaic from 50k training | 99.45 | 0.01  | 0.53 | 0.01 | 9998 |  |
|    |       |      | test    |  10k mosaic from 10k testing | 99.22 |  0    | 0.78 | 0    | 9997 |  |
| 4. | 0,1,2 | run4 | trained | 30k mosaic from 50k training | 15.7  | 82.82 | 0.13 | 1.35 | 0    | 17 |
|    |       |      | test    | 10k mosaic from 50k training | 15.73 | 82.42 | 0.22 | 1.63 | 0    |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 16.46 | 81.89 | 0.17 | 1.48 | 0    |  |
| 5. | 1,2,3 | run1 | trained | 30k mosaic from 50k training | 16.24 | 82.72 | 0.33 | 0.70 | 0    | 23 |
|    |       |      | test    | 10k mosaic from 50k training | 16.33 | 82.59 | 0.36 | 0.72 | 0 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 16.52 | 82.17 | 0.52 | 0.79 | 0 |  |
| 6. | 1,2,3 | run2 | trained | 30k mosaic from 50k training | 11.79 | 87.3 | 0.13 | 0.77 | 0 | 19 |
|    |       |      | test    | 10k mosaic from 50k training | 12.42 | 86.68 | 0.15 | 0.75 | 0 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 11.8 | 86.81 | 0.16 | 1.23 | 0 |  |
| 7. | 1,2,3 | run3 | trained | 30k mosaic from 50k training | 98.94 | 0.3 | 0.75 | 0.01 | 3440 | 29 |
|    |       |      | test    | 10k mosaic from 50k training | 98.88 | 0.24 | 0.87 | 0.01 | 1112 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 98.7 | 0.17 | 1.12 | 0.01 | 1047 |  |
| 8. | 0,1,2 | run4 | trained | 30k mosaic from 50k training | 90.11 | 9.30 | 0.58 |  0  | 653 | 26 |
|    |       |      | test    | 10k mosaic from 50k training | 89.47 | 9.92 | 0.61 |   0 | 236 |    |
|    |       |      | test    | 10k mosaic from 10k testing  | 90.64 | 8.42 | 0.94 |  0  | 233 |    |
| 9. | 2,3,4 | run1 | trained | 30k mosaic from 50k training | 48.01 | 50.89 | 0.87 | 0.24 | 0 | 30 |
|    |       |      | test    | 10k mosaic from 50k training | 47.54 | 51.11 | 1.04 | 0.31 | 0 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 49.17 | 49.13 | 1.21 | 0.49 | 0 |  |
| 10. | 2,3,4 | run2 | trained |30k mosaic from 50k training  | 18.85 | 79.46 | 0.39 | 1.3 | 0 | 33 |
|     |       |      | test    | 10k mosaic from 50k training | 18.94 | 79.01 | 0.5 | 1.55 | 0 |  |
|     |       |      | test    | 10k mosaic from 10k testing  | 19.56 | 78.69 | 0.46 | 1.29 | 0 |  |
| 11. | 2,3,4 | run3 | trained | 30k mosaic from 50k training | 75.93 | 22.79 | 1.23 | 0.05 | 793 | 47 |
|     |       |      | test    | 10k mosaic from 50k training | 75.8 | 22.83 | 1.3 | 0.07 | 296 |  |
|     |       |      | test    | 10k mosaic from 10k testing  | 75.69 | 23.03 | 1.24 | 0.04 | 277 |  |
| 12. | 3,4,5 | run1 | trained | 30k mosaic from 50k training | 23.19 | 75.97 | 0.20 | 0.62 | 0 | 26 |
|     |       |      | test    | 10k mosaic from 50k training | 22.31 | 76.76 | 0.34 | 0.59 | 0 |  |
|     |       |      | test    | 10k mosaic from 10k testing  | 24.44 | 74.58 | 0.26 | 0.72 | 0 |  |
| 13. | 3,4,5 | run2 | trained | 30k mosaic from 50k training | 22.37 | 76.63 | 0.17 | 0.82 | 0 | 47 |
|     |       |      | test    | 10k mosaic from 50k training | 21.96 | 77.09 | 0.27 | 0.68 | 0 |  |
|     |       |      | test    | 10k mosaic from 10k testing  | 23.17 | 76 | 0.16 | 0.67 | 0 |  |
| 14. | 3,4,5 | run3 | trained | 30k mosaic from 50k training | 17.7 | 81.25 | 0.09 | 0.96 | 0 | 36 |
|     |       |      | test    | 10k mosaic from 50k training | 18.15 | 80.7 | 0.13 | 1.02 | 0 |  |
|     |       |      | test    | 10k mosaic from 10k testing  | 19.17 | 79.73 | 0.19 | 0.91 | 0 |  |

## Table 1 gamma = 0.02 for Experiment 1:
    
|Sno.|FG classes| #run | train/ test | on Dataset | FTPT | FFPT | FTPF | FFPF | alpha>0.5 | Epochs req for training|
|----|----------|------|----|------|------|-----|------|--------------|--------------|---------|
| 1. | 0,1,2 | run1 | trained | 30k mosaic from 50k training | 29.44 | 69.19 | 0.30 | 1.06 | 0 | 34 |
|    |       |      | test    | 10k mosaic from 50k training | 29.63 | 68.93 | 0.34 | 1.10 | 0 |    |
|    |       |      | test    | 10k mosaic from 10k testing  | 29.09 | 69.54 | 0.30 | 1.07 | 0 |    |
| 2. | 0,1,2 | run2 | trained | 30k mosaic from 50k training | 76.32 | 22.86 | 0.81 | 0.006 | 20331 | 33 |
|    |       |      | test    | 10k mosaic from 50k training | 76.24 | 22.13 | 1.63 | 0     | 6851 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 76.64 | 22.97 | 4.39 | 0     | 6745 |  |
| 3. | 0,1,2 | run3 | trained | 30k mosaic from 50k training | 81.66 | 17.70  | 0.63 | 0 | 20360 | 22 |
|    |       |      | test    | 10k mosaic from 50k training | 81.45 | 17.52  | 1.03 | 0 | 6840 |  |
|    |       |      | test    |  10k mosaic from 10k testing | 80.35 | 17.52  | 2.13 | 0 | 6815 |  |
| 4. | 0,1,2 | run4 | trained | 30k mosaic from 50k training | 28.33  | 70.43 | 0.31 | 0.91 | 0    | 44 |
|    |       |      | test    | 10k mosaic from 50k training | 28.76 | 69.89 | 0.34 | 1.01 | 0    |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 27.48 | 70.80 | 0.39 | 1.33 | 0    |  |
| 5. | 1,2,3 | run1 | trained | 30k mosaic from 50k training | 99.39 | 0 | 0.6 | 0 | 30000    | 32 |
|    |       |      | test    | 10k mosaic from 50k training | 99.47 | 0 | 0.53 | 0 | 10000 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 99.6 | 0 | 1.4 | 0 | 10000 |  |
| 6. | 1,2,3 | run2 | trained | 30k mosaic from 50k training | 28.73 | 69.93 | 0.53 | 0.8 | 39 | 62 |
|    |       |      | test    | 10k mosaic from 50k training | 28.58 | 70.69 | 0.62 | 1.11 | 8 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 27.97 | 69.89 | 0.97 | 1.17 | 9 |  |
| 7. | 1,2,3 | run3 | trained | 30k mosaic from 50k training | 30.67 | 67.85 | 0.72 | 0.75 | 17 | 51 |
|    |       |      | test    | 10k mosaic from 50k training | 30.91 | 67.59 | 0.75 | 0.75 | 4 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 31.2 | 66.80 | 1.14 | 0.86 | 0 |  |

## Table 1 gamma = 0.14 for Experiment 1:
    
|Sno.|FG classes| #run | train/ test | on Dataset | FTPT | FFPT | FTPF | FFPF | alpha>0.5 | Epochs req for training|
|----|----------|------|----|------|------|-----|------|--------------|--------------|---------|
| 1. | 0,1,2 | run1 | trained | 30k mosaic from 50k training | 19.74 | 79.51 | 0.09 | 0.65 | 0 | 20 |
|    |       |      | test    | 10k mosaic from 50k training | 20.23 | 78.85 | 0.14 | 0.78 | 0 |    |
|    |       |      | test    | 10k mosaic from 10k testing  | 19.51 | 79.10 | 0.42 | 0.97 | 0 |    |
| 2. | 0,1,2 | run2 | trained | 30k mosaic from 50k training | 99.45 | 0 | 0.54 | 0 | 29031 | 19 |
|    |       |      | test    | 10k mosaic from 50k training | 99.58 | 0  | 0.42 | 0 | 9656 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 99.24 | 0 | 0.76 | 0  | 9681 |  |
| 3. | 0,1,2 | run3 | trained | 30k mosaic from 50k training | 99.58 | 0.003  | 0.41 | 0 | 29998 | 17 |
|    |       |      | test    | 10k mosaic from 50k training | 99.33 | 0  | 0.67 | 0 | 9999 |  |
|    |       |      | test    |  10k mosaic from 10k testing |  |    0  | 0.99 | 0    | 9999 |  |
| 4. | 1,2,3 | run1 | trained | 30k mosaic from 50k training | 15.64 | 83.27 | 0.27 | 0.81 | 0    | 21 |
|    |       |      | test    | 10k mosaic from 50k training | 15.38 | 83.38 | 0.34 | 0.9 | 0 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 15.83 | 82.75 | 0.42 | 1 | 0 |  |
| 5. | 1,2,3 | run2 | trained | 30k mosaic from 50k training | 99.50 | 0 | 0.49 | 0 | 29566 | 20 |
|    |       |      | test    | 10k mosaic from 50k training | 99.41 | 0 | 0.59 | 0 | 9853 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 99.4 | 0 | 0.6 | 0 | 9883 |  |
| 6. | 1,2,3 | run3 | trained | 30k mosaic from 50k training | 14.25 | 84.17 | 0.15 | 1.42 | 0 | 27 |
|    |       |      | test    | 10k mosaic from 50k training | 13.54 | 84.97 | 0.13 | 1.36 | 0 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 14.63 | 83.17 | 0.29 | 1.91 | 0 |  |

## Table 1 gamma = 0.06 for Experiment 1:
    
|Sno.|FG classes| #run | train/ test | on Dataset | FTPT | FFPT | FTPF | FFPF | alpha>0.5 | Epochs req for training|
|----|----------|------|----|------|------|-----|------|--------------|--------------|---------|
| 1. | 0,1,2 | run1 | trained | 30k mosaic from 50k training | 85.44 | 14.3 | 0.25 | 0.01 | 23172 | 26 |
|    |       |      | test    | 10k mosaic from 50k training | 85.63 | 14.02 | 0.34 | 0.01 | 7784 |    |
|    |       |      | test    | 10k mosaic from 10k testing  | 85.33 | 13.88 | 0.79 | 0 |7730 |    |
| 2. | 0,1,2 | run2 | trained | 30k mosaic from 50k training | 91.28 | 7.82 | 0.9 | 0 | 21680 | 24 |
|    |       |      | test    | 10k mosaic from 50k training | 91.38 | 7.56  | 1.06 | 0 | 7215 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 90.46 | 8.21  | 1.33 | 0    | 7269 |  |
| 3. | 0,1,2 | run3 | trained | 30k mosaic from 50k training | 71.84 | 27.21  | 0.89 | 0.05 | 20 | 28 |
|    |       |      | test    | 10k mosaic from 50k training | 72.87 | 26.14  | 0.93 | 0.06 | 7 |  |
|    |       |      | test    |  10k mosaic from 10k testing | 71.52 |  27.7    | 0.75 | 0.73    | 7 |  |
| 4. | 1,2,3 | run1 | trained | 30k mosaic from 50k training | 14.52 | 84.52 | 0.20 | 0.75 | 0    | 29 |
|    |       |      | test    | 10k mosaic from 50k training | 14.83 | 84.08 | 0.24 | 0.85 | 0 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 15.14 | 83.22 | 0.33 | 1.31 | 0 |  |
| 5. | 1,2,3 | run2 | trained | 30k mosaic from 50k training | 13.18 | 85.74 | 0.16 | 0.90 | 0 | 33 |
|    |       |      | test    | 10k mosaic from 50k training | 13.13 | 85.47 | 0.25 | 1.15 | 0 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 13 | 85.45 | 0.27 | 1.28 | 0 |  |
| 6. | 1,2,3 | run3 | trained | 30k mosaic from 50k training | 15.93 | 83.47 | 0.13 | 0.47 | 0 | 33 |
|    |       |      | test    | 10k mosaic from 50k training | 15.31 | 83.76 | 0.19 | 0.74 | 0 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 16.45 | 82.23 | 0.25 | 1.07 | 0 |  |

## Table 1 gamma = 0.18 for Experiment 1:
    
|Sno.|FG classes| #run | train/ test | on Dataset | FTPT | FFPT | FTPF | FFPF | alpha>0.5 | Epochs req for training|
|----|----------|------|----|------|------|-----|------|--------------|--------------|---------|
| 1. | 0,1,2 | run1 | trained | 30k mosaic from 50k training | 89.36 | 9.91 | 0.70 | 0.01 | 0 | 18 |
|    |       |      | test    | 10k mosaic from 50k training | 89.19 | 10.15 | 0.65 | 0.01 | 0 |    |
|    |       |      | test    | 10k mosaic from 10k testing  | 88.95 | 10.31 | 0.69 | 0.05 | 0 |    |
| 2. | 0,1,2 | run2 | trained | 30k mosaic from 50k training | 44.04 | 54.79 | 0.54 | 0.62 | 0 | 23 |
|    |       |      | test    | 10k mosaic from 50k training | 43.97 | 54.8  | 0.7 | 0.53 | 0 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 43.63 | 55.26  | 0.49 | 0.62  | 0 |  |
| 3. | 0,1,2 | run3 | trained | 30k mosaic from 50k training | 95.73 | 3.14  | 0.98 | 0.14 | 6398 | 18 |
|    |       |      | test    | 10k mosaic from 50k training | 95.81 | 2.84  | 1.14 | 0.21 | 2157 |  |
|    |       |      | test    |  10k mosaic from 10k testing | 95.64 |  3.25   | 1.02 | 0.09    | 2109 |  |
| 4. | 1,2,3 | run1 | trained | 30k mosaic from 50k training | 97.67 | 1.77 | 0.55 | 0 | 18405    | 18 |
|    |       |      | test    | 10k mosaic from 50k training | 97.99 | 1.51 | 0.5 | 0 | 6105 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 97.54 | 1.57 | 0.88 | 0.01 | 6001 |  |
| 5. | 1,2,3 | run2 | trained | 30k mosaic from 50k training | 97.83 | 1.47 | 0.63 | 0.063 | 0 | 29 |
|    |       |      | test    | 10k mosaic from 50k training | 97.58 | 1.65 | 0.65 | 0.12 | 0 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 97.86 | 1.24 | 0.75 | 0.15 | 0 |  |
| 6. | 1,2,3 | run3 | trained | 30k mosaic from 50k training | 98.62 | 0.88 | 0.49 | 0 | 93 | 23 |
|    |       |      | test    | 10k mosaic from 50k training | 98.64 | 0.78 | 0.57 | 0.01 | 32 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 98.27 | 0.95 | 0.78 | 0 | 20 |  |
## Experiment 2 setup:
1. In CIFAR 10 Dataset (shape: 50000x32x32x3), Reshape it to Matrix A : 50000x3072 then apply SVD on A to get the USV^T, Where V is Orthogonal vectors in row space(A).
2. Consider any 3 row vectors in V^T (or any 3 column vectors in V) which have some significant variance. (I considered 1069,1070,1071)
3. Let these 3 vectors be u1,u2,u3. Now consider Foregorund classes as fg1,fg2,fg3 out of 10 classes of CIFAR 10.
4. Update the Train and Test Dataset as following:

    for all img in CIFAR10 s.t label(img) == fg1 , img = img + 0.1 * |img| * u1  ; 
    
    for all img in CIFAR10 s.t label(img) == fg2 , img = img + 0.1 * |img| * u2  ; 
    
    for all img in CIFAR10 s.t label(img) == fg3 , img = img + 0.1 * |img| * u3  ; 
    
5. Now Create the Train Mosaic Dataset from updated Train CIFAR10 Dataset and Test Mosaic Dataset from updated Test CIFAR10 Dataset.
6. Train on this training Mosaic dataset and report the FTPT, FFPT, FTPF, FFPF on train and test mosaic dataset.

## Observation table for Experiment 2:
    
|Sno.|FG classes| #run | train/ test | on Dataset | FTPT | FFPT | FTPF | FFPF | alpha>0.5 | Epochs req for training|
|----|----------|------|----|------|------|-----|------|--------------|--------------|---------|
| 1. | 0,1,2 | run1 | trained | 30k mosaic from 50k training | 99.4 | 0.27 | 0.28 | 0.05 | 29908 | 23 |
|    |       |      | test    | 10k mosaic from 50k training | 99.34 | 0.21 | 0.38 | 0.07 | 9970 |    |
|    |       |      | test    | 10k mosaic from 10k testing  | 99 | 0.28 | 0.63 | 0.09 | 9979 |    |
| 2. | 0,1,2 | run2 | trained | 30k mosaic from 50k training | 98.98 | 0.52 | 0.38 | 0.11 | 29887 | 22 |
|    |       |      | test    | 10k mosaic from 50k training | 98.89 | 0.49  | 0.49 | 0.13 | 9961 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 98.96 | 0.46  | 0.55 | 0.03 | 9958 |  |
| 3. | 1,2,3 | run1 | trained | 30k mosaic from 50k training | 99.52 | 0.09  | 0.37 | 0.02 | 29964 | 43 |
|    |       |      | test    | 10k mosaic from 50k training | 99.6 | 0.05  | 0.33 | 0.02 | 9995 |  |
|    |       |      | test    |  10k mosaic from 10k testing | 98.95 |  0.11    | 0.94 | 0    | 9990 |  |
| 4. | 1,2,3 | run2 | trained | 30k mosaic from 50k training | 99.44  | 0.34 | 0.19 | 0.03 | 27247    | 55 |
|    |       |      | test    | 10k mosaic from 50k training | 99.23 | 0.37 | 0.39 | 0.01 | 9064    |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 98.46 | 0.35 | 1.18 | 0.01 | 9102    |  |
| 5. | 2,3,4 | run1 | trained | 30k mosaic from 50k training | 81.37 | 18.34 | 0.27 | 0.02 | 1373    | 48 |
|    |       |      | test    | 10k mosaic from 50k training | 81.8 | 17.57 | 0.58 | 0.05 | 468 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 81.9 | 17.1 | 0.98 | 0.02 | 463 |  |
| 6. | 2,3,4 | run2 | trained | 30k mosaic from 50k training | 49.32 | 49.73 | 0.84 | 0.11 | 226 | 39 |
|    |       |      | test    | 10k mosaic from 50k training | 48.82 | 50.27 | 0.76 | 0.15 | 75 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 50.38 | 48.68 | 0.8 | 0.14 | 100 |  |
| 7. | 2,3,4 | run3 | trained | 30k mosaic from 50k training | 97.87 | 1.73 | 0.40 | 0.003 | 5714 | 58 |
|    |       |      | test    | 10k mosaic from 50k training | 97.84 | 1.6 | 0.56 | 0 | 1874 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 97.42 | 1.79 | 0.79 | 0 | 1856 |  |
| 8. | 3,4,5 | run1 | trained | 30k mosaic from 50k training | 98.1 | 1.39 | 0.45 |  0.06  | 15587 | 29 |
|    |       |      | test    | 10k mosaic from 50k training | 97.93 | 1.32 | 0.71 |  0.04 | 5214 |    |
|    |       |      | test    | 10k mosaic from 10k testing  | 97.64 | 1.3 | 0.94 |  0.12  | 5265 |    |
| 9. | 3,4,5 | run2 | trained | 30k mosaic from 50k training | 98.4 | 1.41 | 0.17 | 0.01 | 15013 | 36 |
|    |       |      | test    | 10k mosaic from 50k training | 98.31 | 1.33 | 0.34 | 0.02 | 5011 |  |
|    |       |      | test    | 10k mosaic from 10k testing  | 97.79 | 1.3 | 0.86 | 0.02 | 4972 |  |
     
## Experiment 3 : It was accidently performed due to a mistake while performing Experiment 1 setup:
1. In CIFAR 10 Dataset (shape: 50000x32x32x3), Reshape it to Matrix A : 50000x3072 then apply SVD on A to get the USV^T, Where V is Orthogonal vectors in row space(A).
2. Consider the last 3 row vectors in V^T (or last 3 column vectors in V) which have least variance (as S has eigen values in descending order).

    MISTAKE : Instead of taking last 3 columns vectors in V, I took last 3 rows of V as u1, u2, u3. 

    u1 = <3069th component of every column vector> ,

    u2 = <3070th component of every column vector> and 

    u3 = <3071th component of every column vector>

3. Let these 3 vectors be u1,u2,u3. Now consider Foregorund classes as fg1,fg2,fg3 out of 10 classes of CIFAR 10.
4. Update the Train and Test Dataset as following:

    for all img in CIFAR10 s.t label(img) == fg1 , img = img + 0.1 * |img| * u1  ; 
    
    for all img in CIFAR10 s.t label(img) == fg2 , img = img + 0.1 * |img| * u2  ; 
    
    for all img in CIFAR10 s.t label(img) == fg3 , img = img + 0.1 * |img| * u3  ; 
    
5. Now Create the Train Mosaic Dataset from updated Train CIFAR10 Dataset and Test Mosaic Dataset from updated Test CIFAR10 Dataset.
6. Train on this training Mosaic dataset and report the FTPT, FFPT, FTPF, FFPF on train and test mosaic dataset.

## Observation table for Experiment 3:
    
|Sno.|FG classes| #run | train/ test | on Dataset | FTPT | FFPT | FTPF | FFPF | alpha>0.5 | Epochs req for training|
|----|----------|------|----|------|------|-----|------|--------------|--------------|---------|
| 1. | 0,1,2 | any  | trained | 30k mosaic from 50k training | 99.61 | 0.01 | 0.38 | 0.003 | 30000 | 18 |
|    |       |      | test    | 10k mosaic from 50k training | 99.26 | 0 | 0.73 | 0.01 | 9999 |    |
| 2. | 1,2,3 | any  | trained | 30k mosaic from 50k training | 99.59 | 0.01 | 0.393 | 0.01 | 30000 | 27 |
|    |       |      | test    | 10k mosaic from 50k training | 99.29 | 0.01  | 0.7 | 0 | 10000 |  |
| 3. | 2,3,4 | any  | trained | 30k mosaic from 50k training | 99.51 | 0.393  | 0.1 | 0 | 27334 | 43 |
|    |       |      | test    | 10k mosaic from 50k training | 99.09 | 0.44  | 0.47 | 0 | 9085 |  |
| 4. | 3,4,5 | any  | trained | 30k mosaic from 50k training | 99.47  | 0.01 | 0.51 | 0.01 | 29994    | 37 |
|    |       |      | test    | 10k mosaic from 50k training | 99.1 | 0.01 | 0.88 | 0.01 | 9996    |  |

Here we observed that in any run, we are getting FTPT >= 99 by just involving one dimension of every column vector in fg img.

Earlier we have never seen this much FTPT performance. Why this is happening? I have no clue about it!
