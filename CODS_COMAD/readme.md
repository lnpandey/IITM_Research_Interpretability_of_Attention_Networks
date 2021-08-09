
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

### Table 3: SDC task on MNIST Data

MLP1 is 1 hidden layer with 64 neurons with ReLU activation.

| Dataset | focus mlp1 classify linear  | focus mlp1 classify mlp1 |
| -------------------------- |  ---------------------------  |----------------------- |
| MNIST  | <img src= ./plots/SDC/mnist/mlp1_linear/mnist_test.png width="450"> | <img src= ./plots/SDC/mnist/mlp1_mlp1/mnist_test.png width="450"> |


### Table 4: SIN and CIN on MNIST and CIFAR

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
