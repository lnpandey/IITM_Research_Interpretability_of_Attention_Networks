#### Alternate minimization

Data distribution : Foreground Classes are in Convex Hull of Background Classes. Any 2 Foreground Classes are linearly separable.
<img src= type4_data.JPG width="450"> 



Performance Analysis
| every 'm' epoch | Train FTPT  | Train FFPT | Train FTPF | Train FFPF | Test FTPT  | Test FFPT | Test FTPF | Test FFPF | 3 class classification accuracy on cifar|
|  ----           |  ---------  |----------- |------------|---------   | --------   |  ---------|  -------- | -----     | ----------------------------------------|
| 1 (classify-focus)  | 69.16 | 30.43 | 0.3 | 0.1  | 67.95 | 31.1 | 0.75 | 0.2 | 71.45 | 
| 1 (focus-classify)  | 66.59 | 29.14 | 0.54 | 3.71 | 58.91 | 20.08 | 4.41 | 16.60 | 82.306|
| 20 (classify-focus) | 70.73  | 28.46 | 0.63 | 0.16 | 71.8 | 27.1 | 1.05 | 0.05 | 66.4 | 
| 20 (focus-classify) | 54.57 | 30.23 |	1.52 | 13.67| 49.55 |	21.26 |	4.15 |	25.04 | 83.44 | 
| Simultaneous train  | 75.96 | 23.56 | 0.4 | 0.06 | 76.75 |	22.1 |  1 |	 0.1 | - |


##### training loss curve every 'm' epoch we alternate between what net and where net
 | every 'm' epoch   |  train_loss_plot |  train_FTPT_Curve | test_FTPT_Curve | 3 class classification on cifar |
 | ---   |   ------- | --- |---|----|
 | 1 (classify-focus)  |<img src= ./what_where_type4/train_loss_every_1_plot.png width="400"> | <img src= ./what_where_type4/train_analysis_every_1.png width="400">  | <img src= ./what_where_type4/test_analysis_every_1.png width="400"> | <img src= ./what_where_type4/type4_classify_acc_every_1_plot.png width="400"> | 
| 1 (focus-classify)  | <img src= ./where_what_type4/train_loss_every_1_plot.png width="400"> | <img src= ./where_what_type4/train_analysis_every_1.png width="400">  | <img src= ./where_what_type4/test_analysis_every_1.png width="400"> | <img src= ./where_what_type4/type4_classify_acc_every_1_plot.png width="400"> |  
| 20 (classify-focus) | <img src= ./what_where_type4/train_loss_every_20_plot.png width="400"> | <img src= ./what_where_type4/train_analysis_every_20.png width="400"> | <img src= ./what_where_type4/test_analysis_every_20.png width="400"> | <img src= ./what_where_type4/type4_classify_acc_every_20_plot.png width="400"> | 
| 20 (focus-classify) | <img src= ./where_what_type4/train_loss_every_20_plot.png width="400"> | <img src= ./where_what_type4/train_analysis_every_20.png width="400">  | <img src= ./where_what_type4/test_analysis_every_20.png width="400">  | <img src= ./where_what_type4/type4_classify_acc_every_20_plot.png width="400"> |  
| Simultaneous train  | <img src= ./simultaneous_type4/train_loss_plot.png width="400"> | <img src= ./simultaneous_type4/train_analysis.png width="400"> | <img src= ./simultaneous_type4/test_analysis.png width="400"> | - |  







 
 
 Data distribution: Elliptical blobs 
 
 Performance Analysis
 
| every 'm' epoch | Train FTPT  | Train FFPT | Train FTPF | Train FFPF | Test FTPT  | Test FFPT | Test FTPF | Test FFPF | 3 class classification accuracy on cifar|
|  ----           |  ---------  |----------- |------------|---------   | --------   |  ---------|  -------- | -----     | ----------------------------------------|
| 1 (classify-focus)  | 69.79 | 27.36 | 0.36 | 2.47 | 62.44 | 18.19 | 3.81 | 15.56 | 81.34 | 
| 1 (focus-classify)  | 66.59 | 29.14 | 0.54 | 3.71 | 58.91 | 20.08 | 4.41 | 16.60 | 82.306|
| 20 (classify-focus) | 67.43 | 32.56 | 0 | 0 | 67.05 | 32.9 | 0.05 | 0 |97.53 | 
| 20 (focus-classify) | 54.57 | 30.23 |	1.52 | 13.67| 49.55 |	21.26 |	4.15 |	25.04 | 83.44 | 
| Simultaneous train  | 100 | 0 | 0 | 0 | 99.9 |	0 |	0.1 | 0  | - |


 ##### training loss curve every 'm' epoch we alternate between what net and where net
 | every 'm' epoch   |   1 (classify-focus)  | 1 (focus-classify)  |  20 (classify-focus) | 20 (focus-classify) |
 | ---   |   ------- | --- |---|----|
 | train_loss_plot   | <img src= ./what_where_blob/train_loss_every_1_plot.png width="400">   | <img src= ./where_what_blob/train_loss_every_1_plot.png width="400"> |  <img src= ./what_where_blob/train_loss_every_20_plot.png width="400"> | <img src= ./where_what_blob/train_loss_every_20_plot.png width="400"> |
 | train_FTPT_Curve  | <img src= ./what_where_blob/train_analysis_every_1.png width="400">  | <img src= ./where_what_blob/train_analysis_every_1.png width="400">  | <img src= ./what_where_blob/train_analysis_every_20.png width="400">  | <img src= ./where_what_blob/train_analysis_every_20.png width="400">  |
 | test_FTPT_Curve   | <img src= ./what_where_blob/test_analysis_every_1.png width="400">    | <img src= ./where_what_blob/test_analysis_every_1.png width="400">   |<img src= ./what_where_blob/test_analysis_every_20.png width="400">   | <img src= ./where_what_blob/test_analysis_every_20.png width="400">   |
 | What_Net_FG_Performance  | <img src= ./what_where_blob/blob_classify_acc_every_1_plot.png width="400">    | <img src= ./where_what_blob/blob_classify_acc_every_1_plot.png width="400">   |<img src= ./what_where_blob/blob_classify_acc_every_20_plot.png width="400">   | <img src= ./where_what_blob/blob_classify_acc_every_20_plot.png width="400">   |


##### training loss curve every 'm' epoch we alternate between what net and where net
 | every 'm' epoch   |  train_loss_plot |  train_FTPT_Curve | test_FTPT_Curve | 3 class classification on cifar |
 | ---   |   ------- | --- |---|----|
 | 1 (classify-focus)  |<img src= ./what_where_blob/train_loss_every_1_plot.png width="400"> | <img src= ./what_where_blob/train_analysis_every_1.png width="400">  | <img src= ./what_where_blob/test_analysis_every_1.png width="400"> | <img src= ./what_where_blob/blob_classify_acc_every_1_plot.png width="400"> | 
| 1 (focus-classify)  | <img src= ./where_what_blob/train_loss_every_1_plot.png width="400"> | <img src= ./where_what_blob/train_analysis_every_1.png width="400">  | <img src= ./where_what_blob/test_analysis_every_1.png width="400"> | <img src= ./where_what_blob/blob_classify_acc_every_1_plot.png width="400"> |  
| 20 (classify-focus) | <img src= ./what_where_blob/train_loss_every_20_plot.png width="400"> | <img src= ./what_where_blob/train_analysis_every_20.png width="400"> | <img src= ./what_where_blob/test_analysis_every_20.png width="400"> | <img src= ./what_where_blob/blob_classify_acc_every_20_plot.png width="400"> | 
| 20 (focus-classify) | <img src= ./where_what_blob/train_loss_every_20_plot.png width="400"> | <img src= ./where_what_blob/train_analysis_every_20.png width="400">  | <img src= ./where_what_blob/test_analysis_every_20.png width="400">  | <img src= ./where_what_blob/blob_classify_acc_every_20_plot.png width="400"> | 
| Simultaneous train  | <img src= ./simultaneous_blob/train_loss_plot.png width="400"> | <img src= ./simultaneous_blob/train_analysis.png width="400"> | <img src= ./simultaneous_blob/test_analysis.png width="400"> | - | 

 


