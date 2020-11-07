###  counter example

## Experiment setup:
1. In CIFAR 10 Dataset (shape: 50000x32x32x3), Reshape it to Matrix A : 50000x3072 then apply SVD on A to get the USV^T, Where V is Orthogonal vectors in row space(A).
2. Consider the last 3 row vectors in V^T (or last 3 column vectors in V) which have least variance (as S has eigen values in descending order).
3. Let these 3 vectors be u1,u2,u3. Now consider Foregorund classes as fg1,fg2,fg3 out of 10 classes of CIFAR 10.
4. Update the Train and Test Dataset as following:

    for all img in CIFAR10 s.t label(img) == fg1 , img = img + gamma * |img| * u1  ; 
    
    for all img in CIFAR10 s.t label(img) == fg2 , img = img + gamma * |img| * u2  ; 
    
    for all img in CIFAR10 s.t label(img) == fg3 , img = img + gamma * |img| * u3  ; 
    
5. Now Create the Train Mosaic Dataset from updated Train CIFAR10 Dataset and Test Mosaic Dataset from updated Test CIFAR10 Dataset.
6. Train on this training Mosaic dataset and report the FTPT, FFPT, FTPF, FFPF on train and test mosaic dataset


Results for the above experiment is as follow:

### CIFAR10 Data

#### low variance
| - gamma value | 0 | 0.02 | 0.03 | 0.04 | 0.05 | 
| --            |-- | --   | ---- | ---- | ---- |
|               | <img src= ./plots_and_images/low_0.JPG width="800"> | <img src= ./plots_and_images/low_02.JPG width="800"> | <img src= ./plots_and_images/low_03.JPG width="800">  | <img src= ./plots_and_images/low_04.JPG width="800">  | <img src= ./plots_and_images/low_05.JPG width="800"> | 

#### high variance
| - gamma value | 0 | 0.02 | 0.03 | 0.04 | 0.05 | 
| --            |-- | --   | ---- | ---- | ---- |
|               | <img src= ./plots_and_images/low_0.JPG width="800"> | <img src= ./plots_and_images/high_02.JPG width="800"> | <img src= ./plots_and_images/high_03.JPG width="800">  | <img src= ./plots_and_images/high_04.JPG width="800">  | <img src= ./plots_and_images/high_05.JPG width="800"> | 

### MNIST Data
#### low variance
| - gamma value | 0 | 0.02 | 0.03 | 0.04 | 0.05 | 0.06 | 
| --            |-- | --   | ---- | ---- | ---- | ---- |
|               | <img src= plot_5.png width="800"> | <img src= plot_1.png width="800"> | <img src= plot_2.png width="800">  | <img src= plot_3.png width="800">  | <img src= plot_4.png width="800"> | <img src= plot_6.png width="800">  |

### Synthetic Data

K=5 NF=3 NB=7


<img src= plots_syn.png width="800">

| train\ test  | test on dataset 1 | test on dataset 2 | test on dataset 3 | test on dataset 4 | test on dataset 5 | test on dataset 6 | test on dataset 7 | test on dataset 8 | test on dataset 9|
|----------|-----|-----|-----|-----|-----|-----|-----|-----|----|
| train on dataset 1      | 41| 40 | 40 | 41 | 43 | 43 | 43 | 43 | 42 |
| train on dataset 2      | 39 | 43 | 44 | 44 | 44 | 45 | 45 | 45 | 44 |
| train on dataset 3      | 36 | 40 | 46 | 47 | 48 | 52 | 53 | 53 | 52 |     
| train on dataset 4      | 34 | 37 | 43 | 51 | 55 | 58 | 60 | 58 | 55 |
| train on dataset 5      | 34 | 36 | 40 | 48 | 56 | 63 | 66 | 67 | 65 |
| train on dataset 6      | 33 | 36 | 39 | 45 | 54 | 66 | 73 | 75 | 74 |
| train on dataset 7      | 33 | 35 | 37 | 41 | 49 | 62 | 78 | 86 | 84 |
| train on dataset 8      | 33 | 34 | 36 | 39 | 46 | 58 | 74 | 91 | 92 |
| train on dataset 9      | 32 | 35 | 38 | 41 | 47 | 59 | 71 | 85 | 99 |





