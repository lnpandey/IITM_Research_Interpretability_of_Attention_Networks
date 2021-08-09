
### Table 1: SDC task on Synthetic Datasets

MLP2 is 2 hidden layer with 50 and 10 neurons with ReLU activation.

| Dataset | focus linear classify linear  | focus linear classify mlp2  | focus mlp2 classify linear  | focus mlp2 classify mlp2 |
| - |     ------      |   --------------------------- |  ---------------------------  |----------------------- |
| <img src= ./plots/convex_instance_noise/ds1_data.png width="300">  | <img src= ./plots/SDC/t0_lin_lin.JPG width="650"> | <img src= ./plots/SDC/t0_lin_mlp2.JPG width="650"> |  <img src= ./plots/SDC/t0_mlp2_lin.JPG width="650"> | <img src= ./plots/SDC/t0_mlp2_mlp2.JPG width="650"> |
| <img src= ./plots/convex_instance_noise/ds2_data.png width="300">  | <img src= ./plots/SDC/t2_lin_lin.JPG width="650"> | <img src= ./plots/SDC/t2_lin_mlp2.JPG width="650"> |  <img src= ./plots/SDC/t2_mlp2_lin.JPG width="650"> | <img src= ./plots/SDC/t2_mlp2_mlp2.JPG width="650"> |
| <img src= ./plots/convex_instance_noise/ds3_data.png width="300">  | <img src= ./plots/SDC/t3_lin_lin.JPG width="650"> | <img src= ./plots/SDC/t3_lin_mlp2.JPG width="650"> |  <img src= ./plots/SDC/t3_mlp2_lin.JPG width="650"> | <img src= ./plots/SDC/t3_mlp2_mlp2.JPG width="650"> |
| <img src= ./plots/convex_instance_noise/ds4_data.png width="300">  | <img src= ./plots/SDC/t4_lin_lin.JPG width="650"> | <img src= ./plots/SDC/t4_lin_mlp2.JPG width="650"> |  <img src= ./plots/SDC/t4_mlp2_lin.JPG width="650"> | <img src= ./plots/SDC/t4_mlp2_mlp2.JPG width="650"> |

### Table 2: SDC task on Grid Data

MLP1 is 1 hidden layer with 64 neurons with ReLU activation.

| Dataset | focus linear classify linear  | focus linear classify mlp1  | focus mlp1 classify linear  | focus mlp1 classify mlp1 |
| - |     ------      |   --------------------------- |  ---------------------------  |----------------------- |
| <img src= ./plots/substitution_instance_noise/grid_data.JPG width="650">  | <img src= ./plots/SDC/gd_lin_lin.JPG width="650"> | <img src= ./plots/SDC/gd_lin_mlp1.JPG width="650"> |  <img src= ./plots/SDC/gd_mlp1_lin.JPG width="650"> | <img src= ./plots/SDC/gd_mlp1_mlp1.JPG width="650"> |

### Table 3.1: SDC task on MNIST Data

- fg_class = {0,1}, bg_class={2,3,4,5,6,7,8,9}
- image = ( image - bg_mean(bg_class) ) / abs(max(bg_class))
- from these images Mosaic data is formed with m=9.
- mosaic_train = mosaic_train - mean(mosaic_train)
- mosaic_test = mosaic_test - mean(mosaic_train)
- MLP1 is 1 hidden layer with 64 neurons with ReLU activation.
- Focus is functionnaly zero and no bias, Classification is initialised with Xavier_norm and bias with all zeros.

| Dataset | focus mlp1 classify linear  | focus mlp1 classify mlp1 |
| -------------------------- |  ---------------------------  |----------------------- |
| MNIST  | <img src= ./plots/SDC/mnist/mlp1_linear/mnist_test.png width="450"> | <img src= ./plots/SDC/mnist/mlp1_mlp1/mnist_test.png width="450"> |

### Table 3.2: SDC task on CIFAR Data

- fg_class = {0,1,2}, bg_class={3,4,5,6,7,8,9}
- image = ( image - bg_mean(bg_class) ) / std_dev(bg_class)
- from these images Mosaic data is formed with m=9.
- mosaic_train = ( mosaic_train - mean(mosaic_train) ) / std_dev(mosaic_train)
- mosaic_test = ( mosaic_test - mean(mosaic_train) ) / std_dev(mosaic_train)
- CNN-3 : conv1(32,3)-conv2(64,3)-conv3(64,3)-fc(512)-fc(64)-fc(10)
- CNN-2 : conv1(6,5)-conv2(16,5)-fc(120)-fc(84)-fc(10)
- Focus is functionnaly zero and no bias, Classification is initialised with Xavier_norm and bias with all zeros.

| Dataset | focus CNN-3 classify CNN-2 Train  | focus CNN-3 classify CNN-2 Test |  focus CNN-3 classify CNN-3 Train  | focus CNN-3 classify CNN-3 Test |
| -------------------------- |  ---------------------------  |----------------------- |-------|----------|
| CIFAR  | <img src= ./plots/SDC/cifar/cnn3_cnn2/cifar_train.png width="350"> | <img src= ./plots/SDC/cifar/cnn3_cnn2/cifar_test.png width="350">  | <img src= ./plots/SDC/cifar/cnn3_cnn3/cifar_train.png width="350"> | <img src= ./plots/SDC/cifar/cnn3_cnn3/cifar_test.png width="350"> |


### Table 4: SIN and CIN on MNIST and CIFAR
- Mosaic creation from CIFAR and MNIST is same as mentioned in Table 3.1 and 3.2
- From mosaic data, CIN data is created with different alpha values.
- MLP1 is 1 hidden layer with 64 neurons with ReLU activation.
- CNN-2 : conv1(6,5)-conv2(16,5)-fc(120)-fc(84)-fc(10)
- Mini-Inception-8 is having 8 inception layer
- Mini-Inception-3 is having 3 inception layer

| Dataset | convex_instance_noise  | substitution_instance_noise |
| -------------------------- |  ---------------------------  |----------------------- |
| MNIST  | <img src= ./plots/convex_instance_noise/mnist.png width="350"> | <img src= ./plots/substitution_instance_noise/mnist.png width="350"> |
| CIFAR  | <img src= ./plots/convex_instance_noise/cifar.png width="350"> | <img src= ./plots/substitution_instance_noise/cifar.png width="350"> |

### Table 5: CIN on Synthetic Data

| Dataset | convex_instance_noise  | 
| -------------------------- |  ---------------------------  |
| <img src= ./plots/convex_instance_noise/ds1_data.png width="300">  | <img src= ./plots/convex_instance_noise/ds1_cin.png width="300"> | 
| <img src= ./plots/convex_instance_noise/ds2_data.png width="300">  | <img src= ./plots/convex_instance_noise/ds2_cin.png width="300"> | 
| <img src= ./plots/convex_instance_noise/ds3_data.png width="300">  | <img src= ./plots/convex_instance_noise/ds3_cin.png width="300"> | 
| <img src= ./plots/convex_instance_noise/ds4_data.png width="300">  | <img src= ./plots/convex_instance_noise/ds4_cin.png width="300"> | 
