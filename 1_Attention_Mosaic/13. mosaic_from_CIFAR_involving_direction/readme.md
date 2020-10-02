## Experiment 1 setup:
1. In CIFAR 10 Dataset (shape: 50000x32x32x3), Reshape it to Matrix A : 50000x3072 then apply SVD on A to get the USV^T, Where V is Orthogonal vectors in row space(A).
2. Consider the last 3 row vectors in V^T (or last 3 column vectors in V) which have least variance (as S has eigen values in descending order).
3. Let these 3 vectors be u1,u2,u3. Now consider Foregorund classes as fg1,fg2,fg3 out of 10 classes of CIFAR 10.
4. Update the Train and Test Dataset as following:

    for all img in CIFAR10 s.t label(img) == fg1 , img = img + 0.1 * |img| * u1  ; 
    
    for all img in CIFAR10 s.t label(img) == fg2 , img = img + 0.1 * |img| * u2  ; 
    
    for all img in CIFAR10 s.t label(img) == fg3 , img = img + 0.1 * |img| * u3  ; 
    
5. Now Create the Train Mosaic Dataset from updated Train CIFAR10 Dataset and Test Mosaic Dataset from updated Test CIFAR10 Dataset.
6. Train on this training Mosaic dataset and report the FTPT, FFPT, FTPF, FFPF on train and test mosaic dataset.

## Observation table for Experiment 1:
    
|Sno.|FG classes| #run | train/ test | on Dataset | FTPT | FFPT | FTPF | FFPF | alpha>0.5 | Epochs req for training|
|----|----------|------|----|------|------|-----|------|--------------|--------------|---------|
| 1. | 0,1,2 | run1| trained |30k mosaic from 50k training | 27.21 | 71.59 | 0.31 | 0.89 | 0 | 27 |
|  |  | | test |10k mosaic from 50k training | 26.33 | 72.63 | 0.25 | 0.79 | 0 |  |
|  |  | | test |10k mosaic from 10k testing | 26.48 | 72.33 | 0.41 | 0.78 | 0 |  |
| 2. | 0,1,2 | run2| trained |30k mosaic from 50k training | 59.97 | 39.31 | 0.69 | 0.02 | 221 | 29 |
|  |  | | test |10k mosaic from 50k training | 59.64 | 39.6 | 0.71 | 0.05 | 78 |  |
|  |  | | test |10k mosaic from 10k testing | 59.81 | 38.7 | 1.49 | 0 | 109 |  |
| 3. | 0,1,2 | run3| trained |30k mosaic from 50k training | 99.44 | 0.03 | 0.51 | 0.01 | 29989 | 27 |
|  |  | | test |10k mosaic from 50k training | 99.45 | 0.01 | 0.53 | 0.01 | 9998 |  |
|  |  | | test |10k mosaic from 10k testing | 99.22 |  0| 0.78 | 0 | 9997 |  |
| 4. | 1,2,3 | run1| trained |30k mosaic from 50k training | 16.24 | 82.72 | 0.33 | 0.70 | 0 | 23 |
|  |  | | test |10k mosaic from 50k training | 16.33 | 82.59 | 0.36 | 0.72 | 0 |  |
|  |  | | test |10k mosaic from 10k testing | 16.52 | 82.17 | 0.52 | 0.79 | 0 |  |
| 5. | 1,2,3 | run2| trained |30k mosaic from 50k training | 11.79 | 87.3 | 0.13 | 0.77 | 0 | 19 |
|  |  | | test |10k mosaic from 50k training | 12.42 | 86.68 | 0.15 | 0.75 | 0 |  |
|  |  | | test |10k mosaic from 10k testing | 11.8 | 86.81 | 0.16 | 1.23 | 0 |  |
| 6. | 1,2,3 | run3| trained |30k mosaic from 50k training | 98.94 | 0.3 | 0.75 | 0.01 | 3440 | 29 |
|  |  | | test |10k mosaic from 50k training | 98.88 | 0.24 | 0.87 | 0.01 | 1112 |  |
|  |  | | test |10k mosaic from 10k testing | 98.7 | 0.17 | 1.12 | 0.01 | 1047 |  |
| 7. | 2,3,4 | run1| trained |30k mosaic from 50k training | 48.01 | 50.89 | 0.87 | 0.24 | 0 | 30 |
|  |  | | test |10k mosaic from 50k training | 47.54 | 51.11 | 1.04 | 0.31 | 0 |  |
|  |  | | test |10k mosaic from 10k testing | 49.17 | 49.13 | 1.21 | 0.49 | 0 |  |
| 8. | 2,3,4  | run2| trained |30k mosaic from 50k training | 18.85 | 79.46 | 0.39 | 1.3 | 0 | 33 |
|  |  | | test |10k mosaic from 50k training | 18.94 | 79.01 | 0.5 | 1.55 | 0 |  |
|  |  | | test |10k mosaic from 10k testing | 19.56 | 78.69 | 0.46 | 1.29 | 0 |  |
| 9. | 2,3,4  | run3| trained |30k mosaic from 50k training | 75.93 | 22.79 | 1.23 | 0.05 | 793 | 47 |
|  |  | | test |10k mosaic from 50k training | 75.8 | 22.83 | 1.3 | 0.07 | 296 |  |
|  |  | | test |10k mosaic from 10k testing | 75.69 | 23.03 | 1.24 | 0.04 | 277 |  |
| 10. | 3,4,5  | run1| trained |30k mosaic from 50k training | 23.19 | 75.97 | 0.20 | 0.62 | 0 | 26 |
|  |  | | test |10k mosaic from 50k training | 22.31 | 76.76 | 0.34 | 0.59 | 0 |  |
|  |  | | test |10k mosaic from 10k testing | 24.44 | 74.58 | 0.26 | 0.72 | 0 |  |
| 11. | 3,4,5 | run2| trained |30k mosaic from 50k training | 22.37 | 76.63 | 0.17 | 0.82 | 0 | 47 |
|  |  | | test |10k mosaic from 50k training | 21.96 | 77.09 | 0.27 | 0.68 | 0 |  |
|  |  | | test |10k mosaic from 10k testing | 23.17 | 76 | 0.16 | 0.67 | 0 |  |
| 12. | 3,4,5 | run3| trained |30k mosaic from 50k training | 17.7 | 81.25 | 0.09 | 0.96 | 0 | 36 |
|  |  | | test |10k mosaic from 50k training | 18.15 | 80.7 | 0.13 | 1.02 | 0 |  |
|  |  | | test |10k mosaic from 10k testing | 19.17 | 79.73 | 0.19 | 0.91 | 0 |  |
