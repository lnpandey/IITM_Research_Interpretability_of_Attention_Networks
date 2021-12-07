#### SIN CIN trained SDC

- Dataset 4 m 100 size 100


##### Table 1: train both 

| scaled by \ - | intial db | final train| final test | final db |
| ---------  | ------ | ----- | ------ | ------- |
| 1 |<img src= ./plots/train_both/initial_scaled_by_1.png width="800">  |  <img src= ./plots/train_both/final_scaled_by_1_train.png width="800"> | <img src= ./plots/train_both/final_scaled_by_1_test.png width="800"> | <img src= ./plots/train_both/final_scaled_by_1_db.png width="800"> |
| 2 |<img src= ./plots/train_both/initial_scaled_by_2.png width="800">  |  <img src= ./plots/train_both/final_scaled_by_2_train.png width="800"> | <img src= ./plots/train_both/final_scaled_by_2_test.png width="800"> | <img src= ./plots/train_both/final_scaled_by_2_db.png width="800"> |
| 3.5 |<img src= ./plots/train_both/initial_scaled_by_3.5.png width="800">  |  <img src= ./plots/train_both/final_scaled_by_3.5_train.png width="800"> | <img src= ./plots/train_both/final_scaled_by_3.5_test.png width="800"> | <img src= ./plots/train_both/final_scaled_by_3.5_db.png width="800"> |
| 7 |<img src= ./plots/train_both/initial_scaled_by7.png width="800">  |  <img src= ./plots/train_both/final_scaled_by_7_train.png width="800"> | <img src= ./plots/train_both/final_scaled_by_7_test.png width="800"> | <img src= ./plots/train_both/final_scaled_by_7_db.png width="800"> |
| 10 |<img src= ./plots/train_both/initial_scaled_by_10.png width="800">  |  <img src= ./plots/train_both/final_scaled_by_10_train.png width="800"> | <img src= ./plots/train_both/final_scaled_by_10_test.png width="800"> | <img src= ./plots/train_both/final_scaled_by_10_db.png width="800"> |
| 15 |<img src= ./plots/train_both/initial_scaled_by_15.png width="800">  |  <img src= ./plots/train_both/final_scaled_by_15_train.png width="800"> | <img src= ./plots/train_both/final_scaled_by_15_test.png width="800"> | <img src= ./plots/train_both/final_scaled_by_15_db.png width="800"> |

##### Table 2: train both performance

|scaled by \ - | train accuracy | train ftpt  | train ffpt | test accuracy |test ftpt | test ffpt |
| ------- | ---- | -- | --- |  --- | ---- | --- |
| 1 |  80 | 0 | 80  | 33.9 |  0 | 33.9|
| 2 | 66 | 0 | 66 | 33.7 | 0 | 33.7 |
| 3.5 | 82 | 35 | 47 | 67.2 | 35.7 | 31.5 |
| 7 | 100 | 61 | 39 | 100 | 68 | 32 |
| 10 | 100 | 61 | 39 | 100 | 68 | 32 |
| 15 | 100 | 63 | 37 | 99.9 | 68.5 | 31.4 | 
| 25 | 100 | 63 | 37 | 100 | 69   |  31  |
| 50 | 100 | 62 | 38 | 99.7 | 67.7 | 32.0|
| 100 | 100 | 61 | 39 | 99.5 | 67.5 | 32.0 |

##### Table 3: Pretraining on True foreground data
- Pretrain Performance
- train 100
- test 100

| scaled by/ -  | inital db| final train | final test | train accuracy | train ftpt | train ffpt | test accuracy | test ftpt | test ffpt |
|  ------       | ----     |     ------- | --------- |  ---------   | ----- | --- | ----- | ---- | ----- |  
| 1 | <img src= ./plots/fg_train/initial_scaled_by_1.png width="800"> | <img src= ./plots/fg_train/final_scaled_by_1_train.png width="800"> | <img src= ./plots/fg_train/final_scaled_by_1_test.png width="800"> | 100 | 61 | 39 | 100 | 68.1 | 31.9 |  

<!-- 
  - scaled by 1
    - train performance 74
    - test performance 67.7

  - scaled by 0.8
    - train performance 100
    - test performance 100

  - scaled by 1.5
    - train performance 100
    - test performance 100
 -->
