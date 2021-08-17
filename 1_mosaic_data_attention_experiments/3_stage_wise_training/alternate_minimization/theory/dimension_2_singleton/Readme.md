### 2D Singleton Experiment


- Data
  - D_0 = [3.5,4]
  - D_1 = [1,1]
  - D_2 = [2,1]
  - D_3 = [1,2]
  - initial a = 0 , b = 0 ,c = 0 {a and c are vectors, b is a matrix}


 ##### Running for number of epochs(10000) without any tolerance after 20 runs of minimizing b_c and minimizing a alternatively
- m = 2
    - minimizing b_c first
    - initial loss =  1.098612
    - final loss = 0.00573
    - final a = [[-1.095398], [-1.5270395]]  
    - same results for minimizing a first
 
- m = 9 
    - minimizing b_c first
    - initial loss = 1.098612
    - final loss = 0.002946
    - final a = [[-1.4724603], [-1.8271058]]
    - same results for minimizing a first


 ##### Running for number of epochs(200000) with tolerance of 0.01 after 20 runs of minimizing b_c and minimizing a alternatively
- m = 2
    - minimizing b_c first
    - initial loss =  1.098612
    - final loss = 0.009999 (happens after first minimize a when we starts with minimize b_c for the case of minimize a first this occurs after 2nd minimize a)
    - final a = [[-0.17368719], [-0.24413258]] 
    - same results for minimizing a first


 
- m = 9 
    - minimizing b_c first
    - initial loss = 1.098612
    - final loss = 0.009999 (happens after first minimize a when we starts with minimize b_c for the case of minimize a first this occurs after 2nd minimize a)
    - final a = [[-0.74600106], [-0.8439506]]
    - same results for minimizing a first

### 2d Non-Singleton Experiment

<!---| Experiment |Data | Margin | Final a | Final b | Final c | Accuracy | FTPT | FFPT|
| ---------- | --  | ------ | ------- | ------  | ------- | -------- | -----| --- |
|  Simultaneous | <img src= ./plots/Data_1.PNG width="450"> | 1.775 | [-0.4871, -0.4627] | [[-0.0115, -0.3366],[ 1.2266, -1.5368],[-1.2151,  1.8734]]  | [-0.4299,  0.1471,  0.2828] | 100 | 100 | 0 | 6,6 5,5,4,4,3.5,3.5 
| Alternate     | <img src= ./plots/Data_1.PNG width="450"> | 1.775 | [-0.5805, -0.5160]  | [[-0.0213, -0.2803],[ 1.0890, -1.3582],[-1.0678,  1.6385]] | [-0.3307,  0.1240,  0.2067] | 100 | 100 | 0  |
| Simultaneous    |<img src= ./plots/Data_2.PNG width="450"> | 1.07 | [-0.5695, -0.4968] | [[-0.0920, -0.3123],[ 1.1583, -1.5061],[-1.0663,  1.8184]] | [-0.4473,  0.1858,  0.2615] |100  | 100  | 0   | 
| Alternate     | <img src= ./plots/Data_2.PNG width="450">|  1.07 | [-0.6335, -0.5297] | [[-0.0910, -0.2624],[ 1.0322, -1.3351],[-0.9411,  1.5975]]  | [-0.3598,  0.1592,  0.2006]| 100 | 100 | 0 | 
| Simultaneous    | <img src= ./plots/Data_3.PNG width="450"> | 0.37 | [-0.7408, -0.5857] | [[-0.2075, -0.2743],[ 1.0654, -1.4508],[-0.8579,  1.7251]] | [-0.4812,  0.2539,  0.2273] | 100  | 100 |  0  |
| Alternate     | <img src= ./plots/Data_3.PNG width="450"> | 0.37 | [-0.7598, -0.5871] | [[-0.1911, -0.2361],[ 0.9541, -1.2917], [-0.7630,  1.5278]]| [-0.4074,  0.2227,  0.1847]  | 100 | 100 | 0  |
| Simultaneous   |<img src= ./plots/Data_4.PNG width="450">| 0.021 | [-0.8963, -0.7067] | [[-0.2846, -0.2525],[ 1.0105, -1.4098],[-0.7259,  1.6624]] | [-0.5226,  0.3213,  0.2013] | 100 | 100 | 0  | 
| Alternate     | <img src= ./plots/Data_4.PNG width="450"> | 0.021 | [-0.8830, -0.6874] |  [[-0.2589, -0.2218],[ 0.9082, -1.2594],[-0.6493,  1.4812]] | [-0.4542,  0.2865,  0.1677] | 100 | 100 | 0  |
--->

| Experiment   | Data| FG Margin | FG vs BG Margin | final a | final b | final c | Accuracy | FTPT | FFPT |
| -----------  | ---- |-------   | --------------  | --      | -----   | ------- | -------- | ---- | ---  |
| Simultaneous | <img src= ./plots/data_fg_l_bg_l.PNG width="450"> |large      | large (1.775)   | [-0.4871, -0.4627] | [[-0.0115, -0.3366],[ 1.2266, -1.5368],[-1.2151,  1.8734]]  | [-0.4299,  0.1471,  0.2828] | 100 | 100 | 0 |
| Alternate    | - | large    | large (1.775 )  | [-0.5805, -0.5160]  | [[-0.0213, -0.2803],[ 1.0890, -1.3582],[-1.0678,  1.6385]] | [-0.3307,  0.1240,  0.2067] | 100 | 100 | 0 |
| Simultaneous | <img src= ./plots/data_fg_l_bg_s.PNG width="450"> |large      | small (0.021)   |  [-0.8963, -0.7067] | [[-0.2846, -0.2525],[ 1.0105, -1.4098],[-0.7259,  1.6624]] | [-0.5226,  0.3213,  0.2013] | 100 | 100 | 0  | 
| Alternate    | -| large   | small (0.021)   |  [-0.8830, -0.6874] |  [[-0.2589, -0.2218],[ 0.9082, -1.2594],[-0.6493,  1.4812]] | [-0.4542,  0.2865,  0.1677] | 100 | 100 | 0  |
| Simultaneous | <img src= ./plots/data_fg_l_bg_n.png width="450"> | large      | negative        | [-1.1977, -0.8701]  |   [-0.4020, -0.2145],[ 0.9927, -1.4162],[-0.5907,  1.6306] | [-0.7524,  0.5525,  0.1999] | 100 | 99.3 | 0.7 |
| Alternate    | - | large    | negative   | [-1.1333, -0.8355] | [-0.3590, -0.1998],[ 0.8910, -1.2623],[-0.5320,  1.4621] | [-0.6373,  0.4817,  0.1557] | 100 | 99.4 | 0.6 |
| Simultaneous | <img src= ./plots/data_fg_s_bg_l.png width="450"> | small   | large(1.80) | [-0.1739, -0.0109]  | [-0.2626, -0.4317],[ 1.9778, -2.4653],[-1.7152,  2.8970] | [-3.8145,  3.1386,  0.6759]  | 99.4 | 99.4 | 0|
| Alternate    | - | small    | large(1.80)    | [-0.5935, -0.3999] | [-0.1756, -0.2744],[ 1.7668, -2.3802],[-1.5912,  2.6546] | [-2.2580,  1.8282,  0.4298] | 97.1 | 97.1 | 0 |  
| Simultaneous | <img src= ./plots/data_fg_s_bg_s.png width="450"> |  small  |  small(0.06) | [-0.3298, -0.0679]  |  [-0.6556, -1.0324],[ 1.5053, -2.1144],[-0.8497,  3.1468] | [-4.2313,  4.4658, -0.2344]  | 99.9 | 99.9 | 0 |
| Alternate   | - |small |  small (0.06) |  [-0.3110, -0.1293] | [-0.5841, -0.7824],[ 1.3705, -2.0520],[-0.7864,  2.8344] | [-3.4342,  3.5680, -0.1337] | 99.8 | 99.8 | 0 |
| Simultaneous | <img src= ./plots/data_fg_s_bg_n.png width="450"> |small | negative | [-0.4566, -0.0703] | [-0.8148, -1.1690],[ 1.2640, -1.7271],[-0.4491,  2.8961] | [-3.8652,  4.7646, -0.8994] | 99.9 | 99.3 | 0.6 |
| Alternate | - | small | negative | [-0.4492, -0.1199] | [-0.7156, -0.9654], [ 1.1231, -1.6631],[-0.4074,  2.6285] | [-3.2651,  3.9658, -0.7008] | 100 | 99.6 | 0.4 |
| Simultaneous | <img src= ./plots/data_fg_n_bg_l.png width="450"> | negative | large(1.86) | [-0.1956, -0.0161] | [ 0.1624, -1.1270],[ 1.9000, -1.7433],[-2.0624,  2.8704] | [-5.5357,  5.6765, -0.1408] | 90.1 | 90.1 | 0 |  
| Alternate  | - |negative  | large(1.86) | [-0.5737, -0.2861] | [ 0.1318, -0.5949],[ 1.3926, -1.5572],[-1.5244,  2.1522] | [-2.9890,  2.9546,  0.0344] | 88.6 | 88.6 | 0 |
| Simultaneous | <img src= ./plots/data_fg_n_bg_s.png width="450"> | negative | small (0.09)    | [-0.3121, -0.2704] | [-0.4758, -1.1835],[ 2.1850, -1.9214],[-1.7092,  3.1050] | [-4.3531,  5.9438, -1.5907] | 93.2 | 93.2  | 0|
| Alternate    | - |negative | small (0.09)    | [-0.2952, -0.2850] | [-0.3622, -1.1168],[ 1.9109, -1.8734],[-1.5487,  2.9902] | [-3.6028,  4.6278, -1.0251] | 93.4  | 93.4 | 0 | 
| Simultaneous | <img src= ./plots/data_fg_n_bg_n.png width="450"> |negative | negative | [-0.5045, -0.3360] | [-0.6341, -1.2189],[ 2.1319, -1.8091],[-1.4977,  3.0280] | [-3.3582,  5.6900, -2.3319] | 92.9 | 92.7 | 0.2 |
| Alternate |  - | negative  |  negative | [-0.4856, -0.3613] | [-0.5382, -1.1886],[ 1.8617, -1.7577],[-1.3235,  2.9463] | [-3.0063,  4.6494, -1.6430] | 92.8 | 92.6 | 0.2 |

#### Increasing the BG Variance and keeping FG Margin Small and BG vs FG margin large(1.80)

| Experiment | Data | final a | final b| final c| Accuracy | ftpt | ffpt |
| ---------  | --   | ----    |------  | -----  | -------- | ---  | ---  |
| Simultaneous |  <img src= ./plots/data_bg_var_0_2.png width="450">  |  [-0.1615, -0.1378] | [-0.4846, -0.3946],[ 2.8523, -3.4964],[-2.3677,  3.8910] | [-4.2962,  3.2414,  1.0548] | 99.3 | 99.3 | 0 | 
| Alternate    | -  | [-0.4024, -0.2984] |  [-0.3091, -0.2265],[ 2.3525, -3.0624],[-2.0434,  3.2889]  | [-2.4181,  1.8502,  0.5679] | 97.5 |97.5  |0 |
| Simultaneous | <img src= ./plots/data_bg_var_0_3.png width="450"> | [-0.1890, -0.1919] | [-0.5868, -0.3908],[ 3.2665, -3.9442],[-2.6796,  4.3350] |  [-4.4597,  3.2409,  1.2187] |  99.2 | 99.2 | 0 |
| Alternate    |  - | [-0.1944, -0.2508] | [-0.4404, -0.2122],[ 2.7887, -3.5050],[-2.3484,  3.7172]  | [-2.6832,  1.9644,  0.7188] | 98.3 | 98.3 | 0 |
| Simultaneous | <img src= ./plots/data_bg_var_0_4.png width="450">  | [-0.2145, -0.2323] | [-0.6563, -0.3858],[ 3.5754, -4.2655],[-2.9192,  4.6514] | [-4.5507,  3.2212,  1.3294] | 99.2 | 99.2 | 0 |
| Alternate    | - | [-0.2272, -0.2911] | [-0.4930, -0.2104],[ 3.0481, -3.7761],[-2.5551,  3.9864] | [-2.8002,  1.9914,  0.8088] |  98.4 | 98.4 | 0 |
| Simultaneous |  <img src= ./plots/data_bg_var_1.png width="450">  | [-0.3482, -0.3727] | [-0.8743, -0.4078],[ 4.6882, -5.2902],[-3.8139,  5.6980] | [-4.8614,  3.1185,  1.7429] | 99.1 | 99.1 | 0 |
| Alternate | - | | | | | | |
| Simultaneous | <img src= ./plots/data_bg_var_1.png width="450"> | [-0.4993, -0.4927] | [-1.0138, -0.4973],[ 5.5521, -6.0480],[-4.5383,  6.5453] | [-5.2342,  3.1624,  2.0718] | 98.8 | 98.8 |0 |
| Alternate | - | | | | | | |
| Simultaneous | <img src= ./plots/data_bg_var_5.png width="450"> | [-0.7846, -0.7141] | [-1.1647, -0.6820],[ 6.6620, -6.9221],[-5.4973,  7.6042] | [-5.7317,  3.2180,  2.5137] | 98.9 | 98.9 | 0|
| Alternate | - | | | | | | |
| Simultaneous | <img src= ./plots/data_bg_var_10.png width="450">| [-1.2077, -1.0847] | [-1.2248, -0.8353],[ 7.3237, -7.4284],[-6.0989,  8.2638] | [-5.9478,  3.2040,  2.7438] | 98.7| 98.7 | 0 |
| Alternate | - | | | | | | |

