#### Alternate minimization

Performance Analysis
| every 'm' epoch | 1(classify-focus)  | 1(focus-classify ) | 20 (classify-focus) | 20(focus-classify) | Simultaneous  | 
|  ----           |  ---------         | --------           |  ------------       |  -----------       | -------       |
| training        |                    |                    |    93.1             |                    |           | 
| test            |                    |                    |     75.1            |                    |           |


#### Performance on CIFAR Data Foreground Classes After First 20 epochs of 20(classify-focus)
Training Accuracy - 57.31% 


##### training loss curve every 'm' epoch we alternate between what net and where net
 | every 'm' epoch   |   1 (classify-focus)  | 1 (focus-classify)  |  20 (classify-focus) | 20 (focus-classify) |
 | ---   |   ------- | --- |---|----|
 | train_loss_plot  |  <img src= ./plots/train_loss_every_1_plot.png width="400">   | <img src= ./plots/where_what_train_loss_every_1_plot.png width="400"> |  <img src= ./plots/train_loss_every_20_plot.png width="400"> | <img src= ./plots/where_what_train_loss_every_20_plot.JPG width="400"> |
 |  train_FTPT_Curve  |  <img src= ./plots/train_analysis_every_1.png width="400">  | <img src= ./plots/where_what_train_analysis_every_1.png width="400">  | <img src= ./plots/train_analysis_every_20.png width="400">  | <img src= ./plots/where_what_train_analysis_every_20.JPG width="400">  |
 |  test_FTPT_Curve   | <img src= ./plots/test_analysis_every_1.png width="400">    | <img src= ./plots/where_what_test_analysis_every_1.png width="400">   |<img src= ./plots/test_analysis_every_20.png width="400">   | <img src= ./plots/where_what_test_analysis_every_20.JPG width="400">   |



