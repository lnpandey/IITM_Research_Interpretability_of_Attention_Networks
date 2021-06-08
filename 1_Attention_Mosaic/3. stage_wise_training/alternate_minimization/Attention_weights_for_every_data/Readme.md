### Learning attention weights for every data point CIFAR data


#### Table A1: Simultaneous Model Performance (in percentage)
| \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| Train | 70.93 	 | 29.07 |	73.690000 |	24.933333 |	0.300000 |	1.076667 | 
| Test | 67.48	 |  32.52 |	66.16 |	17.39 |	4.10 |	12.35 |




#### Table A2 : learning attention weights as well as what net(random)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 15.91 |	84.08	 |  16.39 |	80.88 |	0.216	|  2.51 |
| 0.1 | 54.87 | 	45.13 |	19.65 |78.36 |	0.216	 | 1.76 |
| 1 |99.68 |	0.31 | 21.12 |	56.67 |	2.04 |	20.17 |
| 10 | 100 |	0	 | 19.89 |	54.78 |	2.35 |	22.97 |



#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table A3: Fixed what net learning only attention weights for each data point
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 3886 | 	26114 |	4877 |	23269 |	50 |	1804 |
| 0.1 | 12483 |	17517 |	7146 |	22167	 | 5 |	682 |
| 1 | 26332	| 3668 |	8460 |	16695 |	131 |	4714 |
| 10  | 28421 |	1579	 | 7958	| 14228	 | 252	| 7562 |

#### Table A4: Fixed what net learning both attention weights and what net 

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 3419	| 26581	| 4430 |	24961	 | 44	 | 565 |
| 0.1 | 15734	| 14266 |	8072 |	21396	| 35 |	497 |
| 1 | 29930	| 70 |	8827 |	16703 |	350 |	4120 |
| 10 | 30000 |	0	| 7484 |	15810 |	475 |	6231 |





### Learning attention weights for every data point type4 data


#### Table B1: Simultaneous Model Performance (in percentage)
| \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | -- |
| Train |- | -|84.366667	| 15.6 |	0.033333 |	0.0 | <img src= ./type4_data/db.png width="450"> |





#### Table B2 : learning attention weights as well as what net (random)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | --- |
| 0.01 | 671 |	2329 |	495 |	2455 |	18 |	32 | <img src= ./type4_data/both_random_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1  |  2250 |	750 |	616 |	2364 |	20	 |0 | <img src= ./type4_data/both_random_what/lr_0.1/decision_boundary.png width="450"> |
| 1 | 2997 |	3	 | 146	| 2668 |	21 |	165 | <img src= ./type4_data/both_random_what/lr_1/decision_boundary.png width="450"> |
| 10 | 3000 |	0	 | 125 |	2546 |	23 |	306 | <img src= ./type4_data/both_random_what/lr_10/decision_boundary.png width="450"> |



#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table B3: Fixed what net learning only attention weights for each data point
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 370 |	2630 |	538 |	2421 |	10 |	31 | <img src= ./type4_data/only_attn_wts_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 	809	| 2191	| 694 |	2283 |	7 |	16 | <img src= ./type4_data/only_attn_wts_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 1785 |	1215 |	634 |	2237 |	66 |	63 | <img src= ./type4_data/only_attn_wts_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10  | 2049 |	951 |	632 |	2079 |	138 |	151 | <img src= ./type4_data/only_attn_wts_pretrained_what/lr_10/decision_boundary.png width="450">   |

#### Table B4: Fixed what net learning both attention weights and what net 

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 	858 |	2142 |	415 |	2562 |	17 |	6 | <img src= ./type4_data/both_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 	892	 | 2108 |	843 |	2117 |	3 |	37 | <img src= ./type4_data/both_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 2060 |	940 |	785 |	2179 |	9 |	27 | <img src= ./type4_data/both_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10 | 2777 | 223 |	652 |	2290 |	4 | 	54| <img src= ./type4_data/both_pretrained_what/lr_10/decision_boundary.png width="450">   |



### Learning attention weights for every data point blob data


#### Table C1: Simultaneous Model Performance (in percentage)
| \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| Train | -	 | -  |	99.9 |	0.1 |	0 |	0 | 




#### Table A2 : learning attention weights as well as what net(random)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 518	| 2482 |	157	| 2798 |	13 |	32 |
| 0.1 | 2275 |	725 |	204 |	2755 |	20 |	21 |
| 1 | 2999 |	1	 | 389	 | 1799 |	57 |	755 |
| 10 | 3000 |	0	 | 365	| 1581 |	71 |	983| 



#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table A3: Fixed what net learning only attention weights for each data point
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 462 |	2538	|630	 |2287 |	11 |	72 |
| 0.1 | 855 |	2145 |	722 |	2240 |	9	| 29 |
| 1 | 1714	| 1286 |	702 |	2249 |	0 |	49 |
| 10  | 2011 |	989	 | 597 |	2250 |	0	 |153 |

#### Table A4: Fixed what net learning both attention weights and what net 

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 	479	|2521|	409	|2541 |	8	| 42|
| 0.1 | 988	|2012	|632	|2315	|6	| 47 |
| 1 | 2696	|304	|877	 |1915	|6	 | 202 |
| 10 | 2975	|25	|745	|1705	|15	 |535 |





