### generalization in attention networks

Base Model CNN 6 layer model

Attention Model 1 - Random Focus Random Classify train both

Attention Model 2 - Random Focus Random Classify train classify

<!---| Model        | Train Accuracy | Test Accuracy |
| ------------ | -------------- |  ------------ |
| Attn Model 1 |    99          |  91           |
| Attn Model 2 |    99          |  41           |--->


Parameter Analysis 
|  Model        |  Min Value    | Max Value | Margin  | Prod Spec Norm | Path Norm |
| ------------- | ------------- | --------- | ------  | -------------- | --------  |
| Attn Model 1  |  -1.09        |  1.511    |    3.44 | 6.66x10e9      |   4.7666  |
| Attn Model 2  | -1.47         |  1.93     |  3.08   | 2.5x10e13      |   110.621 |

#### Histogram Attn Model 1
<img src= attention_model_1_hist.png width="400">  
#### Histogram Attn Model 2
<img src= attention_model_2_hist.png width="400">  
