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

Here we have considered gamma value as 1.

Results for the above experiment is as follow:

<img src= counter_example.png width="800">

gamma value = 0.5 

<img src= plot_low_var_512.png width="800">

for high variance eigen vectors with gamma value 0.5
<img src= plot_high_var.png width="800">

### MNIST Data

gamma value = 0.5
<img src= plot_mnist.png width="800">
