### Learning attention weights for each data point

#### Table A : CIFAR data
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.001        | 0 | 30000 |  3591  | 25744  | 65  | 600 | 
| 0.1         | 9718 | 20282 | 3396 | 26165 | 27 | 412 |
| 10          | 15947 |	14053 |	2486 |	14468 |	1202 |	11844 |
| 100    | 14141 |	15859	 | 2374 | 	16183 |	1202	|10241 |
|1000 | 17048 |	12952	 |2662 |	15768	 | 1105 |	10465  |
| 10000 | 	13191	| 16809 |	2311 |	15807	 | 1255	| 10627  |


As we are changing the LR for attention wts attention weights do improve (as argmax>0.5 column in Table A ), But have very little or no effect on Focus True.


#### Now we are fixing the what net with final weights of simultaneous trained what net

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01         | 650 | 	29350 |	2224 |	10747 |	1689 |	15340|
| 0.1 | 9972 |	20028 | 	3361 |	14267 |	761 |	11611 |
|10 |  17100	| 12900 |	2888 |	11244 |	1009 |	14859 |
| 100    | 17106 |  12894 |	2885 |	11241 |	1008 |	14866 |
|1000 | 17106 |	12894 |	2885 |	11241	 | 1008 |	14866 |

Here as what net is fixed as we increase LR the overall performance does not change much, but still we can see the improvement in alpha values (which are not reflected in Focus True)
