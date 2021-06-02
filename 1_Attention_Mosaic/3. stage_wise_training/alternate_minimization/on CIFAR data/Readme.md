#### Alternate minimization

Performance Analysis
| every 'm' epoch | 1(classify-focus)  | 1(focus-classify ) | 20 (classify-focus) | 20(focus-classify) | Simultaneous  | 
|  ----           |  ---------         | --------           |  ------------       |  -----------       | -------       |
| training        |  97                |   92.9             |    93.1             |  87                | 97.9          | 
| test            |  79.9              |   72.4             |    75.1             |  71                | 78.9          |


#### Performance on CIFAR Data Foreground Classes After First 20 epochs of 20(classify-focus)
Training Accuracy - 57.31% 


##### training loss curve every 'm' epoch we alternate between what net and where net
 | every 'm' epoch   |  train_loss_plot |  train_FTPT_Curve | test_FTPT_Curve | 3 class classification on cifar |
 | ---   |   ------- | --- |---|----|
 | 1 (classify-focus)  | <img src= ./what_where_1/train_loss_every_1_plot.png width="400"> | <img src= ./what_where_1/train_analysis_every_1.png width="400"> | <img src= ./what_where_1/test_analysis_every_1.png width="400"> | <img src= ./what_where_1/cifar_classify_acc_every_1_plot.png width="400"> | 
 | 1 (focus-classify)  | <img src= ./where_what_1/train_loss_every_1_plot.png width="400"> | <img src= ./where_what_1/train_analysis_every_1.png width="400"> | <img src= ./where_what_1/test_analysis_every_1.png width="400"> | <img src= ./where_what_1/cifar_classify_acc_every_1_plot.png width="400"> |  
 | 20 (classify-focus) | <img src= ./what_where_20/train_loss_every_20_plot.png width="400"> | <img src= ./what_where_20/train_analysis_every_20.png width="400"> | <img src= ./what_where_20/test_analysis_every_20.png width="400"> | <img src= ./what_where_20/cifar_classify_acc_every_20_plot.png width="400"> | 
 | 20 (focus-classify) | <img src= ./where_what_20/train_loss_every_20_plot.png width="400"> | <img src= ./where_what_20/train_analysis_every_20.png width="400"> | <img src= ./where_what_20/test_analysis_every_20.png width="400"> | <img src= ./where_what_20/cifar_classify_acc_every_20_plot.png width="400"> |  
 | Simultaneous train  | <img src= ./where_what_simultaneous/train_loss_sim_plot.png width="400"> | <img src= ./where_what_simultaneous/train_analysis_sim.png width="400"> | <img src= ./where_what_simultaneous/test_analysis_sim.png width="400"> | <img src= ./where_what_simultaneous/cifar_classify_acc_sim_plot.png width="400"> |  
 

