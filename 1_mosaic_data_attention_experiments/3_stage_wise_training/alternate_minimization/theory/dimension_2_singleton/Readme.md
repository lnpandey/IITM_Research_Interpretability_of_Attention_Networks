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

