#### Alternate minimization

Data distribution : Foreground Classes are in Convex Hull of Background Classes. Any 2 Foreground Classes are linearly separable.
<img src= type4_data.JPG width="450"> 

##### training loss curve every 'm' epoch we alternate between what net and where net
 | every 'm' epoch   |   1 (classify-focus)  | 1 (focus-classify)  |  20 (classify-focus) | 20 (focus-classify) |
 | ---   |   ------- | --- |---|----|
 | train_loss_plot   | <img src= ./what_where/train_loss_every_1_plot.png width="400">   | <img src= ./where_what/train_loss_every_1_plot.png width="400"> |  <img src= ./what_where/train_loss_every_20_plot.png width="400"> | <img src= ./where_what/train_loss_every_20_plot.png width="400"> |
 | train_FTPT_Curve  | <img src= ./what_where/train_analysis_every_1.png width="400">  | <img src= ./where_what/train_analysis_every_1.png width="400">  | <img src= ./what_where/train_analysis_every_20.png width="400">  | <img src= ./where_what/train_analysis_every_20.png width="400">  |
 | test_FTPT_Curve   | <img src= ./what_where/test_analysis_every_1.png width="400">    | <img src= ./where_what/test_analysis_every_1.png width="400">   |<img src= ./what_where/test_analysis_every_20.png width="400">   | <img src= ./where_what/test_analysis_every_20.png width="400">   |
 
 
 Data distribution: Elliptical blobs 
 
 ##### training loss curve every 'm' epoch we alternate between what net and where net
 | every 'm' epoch   |   1 (classify-focus)  | 1 (focus-classify)  |  20 (classify-focus) | 20 (focus-classify) |
 | ---   |   ------- | --- |---|----|
 | train_loss_plot   | <img src= ./what_where_blob/train_loss_every_1_plot.png width="400">   | <img src= ./where_what_blob/train_loss_every_1_plot.png width="400"> |  <img src= ./what_where_blob/train_loss_every_20_plot.png width="400"> | <img src= ./where_what_blob/train_loss_every_20_plot.png width="400"> |
 | train_FTPT_Curve  | <img src= ./what_where_blob/train_analysis_every_1.png width="400">  | <img src= ./where_what_blob/train_analysis_every_1.png width="400">  | <img src= ./what_where_blob/train_analysis_every_20.png width="400">  | <img src= ./where_what_blob/train_analysis_every_20.png width="400">  |
 | test_FTPT_Curve   | <img src= ./what_where_blob/test_analysis_every_1.png width="400">    | <img src= ./where_what_blob/test_analysis_every_1.png width="400">   |<img src= ./what_where_blob/test_analysis_every_20.png width="400">   | <img src= ./where_what_blob/test_analysis_every_20.png width="400">   |



