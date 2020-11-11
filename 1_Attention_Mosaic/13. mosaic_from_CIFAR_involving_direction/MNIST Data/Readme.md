## Experiment 1 setup:
1. In MNIST Dataset (shape: 60000x28x28), Reshape it to Matrix A : 60000x784 then apply SVD on A to get the USV^T, Where V is Orthogonal vectors in row space(A).
2. Consider the last 3 row vectors in V^T (or last 3 column vectors in V) which have least variance (as S has eigen values in descending order).
3. Let these 3 vectors be u1,u2,u3. Now consider Foregorund classes as fg1,fg2,fg3 out of 10 classes of MNIST.
4. Update the Train and Test Dataset as following:

    for all img in MNIST s.t label(img) == fg1 , img = img + gamma * |img| * u1  ; 
    
    for all img in MNIST s.t label(img) == fg2 , img = img + gamma * |img| * u2  ; 
    
    for all img in MNIST s.t label(img) == fg3 , img = img + gamma * |img| * u3  ; 
    
5. Now Create the Train Mosaic Dataset from updated Train MNSIT Dataset and Test Mosaic Dataset from updated Test MNIST Dataset.
6. Train on this training Mosaic dataset and report the FTPT, FFPT, FTPF, FFPF on train and test mosaic dataset.

### training Performance for different gamma values
| gamma | Accuracy | FTPT | FFPT |
| -     |  -       | -    | -    |
| 0.0002 | 98.822 | 96.85 | 1.971 |
| 0.0004 | 98.8763 | 97.6423 | 1.234|
| 0.0008 | 98.9407 | 97.564 | 1.34067| 
| 0.0016 | 98.9123 | 97.3647 | 1.5476 |
| 0.0032 | 98.768 | 97.4623 | 1.30567|
| 0.005 | 98.8013 | 97.4247 | 1.376 |
|0.02  |  98.865 | 97.784 | 1.081 |
| 0.03 | 99.0153 |  97.8897|  1.12567|
| 0.04 | 99.0073 | 97.1403 | 1.867 |
| 0.05  | 99.1667 | 98.3233 | 0.8433 |


### test Performance for different gamma values
| gamma | Accuracy | FTPT | FFPT |
| -     |  -       | -    | -    |
| 0.0002 | 98.527 | 96.579 | 1.948 |
| 0.0004 | 98.658 | 97.476 | 1.182|
| 0.0008 | 98.675 | 97.329 | 1.346 | 
| 0.0016 | 98.387 | 96.602 | 1.785 |
| 0.0032 | 98.507 | 97.283 | 1.224 |
| 0.005 | 98.589 | 97.207 | 1.382 |
|0.02 | 98.777 | 97.625 | 1.152 |
| 0.03 | 98.859 | 97.718  | 1.141 |
| 0.04 | 98.835  96.879   1.956 |
| 0.05  | 98.96 | 98.04 | 0.92
