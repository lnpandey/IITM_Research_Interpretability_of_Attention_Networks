In these Experiments We train classification models for SIN and CIN data with multiple fixed focus.

<!-- h<sub>&theta;</sub>(x) = &theta;<sub>o</sub> x + &theta;<sub>1</sub>x -->

- For Dataset 4 we consider n = 100 m =100
- For Dataset 5 we consider n = 100 m =100 
- For CIFAR data we consider n= 10k m = 5 
- For CIFAR Dataset 1 is for &alpha; = 0.2, Dataset 2 is for &alpha; = 0.4, Dataset 3 is for &alpha;= 0.6, Dataset 4 is for &alpha; = 0.8 and Dataset 5 is for &alpha; = 1. 
- For Dataset 4 and Dataset 5, legends show the &alpha; value
- directions starts from [1,0] and move in anti-clockwise direction at angle of 45 degrees

|  | Dataset 4 (&alpha;' = &alpha;+0.01) | Dataset 5 (&alpha;' = &alpha;+0.01) | CIFAR (&alpha;' = &alpha;+0.1) | CIFAR (&alpha;' = &alpha;+0.01) |
| - | -----    | -------   | ---------------          | ------------ |
| SIN L<sub>h</sub>(&alpha;)   |    <img src= ./plots/SIN_dataset_4_train_loss.png width="300"> | <img src= ./plots/SIN_dataset_5_train_loss.png width="300"> | <img src= ./plots/SIN_cifar_loss_1.png width="300"> | <img src= ./plots/SIN_cifar_loss_2.png width="300"> |
| SIN L<sub>h</sub>(&alpha;) - L<sub>h</sub>(&alpha;')    |    <img src= ./plots/SIN_dataset_4_train-_loss_alpha.png width="300"> | <img src= ./plots/SIN_dataset_5_train-_loss_alpha.png width="300"> | <img src= ./plots/SIN_cifar_loss-loss_alpha_1.png width="300"> | <img src= ./plots/SIN_cifar_loss-loss_alpha_2.png width="300"> 
| CIN L<sub>h</sub>(&alpha;)    |    <img src= ./plots/CIN_dataset_4_train_loss.png width="300"> | <img src= ./plots/CIN_dataset_5_train_loss.png width="300"> | <img src= ./plots/CIN_cifar_loss_1.png width="300"> | <img src= ./plots/CIN_cifar_loss_2.png width="300"> |
| CIN L<sub>h</sub>(&alpha;) - L<sub>h</sub>(&alpha;')   |      <img src= ./plots/CIN_dataset_4_train-_loss_alpha.png width="300"> | <img src= ./plots/CIN_dataset_5_train-_loss_alpha.png width="300"> | <img src= ./plots/CIN_cifar_loss-loss_alpha_1.png width="300"> | <img src= ./plots/CIN_cifar_loss-loss_alpha_2.png width="300"> 


### Dataset 6

<img src= ./plots/base_data.png width="300">

- Soft attention Performance(train[FTPT,FFPT,FFPT,FFPF], test[FTPT,FFPT,FFPT,FFPF]) - ([66, 34, 0, 0], [645, 355, 0, 0]) 
- Hard attention Performance(train[FTPT,FFPT,FFPT,FFPF], test[FTPT,FFPT,FFPT,FFPF]) - ([100, 0, 0, 0], [1000, 0, 0, 0])

#### plot 1A m value 100 size 100
| |  CIN    |  SIN |
| -----  | ----    | ---- |
| loss curve | <img src= ./plots/cin_train_loss_1.png width="300">|   <img src= ./plots/sin_train_loss_1.png width="300"> |
| beta 0 | <img src= ./plots/cin_train_loss_1_loss_beta_0.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_0.png width="300"> |
| beta 0.01 | <img src= ./plots/cin_train_loss_1_loss_beta_1.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_1.png width="300"> |
| beta 0.08 | <img src= ./plots/cin_train_loss_1_loss_beta_4.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_4.png width="300"> |
| beta 0.32 | <img src= ./plots/cin_train_loss_1_loss_beta_6.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_6.png width="300"> |
| beta 0.5  | <img src= ./plots/cin_train_loss_1_loss_beta_7.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_7.png width="300"> |
| beta 1    | <img src= ./plots/cin_train_loss_1_loss_beta_9.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_9.png width="300"> |
| beta 2.56 | <img src= ./plots/cin_train_loss_1_loss_beta_11.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_11.png width="300"> |


- Soft attention Performance(train[FTPT,FFPT,FFPT,FFPF], test[FTPT,FFPT,FFPT,FFPF]) - ([500, 0, 0, 0], [1000, 0, 0, 0])
- Hard attention Performance(train[FTPT,FFPT,FFPT,FFPF], test[FTPT,FFPT,FFPT,FFPF]) - ([500, 0, 0, 0], [1000, 0, 0, 0])

#### plot 1B m value 100 size 500
| |  CIN    |  SIN |
| -----  | ----    | ---- |
| loss curve | <img src= ./plots/cin_train_loss_2.png width="300">|   <img src= ./plots/sin_train_loss_2.png width="300"> |
| beta 0 | <img src= ./plots/cin_train_loss_2_loss_beta_0.png width="300"> | <img src= ./plots/sin_train_loss_2_loss_beta_0.png width="300"> |
| beta 0.01 | <img src= ./plots/cin_train_loss_2_loss_beta_1.png width="300"> | <img src= ./plots/sin_train_loss_2_loss_beta_1.png width="300"> |
| beta 0.08 | <img src= ./plots/cin_train_loss_2_loss_beta_4.png width="300"> | <img src= ./plots/sin_train_loss_2_loss_beta_4.png width="300"> |
| beta 0.32 | <img src= ./plots/cin_train_loss_2_loss_beta_6.png width="300"> | <img src= ./plots/sin_train_loss_2_loss_beta_6.png width="300"> |
| beta 0.5  | <img src= ./plots/cin_train_loss_2_loss_beta_7.png width="300"> | <img src= ./plots/sin_train_loss_2_loss_beta_7.png width="300"> |
| beta 1    | <img src= ./plots/cin_train_loss_2_loss_beta_9.png width="300"> | <img src= ./plots/sin_train_loss_2_loss_beta_9.png width="300"> |
| beta 2.56 | <img src= ./plots/cin_train_loss_2_loss_beta_11.png width="300"> | <img src= ./plots/sin_train_loss_2_loss_beta_11.png width="300"> |



- Soft attention Performance(train[FTPT,FFPT,FFPT,FFPF], test[FTPT,FFPT,FFPT,FFPF]) - ([0, 43, 0, 57], [0, 323, 0, 677]) 
- Hard attention Performance(train[FTPT,FFPT,FFPT,FFPF], test[FTPT,FFPT,FFPT,FFPF]) - ([100, 0, 0, 0], [1000, 0, 0, 0])

#### plot 1C m value 500 size 100
| |  CIN    |  SIN |
| -----  | ----    | ---- |
| loss curve | <img src= ./plots/cin_train_loss_3.png width="300">|   <img src= ./plots/sin_train_loss_3.png width="300"> |
| beta 0 | <img src= ./plots/cin_train_loss_3_loss_beta_0.png width="300"> | <img src= ./plots/sin_train_loss_3_loss_beta_0.png width="300"> |
| beta 0.01 | <img src= ./plots/cin_train_loss_3_loss_beta_1.png width="300"> | <img src= ./plots/sin_train_loss_3_loss_beta_1.png width="300"> |
| beta 0.08 | <img src= ./plots/cin_train_loss_3_loss_beta_4.png width="300"> | <img src= ./plots/sin_train_loss_3_loss_beta_4.png width="300"> |
| beta 0.32 | <img src= ./plots/cin_train_loss_3_loss_beta_6.png width="300"> | <img src= ./plots/sin_train_loss_3_loss_beta_6.png width="300"> |
| beta 0.5  | <img src= ./plots/cin_train_loss_3_loss_beta_7.png width="300"> | <img src= ./plots/sin_train_loss_3_loss_beta_7.png width="300"> |
| beta 1    | <img src= ./plots/cin_train_loss_3_loss_beta_9.png width="300"> | <img src= ./plots/sin_train_loss_3_loss_beta_9.png width="300"> |
| beta 2.56 | <img src= ./plots/cin_train_loss_3_loss_beta_11.png width="300"> | <img src= ./plots/sin_train_loss_3_loss_beta_11.png width="300"> |



- Soft attention Performance(train[FTPT,FFPT,FFPT,FFPF], test[FTPT,FFPT,FFPT,FFPF]) - ([500, 0, 0, 0], [1000, 0, 0, 0])
- Hard attention Performance(train[FTPT,FFPT,FFPT,FFPF], test[FTPT,FFPT,FFPT,FFPF]) - ([500, 0, 0, 0], [1000, 0, 0, 0])

#### plot 1D m value 500 size 500
| |  CIN    |  SIN |
| -----  | ----    | ---- |
| loss curve | <img src= ./plots/cin_train_loss_4.png width="300">|   <img src= ./plots/sin_train_loss_4.png width="300"> |
| beta 0 | <img src= ./plots/cin_train_loss_4_loss_beta_0.png width="300"> | <img src= ./plots/sin_train_loss_4_loss_beta_0.png width="300"> |
| beta 0.01 | <img src= ./plots/cin_train_loss_4_loss_beta_1.png width="300"> | <img src= ./plots/sin_train_loss_4_loss_beta_1.png width="300"> |
| beta 0.08 | <img src= ./plots/cin_train_loss_4_loss_beta_4.png width="300"> | <img src= ./plots/sin_train_loss_4_loss_beta_4.png width="300"> |
| beta 0.32 | <img src= ./plots/cin_train_loss_4_loss_beta_6.png width="300"> | <img src= ./plots/sin_train_loss_4_loss_beta_6.png width="300"> |
| beta 0.5  | <img src= ./plots/cin_train_loss_4_loss_beta_7.png width="300"> | <img src= ./plots/sin_train_loss_4_loss_beta_7.png width="300"> |
| beta 1    | <img src= ./plots/cin_train_loss_4_loss_beta_9.png width="300"> | <img src= ./plots/sin_train_loss_4_loss_beta_9.png width="300"> |
| beta 2.56 | <img src= ./plots/cin_train_loss_4_loss_beta_11.png width="300"> | <img src= ./plots/sin_train_loss_4_loss_beta_11.png width="300"> |



<!-- | beta 0.02 | <img src= ./plots/cin_train_loss_1_loss_beta_2.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_2.png width="300"> |
| beta 0.04 | <img src= ./plots/cin_train_loss_1_loss_beta_3.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_3.png width="300"> |

| beta 0.16 | <img src= ./plots/cin_train_loss_1_loss_beta_5.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_5.png width="300"> |
| beta 0.64 | <img src= ./plots/cin_train_loss_1_loss_beta_8.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_8.png width="300"> |

| beta 1.28 | <img src= ./plots/cin_train_loss_1_loss_beta_10.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_10.png width="300"> |

| beta 5.12 | <img src= ./plots/cin_train_loss_1_loss_beta_12.png width="300"> | <img src= ./plots/sin_train_loss_1_loss_beta_12.png width="300"> | -->








