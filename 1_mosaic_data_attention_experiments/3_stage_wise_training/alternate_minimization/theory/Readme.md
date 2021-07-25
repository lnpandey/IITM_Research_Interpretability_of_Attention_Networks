### Alternate minimization theory


- m = 2
- f(x) = ax
- g(x) = bx + c

#### Minimize b and c while a is fixed

- Contour plots

| a | 0 | -10 | 10 | 
| - | - | -   | -  |  
|plots | <img src= ./plots/contour_b_c_a_0.png width="450"> | <img src= ./plots/contour_b_c_a_n10.png width="450"> | <img src= ./plots/contour_b_c_a_10.png width="450"> |
| initial loss | 0.6931 | 0.6931 | 0.6931 |
| final loss   |  0.0013 | 0.0001 |    0.6931   |


- Plots


| | loss plot fixed a | minimized b value for fixed a | minimized c value for fixed a |
| - |     ------      |   --------------------------- |  ---------------------------  |
|   | <img src= ./plots/loss_fixed_a.png width="450"> |  <img src= ./plots/minimized_b_fixed_a.png width="450"> |  <img src= ./plots/minimized_c_fixed_a.png width="450"> |


 

#### Minimize a while b and c are fixed

- loss landscape

| b   c| 0  |  10  |  -10 |
| ---  |  -   | -    | -    |
| 0  | <img src= ./plots/loss_landscape_b_0_c_0.png width="450"> |  <img src= ./plots/loss_landscape_b_0_c_10.png width="450"> | <img src= ./plots/loss_landscape_b_0_c_n10.png width="450"> |
| 10 | <img src= ./plots/loss_landscape_b_10_c_0.png width="450"> |  <img src= ./plots/loss_landscape_b_10_c_10.png width="450"> | <img src= ./plots/loss_landscape_b_10_c_n10.png width="450"> |
| -10 | <img src= ./plots/loss_landscape_b_n10_c_0.png width="450"> |  <img src= ./plots/loss_landscape_b_n10_c_10.png width="450"> | <img src= ./plots/loss_landscape_b_n10_c_n10.png width="450"> |

