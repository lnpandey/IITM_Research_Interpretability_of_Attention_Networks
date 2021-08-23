## Alternate minimization theory

### Data 1
- m = 2
- f(x) = ax
- g(x) = bx + c
- Data_1  D_0 = 3 , D_1 = +1, D_-1 = -1

#### Minimize b and c while a is fixed

- Table A1: Contour plots

| a | 0 | -10 | 10 | 
| - | - | -   | -  |  
|plots | <img src= ./plots/data_1/contour_b_c_a_0.png width="450"> | <img src= ./plots/data_1/contour_b_c_a_n10.png width="450"> | <img src= ./plots/data_1/contour_b_c_a_10.png width="450"> |
| initial loss | 0.6931 | 0.6931 | 0.6931 |
| final loss   |  0.0013 | 0.0001 |    0.6931   |


- Table A2: Plots


| | loss plot fixed a | minimized b value for fixed a | minimized c value for fixed a |
| - |     ------      |   --------------------------- |  ---------------------------  |
|   | <img src= ./plots/data_1/loss_fixed_a.png width="450"> |  <img src= ./plots/data_1/minimized_b_fixed_a.png width="450"> |  <img src= ./plots/data_1/minimized_c_fixed_a.png width="450"> |


 

#### Minimize a while b and c are fixed

- Table A3: loss landscape

| b   c| 0  |  10  |  -10 |
| ---  |  -   | -    | -    |
| 0  | <img src= ./plots/data_1/loss_landscape_b_0_c_0.png width="450"> |  <img src= ./plots/data_1/loss_landscape_b_0_c_10.png width="450"> | <img src= ./plots/data_1/loss_landscape_b_0_c_n10.png width="450"> |
| 10 | <img src= ./plots/data_1/loss_landscape_b_10_c_0.png width="450"> |  <img src= ./plots/data_1/loss_landscape_b_10_c_10.png width="450"> | <img src= ./plots/data_1/loss_landscape_b_10_c_n10.png width="450"> |
| -10 | <img src= ./plots/data_1/loss_landscape_b_n10_c_0.png width="450"> |  <img src= ./plots/data_1/loss_landscape_b_n10_c_10.png width="450"> | <img src= ./plots/data_1/loss_landscape_b_n10_c_n10.png width="450"> |

<!---#### Table A4:  loss values and minimized a,b and c


| | a fixed | b c fixed | a  | b  | c | loss | 
| - | -     | ----      | -  | -- | - | -    |
| 1 | True | True    | 0  | 0  | 0 | 0.6931 |
| 2 | True  | False  | 0  | 13.33 | -19.75  | 0.0013 | 
| 3 | False |  True  |  0  |  0    |   0     |  0.6931 |
| 4 | False  |  True  | -0.028 | 13.33 | -19.75 | 0.00090 |
| 5 | True  |   True |  0 | 100 | 0 |  17.269 |
| 6 | True |   False | 0 |  45 | -54 | 5.05e-5 |
| 7 | False | True |  -20 | 100 | 0 | 9.99e-16 |
| 8 | True |  True | -20 | -100 | 0 |    34.53   |
| 9 | True |  False | -20 | 9.199 | 1.57e-15 | 0.00010       |
| 10 | Fale |  True | -20 | -100 | 0 |    34.53      | --->

### Data 2
- m = 2 
- f(x) = ax
- g(x) = bx + c
- Data_2, D_0 = -3, D_1 = +1, D_-1 = -1


#### Minimize b and c while a is fixed

- Table B1: Contour plots

| a | 0 | -10 | 10 | 
| - | - | -   | -  |  
|plots | <img src= ./plots/data_2/contour_b_c_a_0.png width="450"> | <img src= ./plots/data_2/contour_b_c_a_n10.png width="450"> | <img src= ./plots/data_2/contour_b_c_a_10.png width="450"> |
| initial loss | 0.6931 | 0.6931 | 0.6931 |
| final loss   |  0.0013 | 0.6931 |    0.0001   |


- Table B2: Plots


| | loss plot fixed a | minimized b value for fixed a | minimized c value for fixed a |
| - |     ------      |   --------------------------- |  ---------------------------  |
|   | <img src= ./plots/data_2/loss_fixed_a.png width="450"> |  <img src= ./plots/data_2/minimized_b_fixed_a.png width="450"> |  <img src= ./plots/data_2/minimized_c_fixed_a.png width="450"> |


#### Minimize a while b and c are fixed

- Table B3: loss landscape

| b   c| 0  |  10  |  -10 |
| ---  |  -   | -    | -    |
| 0  | <img src= ./plots/data_2/loss_landscape_b_0_c_0.png width="450"> |  <img src= ./plots/data_2/loss_landscape_b_0_c_10.png width="450"> | <img src= ./plots/data_2/loss_landscape_b_0_c_n10.png width="450"> |
| 10 | <img src= ./plots/data_2/loss_landscape_b_10_c_0.png width="450"> |  <img src= ./plots/data_2/loss_landscape_b_10_c_10.png width="450"> | <img src= ./plots/data_2/loss_landscape_b_10_c_n10.png width="450"> |
| -10 | <img src= ./plots/data_2/loss_landscape_b_n10_c_0.png width="450"> |  <img src= ./plots/data_2/loss_landscape_b_n10_c_10.png width="450"> | <img src= ./plots/data_2/loss_landscape_b_n10_c_n10.png width="450"> |



### type 0 data

#### When D0 > D_+1, D_-1

<img src= ./plots/data_2/data_d0_gr_d1.png width="450">

- Loss heatmap for minimizing a with fix value of b and c

<img src= ./plots/data_2/loss_heatmap_1.png width="450">

- final a value heatmap for minimizing a with fix value of b and c

<img src= ./plots/data_2/a_value_heatmap_1.png width="450">


#### When D0 < D_+1, D_-1

<img src= ./plots/data_2/data_d0_ls_d1.png width="450">

- Loss heatmap for minimizing a with fix value of b and c

<img src= ./plots/data_2/loss_heatmap_2.png width="450">

- final a value heatmap for minimizing a with fix value of b and c

<img src= ./plots/data_2/a_value_heatmap_2.png width="450">







