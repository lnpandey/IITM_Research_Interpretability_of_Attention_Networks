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

| Experiment |Data | Margin | Final a | Final b | Final c | Accuracy | FTPT | FFPT|
| ---------- | --  | ------ | ------- | ------  | ------- | -------- | -----| --- |
|  Simultaneous | DATA 1 | 1.775 | [-0.4871, -0.4627] | [[-0.0115, -0.3366],[ 1.2266, -1.5368],[-1.2151,  1.8734]]  | [-0.4299,  0.1471,  0.2828] | 100 | 100 | 0 | <!---6,6 5,5,4,4,3.5,3.5 --->
| Alternate     | Data 1 | 1.775 | [-0.5805, -0.5160]  | [[-0.0213, -0.2803],[ 1.0890, -1.3582],[-1.0678,  1.6385]] | [-0.3307,  0.1240,  0.2067] | 100 | 100 | 0  |
| Simultaneous    | Data 2 | 1.07 | [-0.5695, -0.4968] | [[-0.0920, -0.3123],[ 1.1583, -1.5061],[-1.0663,  1.8184]] | [-0.4473,  0.1858,  0.2615] |100  | 100  | 0   | 
| Alternate     | Data 2 |  1.07 | [-0.6335, -0.5297] | [[-0.0910, -0.2624],[ 1.0322, -1.3351],[-0.9411,  1.5975]]  | [-0.3598,  0.1592,  0.2006]| 100 | 100 | 0 | 
| Simultaneous    | Data 3 | 0.37 | [-0.7408, -0.5857] | [[-0.2075, -0.2743],[ 1.0654, -1.4508],[-0.8579,  1.7251]] | [-0.4812,  0.2539,  0.2273] | 100  | 100 |  0  |
| Alternate     | Data 3 | 0.37 | [-0.7598, -0.5871] | [[-0.1911, -0.2361],[ 0.9541, -1.2917], [-0.7630,  1.5278]]| [-0.4074,  0.2227,  0.1847]  | 100 | 100 | 0  |
| Simultaneous   | Data 4 | 0.021 | [-0.8963, -0.7067] | [[-0.2846, -0.2525],[ 1.0105, -1.4098],[-0.7259,  1.6624]] | [-0.5226,  0.3213,  0.2013] | 100 | 100 | 0  | 
| Alternate     | Data 4 | 0.021 | [-0.8830, -0.6874] |  [[-0.2589, -0.2218],[ 0.9082, -1.2594],[-0.6493,  1.4812]] | [-0.4542,  0.2865,  0.1677] | 100 | 100 | 0  |
