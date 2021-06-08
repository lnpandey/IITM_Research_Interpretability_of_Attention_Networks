### Learning attention weights for every data point CIFAR data


#### Table A1: Simultaneous Model Performance (in percentage)
| \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| Train | 21279	 | 8721 |	73.690000 |	24.933333 |	0.300000 |	1.076667 | 
| Test | 6748	 |  3252 |	66.16 |	17.39 |	4.10 |	12.35 |




#### Table A2 : learning attention weights as well as what net(random)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 4774 |	25226	 |  4918 |	24264 |	63	|  755 |
| 0.1 | 16461 | 	13539 |	5897 |	23510 |	65	 | 528 |
| 1 | 29906 |	94 |	6336 |	17001 |	612 |	6051 |
| 10 | 30000 |	0	 | 5967 |	16434 |	707 |	6892 |



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


#### Table A1: Simultaneous Model Performance (in percentage)
| \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | -- |
| Train |- | -|84.366667	| 15.6 |	0.033333 |	0.0 | <img src= /type4_data/db.png width="450"> |





#### Table A2 : learning attention weights as well as what net (random)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | --- |
| 0.01 | 671 |	2329 |	495 |	2455 |	18 |	32 | <img src= ./type4_data/both_random_what/lr_0_01/decision_boundary.png width="450">   |
| 0.1  |  2250 |	750 |	616 |	2364 |	20	 |0 | <img src= ./type4_data/both_random_what/lr_0.1/decision_boundary.png width="450"> |
| 1 | 2997 |	3	 | 146	| 2668 |	21 |	165 | <img src= ./type4_data/both_random_what/lr_1/decision_boundary.png width="450"> |
| 10 | 3000 |	0	 | 125 |	2546 |	23 |	306 | <img src= ./type4_data/both_random_what/lr_10/decision_boundary.png width="450"> |



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



