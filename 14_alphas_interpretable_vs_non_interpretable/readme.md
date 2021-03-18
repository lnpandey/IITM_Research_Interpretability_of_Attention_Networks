### effects of complexity on interpretability

DATA: Synthetic elliptical blobs data 

### Table A: trend of complexity with CE Loss
Entries are of the form FTPT / FFPT
|focus/ Classify | 50 | 100 | 200 | 300 |
|----------------|----|-----|-----|-----|
| 50  | 74.71 / 25.26 | 82.15 / 17.85 | 80.88 / 19.11 | 86.25 / 13.74 |
| 100 | 76.92 / 16.93 | 90.16 / 9.83  | 99.1 / 0.9    | 87.67 / 12.32 |
| 200 | 86.78 / 7.00  | 86.45 / 7.32  | 97.56 / 2.44  | 99.97 / 0.026 |
| 300 | 99.76 / 0.226 | 90.14 / 3.87  | 99.96 / 0.04  | 99.98 / 0.013 |

### Table 1 : focus 50 Classification 50

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/50_50/k0/run1_50_50_10runs.png width="150"> |  <img src=./plots_images/50_50/k01/run1_50_50_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/50_50/k0/run6_50_50_10runs.png width="150"> |  <img src=./plots_images/50_50/k01/run6_50_50_10runs_entropy.png width="150"> |   
| Run 2  | <img src=./plots_images/50_50/k0/run2_50_50_10runs.png width="150"> |  <img src=./plots_images/50_50/k01/run2_50_50_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/50_50/k0/run7_50_50_10runs.png width="150"> |  <img src=./plots_images/50_50/k01/run7_50_50_10runs_entropy.png width="150"> |   
| Run 3  | <img src=./plots_images/50_50/k0/run3_50_50_10runs.png width="150"> |  <img src=./plots_images/50_50/k01/run3_50_50_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/50_50/k0/run8_50_50_10runs.png width="150"> |  <img src=./plots_images/50_50/k01/run8_50_50_10runs_entropy.png width="150"> |   
| Run 4  | <img src=./plots_images/50_50/k0/run4_50_50_10runs.png width="150"> |  <img src=./plots_images/50_50/k01/run4_50_50_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/50_50/k0/run9_50_50_10runs.png width="150"> |  <img src=./plots_images/50_50/k01/run9_50_50_10runs_entropy.png width="150"> |   
| Run 5  | <img src=./plots_images/50_50/k0/run5_50_50_10runs.png width="150"> |  <img src=./plots_images/50_50/k01/run5_50_50_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/50_50/k0/run10_50_50_10runs.png width="150">|  <img src=./plots_images/50_50/k01/run10_50_50_10runs_entropy.png width="150">|   
 
 
### Table 2 : focus 50 Classification 100

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/50_100/k0/run1_50_100_10runs.png width="150"> |  <img src=./plots_images/50_100/k01/run1_50_100_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/50_100/k0/run6_50_100_10runs.png width="150"> |  <img src=./plots_images/50_100/k01/run6_50_100_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/50_100/k0/run2_50_100_10runs.png width="150"> |  <img src=./plots_images/50_100/k01/run2_50_100_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/50_100/k0/run7_50_100_10runs.png width="150"> |  <img src=./plots_images/50_100/k01/run7_50_100_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/50_100/k0/run3_50_100_10runs.png width="150"> |  <img src=./plots_images/50_100/k01/run3_50_100_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/50_100/k0/run8_50_100_10runs.png width="150"> |  <img src=./plots_images/50_100/k01/run8_50_100_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/50_100/k0/run4_50_100_10runs.png width="150"> |  <img src=./plots_images/50_100/k01/run4_50_100_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/50_100/k0/run9_50_100_10runs.png width="150"> |  <img src=./plots_images/50_100/k01/run9_50_100_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/50_100/k0/run5_50_100_10runs.png width="150"> |  <img src=./plots_images/50_100/k01/run5_50_100_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/50_100/k0/run10_50_100_10runs.png width="150">|  <img src=./plots_images/50_100/k01/run10_50_100_10runs_entropy.png width="150">|  
  
 
### Table 3 : focus 50 Classification 200

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/50_200/k0/run1_50_200_10runs.png width="150"> |  <img src=./plots_images/50_200/k01/run1_50_200_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/50_200/k0/run6_50_200_10runs.png width="150"> |  <img src=./plots_images/50_200/k01/run6_50_200_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/50_200/k0/run2_50_200_10runs.png width="150"> |  <img src=./plots_images/50_200/k01/run2_50_200_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/50_200/k0/run7_50_200_10runs.png width="150"> |  <img src=./plots_images/50_200/k01/run7_50_200_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/50_200/k0/run3_50_200_10runs.png width="150"> |  <img src=./plots_images/50_200/k01/run3_50_200_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/50_200/k0/run8_50_200_10runs.png width="150"> |  <img src=./plots_images/50_200/k01/run8_50_200_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/50_200/k0/run4_50_200_10runs.png width="150"> |  <img src=./plots_images/50_200/k01/run4_50_200_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/50_200/k0/run9_50_200_10runs.png width="150"> |  <img src=./plots_images/50_200/k01/run9_50_200_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/50_200/k0/run5_50_200_10runs.png width="150"> |  <img src=./plots_images/50_200/k01/run5_50_200_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/50_200/k0/run10_50_200_10runs.png width="150">|  <img src=./plots_images/50_200/k01/run10_50_200_10runs_entropy.png width="150">|  
  

### Table 4 : focus 50 Classification 300

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/50_300/k0/run1_50_300_10runs.png width="150"> |  <img src=./plots_images/50_300/k01/run1_50_300_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/50_300/k0/run6_50_300_10runs.png width="150"> |  <img src=./plots_images/50_300/k01/run6_50_300_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/50_300/k0/run2_50_300_10runs.png width="150"> |  <img src=./plots_images/50_300/k01/run2_50_300_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/50_300/k0/run7_50_300_10runs.png width="150"> |  <img src=./plots_images/50_300/k01/run7_50_300_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/50_300/k0/run3_50_300_10runs.png width="150"> |  <img src=./plots_images/50_300/k01/run3_50_300_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/50_300/k0/run8_50_300_10runs.png width="150"> |  <img src=./plots_images/50_300/k01/run8_50_300_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/50_300/k0/run4_50_300_10runs.png width="150"> |  <img src=./plots_images/50_300/k01/run4_50_300_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/50_300/k0/run9_50_300_10runs.png width="150"> |  <img src=./plots_images/50_300/k01/run9_50_300_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/50_300/k0/run5_50_300_10runs.png width="150"> |  <img src=./plots_images/50_300/k01/run5_50_300_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/50_300/k0/run10_50_300_10runs.png width="150">|  <img src=./plots_images/50_300/k01/run10_50_300_10runs_entropy.png width="150">|  

### Table 5 : focus 100 Classification 50

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/100_50/k0/run1_100_50_10runs.png width="150"> |  <img src=./plots_images/100_50/k01/run1_100_50_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/100_50/k0/run6_100_50_10runs.png width="150"> |  <img src=./plots_images/100_50/k01/run6_100_50_10runs_entropy.png width="150"> |   
| Run 2  | <img src=./plots_images/100_50/k0/run2_100_50_10runs.png width="150"> |  <img src=./plots_images/100_50/k01/run2_100_50_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/100_50/k0/run7_100_50_10runs.png width="150"> |  <img src=./plots_images/100_50/k01/run7_100_50_10runs_entropy.png width="150"> |   
| Run 3  | <img src=./plots_images/100_50/k0/run3_100_50_10runs.png width="150"> |  <img src=./plots_images/100_50/k01/run3_100_50_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/100_50/k0/run8_100_50_10runs.png width="150"> |  <img src=./plots_images/100_50/k01/run8_100_50_10runs_entropy.png width="150"> |   
| Run 4  | <img src=./plots_images/100_50/k0/run4_100_50_10runs.png width="150"> |  <img src=./plots_images/100_50/k01/run4_100_50_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/100_50/k0/run9_100_50_10runs.png width="150"> |  <img src=./plots_images/100_50/k01/run9_100_50_10runs_entropy.png width="150"> |   
| Run 5  | <img src=./plots_images/100_50/k0/run5_100_50_10runs.png width="150"> |  <img src=./plots_images/100_50/k01/run5_100_50_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/100_50/k0/run10_100_50_10runs.png width="150">|  <img src=./plots_images/100_50/k01/run10_100_50_10runs_entropy.png width="150">|   
 
 
### Table 6 : focus 100 Classification 100

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/100_100/k0/run1_100_100_10runs.png width="150"> |  <img src=./plots_images/100_100/k01/run1_100_100_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/100_100/k0/run6_100_100_10runs.png width="150"> |  <img src=./plots_images/100_100/k01/run6_100_100_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/100_100/k0/run2_100_100_10runs.png width="150"> |  <img src=./plots_images/100_100/k01/run2_100_100_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/100_100/k0/run7_100_100_10runs.png width="150"> |  <img src=./plots_images/100_100/k01/run7_100_100_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/100_100/k0/run3_100_100_10runs.png width="150"> |  <img src=./plots_images/100_100/k01/run3_100_100_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/100_100/k0/run8_100_100_10runs.png width="150"> |  <img src=./plots_images/100_100/k01/run8_100_100_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/100_100/k0/run4_100_100_10runs.png width="150"> |  <img src=./plots_images/100_100/k01/run4_100_100_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/100_100/k0/run9_100_100_10runs.png width="150"> |  <img src=./plots_images/100_100/k01/run9_100_100_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/100_100/k0/run5_100_100_10runs.png width="150"> |  <img src=./plots_images/100_100/k01/run5_100_100_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/100_100/k0/run10_100_100_10runs.png width="150">|  <img src=./plots_images/100_100/k01/run10_100_100_10runs_entropy.png width="150">|  
  
 
### Table 7 : focus 100 Classification 200

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/100_200/k0/run1_100_200_10runs.png width="150"> |  <img src=./plots_images/100_200/k01/run1_100_200_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/100_200/k0/run6_100_200_10runs.png width="150"> |  <img src=./plots_images/100_200/k01/run6_100_200_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/100_200/k0/run2_100_200_10runs.png width="150"> |  <img src=./plots_images/100_200/k01/run2_100_200_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/100_200/k0/run7_100_200_10runs.png width="150"> |  <img src=./plots_images/100_200/k01/run7_100_200_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/100_200/k0/run3_100_200_10runs.png width="150"> |  <img src=./plots_images/100_200/k01/run3_100_200_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/100_200/k0/run8_100_200_10runs.png width="150"> |  <img src=./plots_images/100_200/k01/run8_100_200_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/100_200/k0/run4_100_200_10runs.png width="150"> |  <img src=./plots_images/100_200/k01/run4_100_200_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/100_200/k0/run9_100_200_10runs.png width="150"> |  <img src=./plots_images/100_200/k01/run9_100_200_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/100_200/k0/run5_100_200_10runs.png width="150"> |  <img src=./plots_images/100_200/k01/run5_100_200_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/100_200/k0/run10_100_200_10runs.png width="150">|  <img src=./plots_images/100_200/k01/run10_100_200_10runs_entropy.png width="150">|  
  

### Table 8 : focus 100 Classification 300

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/100_300/k0/run1_100_300_10runs.png width="150"> |  <img src=./plots_images/100_300/k01/run1_100_300_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/100_300/k0/run6_100_300_10runs.png width="150"> |  <img src=./plots_images/100_300/k01/run6_100_300_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/100_300/k0/run2_100_300_10runs.png width="150"> |  <img src=./plots_images/100_300/k01/run2_100_300_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/100_300/k0/run7_100_300_10runs.png width="150"> |  <img src=./plots_images/100_300/k01/run7_100_300_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/100_300/k0/run3_100_300_10runs.png width="150"> |  <img src=./plots_images/100_300/k01/run3_100_300_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/100_300/k0/run8_100_300_10runs.png width="150"> |  <img src=./plots_images/100_300/k01/run8_100_300_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/100_300/k0/run4_100_300_10runs.png width="150"> |  <img src=./plots_images/100_300/k01/run4_100_300_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/100_300/k0/run9_100_300_10runs.png width="150"> |  <img src=./plots_images/100_300/k01/run9_100_300_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/100_300/k0/run5_100_300_10runs.png width="150"> |  <img src=./plots_images/100_300/k01/run5_100_300_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/100_300/k0/run10_100_300_10runs.png width="150">|  <img src=./plots_images/100_300/k01/run10_100_300_10runs_entropy.png width="150">|  
  

### Table 9 : focus 200 Classification 50

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/200_50/k0/run1_200_50_10runs.png width="150"> |  <img src=./plots_images/200_50/k01/run1_200_50_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/200_50/k0/run6_200_50_10runs.png width="150"> |  <img src=./plots_images/200_50/k01/run6_200_50_10runs_entropy.png width="150"> |   
| Run 2  | <img src=./plots_images/200_50/k0/run2_200_50_10runs.png width="150"> |  <img src=./plots_images/200_50/k01/run2_200_50_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/200_50/k0/run7_200_50_10runs.png width="150"> |  <img src=./plots_images/200_50/k01/run7_200_50_10runs_entropy.png width="150"> |   
| Run 3  | <img src=./plots_images/200_50/k0/run3_200_50_10runs.png width="150"> |  <img src=./plots_images/200_50/k01/run3_200_50_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/200_50/k0/run8_200_50_10runs.png width="150"> |  <img src=./plots_images/200_50/k01/run8_200_50_10runs_entropy.png width="150"> |   
| Run 4  | <img src=./plots_images/200_50/k0/run4_200_50_10runs.png width="150"> |  <img src=./plots_images/200_50/k01/run4_200_50_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/200_50/k0/run9_200_50_10runs.png width="150"> |  <img src=./plots_images/200_50/k01/run9_200_50_10runs_entropy.png width="150"> |   
| Run 5  | <img src=./plots_images/200_50/k0/run5_200_50_10runs.png width="150"> |  <img src=./plots_images/200_50/k01/run5_200_50_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/200_50/k0/run10_200_50_10runs.png width="150">|  <img src=./plots_images/200_50/k01/run10_200_50_10runs_entropy.png width="150">|   
 
 
### Table 10 : focus 200 Classification 100

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/200_100/k0/run1_200_100_10runs.png width="150"> |  <img src=./plots_images/200_100/k01/run1_200_100_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/200_100/k0/run6_200_100_10runs.png width="150"> |  <img src=./plots_images/200_100/k01/run6_200_100_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/200_100/k0/run2_200_100_10runs.png width="150"> |  <img src=./plots_images/200_100/k01/run2_200_100_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/200_100/k0/run7_200_100_10runs.png width="150"> |  <img src=./plots_images/200_100/k01/run7_200_100_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/200_100/k0/run3_200_100_10runs.png width="150"> |  <img src=./plots_images/200_100/k01/run3_200_100_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/200_100/k0/run8_200_100_10runs.png width="150"> |  <img src=./plots_images/200_100/k01/run8_200_100_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/200_100/k0/run4_200_100_10runs.png width="150"> |  <img src=./plots_images/200_100/k01/run4_200_100_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/200_100/k0/run9_200_100_10runs.png width="150"> |  <img src=./plots_images/200_100/k01/run9_200_100_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/200_100/k0/run5_200_100_10runs.png width="150"> |  <img src=./plots_images/200_100/k01/run5_200_100_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/200_100/k0/run10_200_100_10runs.png width="150">|  <img src=./plots_images/200_100/k01/run10_200_100_10runs_entropy.png width="150">|  
  
 
### Table 11 : focus 200 Classification 200

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/200_200/k0/run1_200_200_10runs.png width="150"> |  <img src=./plots_images/200_200/k01/run1_200_200_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/200_200/k0/run6_200_200_10runs.png width="150"> |  <img src=./plots_images/200_200/k01/run6_200_200_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/200_200/k0/run2_200_200_10runs.png width="150"> |  <img src=./plots_images/200_200/k01/run2_200_200_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/200_200/k0/run7_200_200_10runs.png width="150"> |  <img src=./plots_images/200_200/k01/run7_200_200_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/200_200/k0/run3_200_200_10runs.png width="150"> |  <img src=./plots_images/200_200/k01/run3_200_200_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/200_200/k0/run8_200_200_10runs.png width="150"> |  <img src=./plots_images/200_200/k01/run8_200_200_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/200_200/k0/run4_200_200_10runs.png width="150"> |  <img src=./plots_images/200_200/k01/run4_200_200_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/200_200/k0/run9_200_200_10runs.png width="150"> |  <img src=./plots_images/200_200/k01/run9_200_200_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/200_200/k0/run5_200_200_10runs.png width="150"> |  <img src=./plots_images/200_200/k01/run5_200_200_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/200_200/k0/run10_200_200_10runs.png width="150">|  <img src=./plots_images/200_200/k01/run10_200_200_10runs_entropy.png width="150">|  
  

### Table 12 : focus 200 Classification 300

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/200_300/k0/run1_200_300_10runs.png width="150"> |  <img src=./plots_images/200_300/k01/run1_200_300_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/200_300/k0/run6_200_300_10runs.png width="150"> |  <img src=./plots_images/200_300/k01/run6_200_300_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/200_300/k0/run2_200_300_10runs.png width="150"> |  <img src=./plots_images/200_300/k01/run2_200_300_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/200_300/k0/run7_200_300_10runs.png width="150"> |  <img src=./plots_images/200_300/k01/run7_200_300_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/200_300/k0/run3_200_300_10runs.png width="150"> |  <img src=./plots_images/200_300/k01/run3_200_300_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/200_300/k0/run8_200_300_10runs.png width="150"> |  <img src=./plots_images/200_300/k01/run8_200_300_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/200_300/k0/run4_200_300_10runs.png width="150"> |  <img src=./plots_images/200_300/k01/run4_200_300_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/200_300/k0/run9_200_300_10runs.png width="150"> |  <img src=./plots_images/200_300/k01/run9_200_300_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/200_300/k0/run5_200_300_10runs.png width="150"> |  <img src=./plots_images/200_300/k01/run5_200_300_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/200_300/k0/run10_200_300_10runs.png width="150">|  <img src=./plots_images/200_300/k01/run10_200_300_10runs_entropy.png width="150">|  
  

### Table 13 : focus 300 Classification 50

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/300_50/k0/run1_300_50_10runs.png width="150"> |  <img src=./plots_images/300_50/k01/run1_300_50_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/300_50/k0/run6_300_50_10runs.png width="150"> |  <img src=./plots_images/300_50/k01/run6_300_50_10runs_entropy.png width="150"> |   
| Run 2  | <img src=./plots_images/300_50/k0/run2_300_50_10runs.png width="150"> |  <img src=./plots_images/300_50/k01/run2_300_50_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/300_50/k0/run7_300_50_10runs.png width="150"> |  <img src=./plots_images/300_50/k01/run7_300_50_10runs_entropy.png width="150"> |   
| Run 3  | <img src=./plots_images/300_50/k0/run3_300_50_10runs.png width="150"> |  <img src=./plots_images/300_50/k01/run3_300_50_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/300_50/k0/run8_300_50_10runs.png width="150"> |  <img src=./plots_images/300_50/k01/run8_300_50_10runs_entropy.png width="150"> |   
| Run 4  | <img src=./plots_images/300_50/k0/run4_300_50_10runs.png width="150"> |  <img src=./plots_images/300_50/k01/run4_300_50_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/300_50/k0/run9_300_50_10runs.png width="150"> |  <img src=./plots_images/300_50/k01/run9_300_50_10runs_entropy.png width="150"> |   
| Run 5  | <img src=./plots_images/300_50/k0/run5_300_50_10runs.png width="150"> |  <img src=./plots_images/300_50/k01/run5_300_50_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/300_50/k0/run10_300_50_10runs.png width="150">|  <img src=./plots_images/300_50/k01/run10_300_50_10runs_entropy.png width="150">|   
 
 
### Table 14 : focus 300 Classification 100

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/300_100/k0/run1_300_100_10runs.png width="150"> |  <img src=./plots_images/300_100/k01/run1_300_100_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/300_100/k0/run6_300_100_10runs.png width="150"> |  <img src=./plots_images/300_100/k01/run6_300_100_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/300_100/k0/run2_300_100_10runs.png width="150"> |  <img src=./plots_images/300_100/k01/run2_300_100_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/300_100/k0/run7_300_100_10runs.png width="150"> |  <img src=./plots_images/300_100/k01/run7_300_100_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/300_100/k0/run3_300_100_10runs.png width="150"> |  <img src=./plots_images/300_100/k01/run3_300_100_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/300_100/k0/run8_300_100_10runs.png width="150"> |  <img src=./plots_images/300_100/k01/run8_300_100_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/300_100/k0/run4_300_100_10runs.png width="150"> |  <img src=./plots_images/300_100/k01/run4_300_100_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/300_100/k0/run9_300_100_10runs.png width="150"> |  <img src=./plots_images/300_100/k01/run9_300_100_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/300_100/k0/run5_300_100_10runs.png width="150"> |  <img src=./plots_images/300_100/k01/run5_300_100_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/300_100/k0/run10_300_100_10runs.png width="150">|  <img src=./plots_images/300_100/k01/run10_300_100_10runs_entropy.png width="150">|  
  
 
### Table 15 : focus 300 Classification 200

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/300_200/k0/run1_300_200_10runs.png width="150"> |  <img src=./plots_images/300_200/k01/run1_300_200_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/300_200/k0/run6_300_200_10runs.png width="150"> |  <img src=./plots_images/300_200/k01/run6_300_200_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/300_200/k0/run2_300_200_10runs.png width="150"> |  <img src=./plots_images/300_200/k01/run2_300_200_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/300_200/k0/run7_300_200_10runs.png width="150"> |  <img src=./plots_images/300_200/k01/run7_300_200_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/300_200/k0/run3_300_200_10runs.png width="150"> |  <img src=./plots_images/300_200/k01/run3_300_200_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/300_200/k0/run8_300_200_10runs.png width="150"> |  <img src=./plots_images/300_200/k01/run8_300_200_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/300_200/k0/run4_300_200_10runs.png width="150"> |  <img src=./plots_images/300_200/k01/run4_300_200_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/300_200/k0/run9_300_200_10runs.png width="150"> |  <img src=./plots_images/300_200/k01/run9_300_200_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/300_200/k0/run5_300_200_10runs.png width="150"> |  <img src=./plots_images/300_200/k01/run5_300_200_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/300_200/k0/run10_300_200_10runs.png width="150">|  <img src=./plots_images/300_200/k01/run10_300_200_10runs_entropy.png width="150">|  
  

### Table 16 : focus 300 Classification 300

| #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy | #Runs | loss = CE loss  |  loss = 0.9*CE + 0.1*entropy |
| -       | -  | - | -       | -  | - |
| Run 1  | <img src=./plots_images/300_300/k0/run1_300_300_10runs.png width="150"> |  <img src=./plots_images/300_300/k01/run1_300_300_10runs_entropy.png width="150"> | Run 6  | <img src=./plots_images/300_300/k0/run6_300_300_10runs.png width="150"> |  <img src=./plots_images/300_300/k01/run6_300_300_10runs_entropy.png width="150"> |  
| Run 2  | <img src=./plots_images/300_300/k0/run2_300_300_10runs.png width="150"> |  <img src=./plots_images/300_300/k01/run2_300_300_10runs_entropy.png width="150"> | Run 7  | <img src=./plots_images/300_300/k0/run7_300_300_10runs.png width="150"> |  <img src=./plots_images/300_300/k01/run7_300_300_10runs_entropy.png width="150"> |  
| Run 3  | <img src=./plots_images/300_300/k0/run3_300_300_10runs.png width="150"> |  <img src=./plots_images/300_300/k01/run3_300_300_10runs_entropy.png width="150"> | Run 8  | <img src=./plots_images/300_300/k0/run8_300_300_10runs.png width="150"> |  <img src=./plots_images/300_300/k01/run8_300_300_10runs_entropy.png width="150"> |  
| Run 4  | <img src=./plots_images/300_300/k0/run4_300_300_10runs.png width="150"> |  <img src=./plots_images/300_300/k01/run4_300_300_10runs_entropy.png width="150"> | Run 9  | <img src=./plots_images/300_300/k0/run9_300_300_10runs.png width="150"> |  <img src=./plots_images/300_300/k01/run9_300_300_10runs_entropy.png width="150"> |  
| Run 5  | <img src=./plots_images/300_300/k0/run5_300_300_10runs.png width="150"> |  <img src=./plots_images/300_300/k01/run5_300_300_10runs_entropy.png width="150"> | Run 10 | <img src=./plots_images/300_300/k0/run10_300_300_10runs.png width="150">|  <img src=./plots_images/300_300/k01/run10_300_300_10runs_entropy.png width="150">|  

