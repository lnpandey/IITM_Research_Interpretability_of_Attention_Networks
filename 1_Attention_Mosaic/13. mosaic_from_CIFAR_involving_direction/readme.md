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
