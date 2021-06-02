#### Alternate minimization

Performance Analysis
| every 'm' epoch | Train FTPT  | Train FFPT | Train FTPF | Train FFPF | Test FTPT  | Test FFPT | Test FTPF | Test FFPF | 3 class classification accuracy on cifar|
|  ----           |  ---------  |----------- |------------|---------   | --------   |  ---------|  -------- | -----     | ----------------------------------------|
| 1 (classify-focus)  | 69.79 | 27.36 | 0.36 | 2.47 | 62.44 | 18.19 | 3.81 | 15.56 | 81.34 | 
| 1 (focus-classify)  | 66.59 | 29.14 | 0.54 | 3.71 | 58.91 | 20.08 | 4.41 | 16.60 | 82.306|
| 20 (classify-focus) | 65.79 | 32.60 | 0.25 | 1.34 | 56.43 | 18.47 | 5.41 | 19.69 | 67.84 | 
| 20 (focus-classify) | 54.57 | 30.23 |	1.52 | 13.67| 49.55 |	21.26 |	4.15 |	25.04 | 83.44 | 
| Simultaneous train  | 65.96 | 29.13 | 0.58 | 4.31 | 58.84 |	20.14 |	4.39 |	16.63 | 82.75 |


##### training loss curve every 'm' epoch we alternate between what net and where net
 | every 'm' epoch   |  train_loss_plot |  train_FTPT_Curve | test_FTPT_Curve | 3 class classification on cifar |
 | ---   |   ------- | --- |---|----|
 | 1 (classify-focus)  | <img src= ./what_where_1/train_loss_every_1_plot.png width="400"> | <img src= ./what_where_1/train_analysis_every_1.png width="400"> | <img src= ./what_where_1/test_analysis_every_1.png width="400"> | <img src= ./what_where_1/cifar_classify_acc_every_1_plot.png width="400"> | 
 | 1 (focus-classify)  | <img src= ./where_what_1/train_loss_every_1_plot.png width="400"> | <img src= ./where_what_1/train_analysis_every_1.png width="400"> | <img src= ./where_what_1/test_analysis_every_1.png width="400"> | <img src= ./where_what_1/cifar_classify_acc_every_1_plot.png width="400"> |  
 | 20 (classify-focus) | <img src= ./what_where_20/train_loss_every_20_plot.png width="400"> | <img src= ./what_where_20/train_analysis_every_20.png width="400"> | <img src= ./what_where_20/test_analysis_every_20.png width="400"> | <img src= ./what_where_20/cifar_classify_acc_every_20_plot.png width="400"> | 
 | 20 (focus-classify) | <img src= ./where_what_20/train_loss_every_20_plot.png width="400"> | <img src= ./where_what_20/train_analysis_every_20.png width="400"> | <img src= ./where_what_20/test_analysis_every_20.png width="400"> | <img src= ./where_what_20/cifar_classify_acc_every_20_plot.png width="400"> |  
 | Simultaneous train  | <img src= ./where_what_simultaneous/train_loss_sim_plot.png width="400"> | <img src= ./where_what_simultaneous/train_analysis_sim.png width="400"> | <img src= ./where_what_simultaneous/test_analysis_sim.png width="400"> | <img src= ./where_what_simultaneous/cifar_classify_acc_sim_plot.png width="400"> |  
 

