In these Experiments We train classification models for SIN and CIN data with multiple fixed focus.

<!-- h<sub>&theta;</sub>(x) = &theta;<sub>o</sub> x + &theta;<sub>1</sub>x -->

- For Dataset 4 we consider n = 100 m =100
- For Dataset 5 we consider n = 100 m =100 
- For CIFAR data we consider n= 10k m = 5

|  | Dataset 4 (alpha' = alpha+0.01) | Dataset 5 (alpha' = alpha+0.01) | CIFAR (alpha' = alpha+0.1) | CIFAR (alpha' = alpha+0.01) |
| - | -----    | -------   | ---------------          | ------------ |
| SIN L<sub>h</sub>(&alpha;)   |    <img src= ./plots/SIN_dataset_4_train_loss.png width="300"> | <img src= ./plots/SIN_dataset_5_train_loss.png width="300"> | <img src= ./plots/SIN_cifar_loss_1.png width="300"> | <img src= ./plots/SIN_cifar_loss_2.png width="300"> |
| SIN L<sub>h</sub>(&alpha;) - L<sub>h</sub>(&alpha;')    |    <img src= ./plots/SIN_dataset_4_train-_loss_alpha.png width="300"> | <img src= ./plots/SIN_dataset_5_train-_loss_alpha.png width="300"> | <img src= ./plots/SIN_cifar_loss-loss_alpha_1.png width="300"> | <img src= ./plots/SIN_cifar_loss-loss_alpha_2.png width="300"> 
| CIN L<sub>h</sub>(&alpha;)    |    <img src= ./plots/CIN_dataset_4_train_loss.png width="300"> | <img src= ./plots/CIN_dataset_5_train_loss.png width="300"> | <img src= ./plots/CIN_cifar_loss_1.png width="300"> | <img src= ./plots/CIN_cifar_loss_2.png width="300"> |
| CIN L<sub>h</sub>(&alpha;) - L<sub>h</sub>(&alpha;')   |      <img src= ./plots/CIN_dataset_4_train-_loss_alpha.png width="300"> | <img src= ./plots/CIN_dataset_5_train-_loss_alpha.png width="300"> | <img src= ./plots/CIN_cifar_loss-loss_alpha_1.png width="300"> | <img src= ./plots/CIN_cifar_loss-loss_alpha_2.png width="300"> 
