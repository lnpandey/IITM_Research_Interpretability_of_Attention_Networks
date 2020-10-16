##### Histogram of CIFAR True Training Dataset
![](./plots_and_images/hist_true_train.JPG)

##### Histogram of CIFAR True Testing Dataset
![](./plots_and_images/hist_true_test.JPG)

### Table 1 : Comparison of histogram with different gamma
| gamma | Histogram Training Dataset | Histogram Testing Dataset |
|---------|--------------------|-------------------------|
|0.001 |  <img src= ./plots_and_images/hist_001_train.JPG width="200"> |  <img src= ./plots_and_images/hist_001_test.JPG width="200"> |
|0.002 |  <img src= ./plots_and_images/hist_002_train.JPG width="200"> |  <img src= ./plots_and_images/hist_002_test.JPG width="200"> |
|0.004 |  <img src= ./plots_and_images/hist_004_train.JPG width="200"> |  <img src= ./plots_and_images/hist_004_test.JPG width="200"> |
|0.008 |  <img src= ./plots_and_images/hist_008_train.JPG width="200"> |  <img src= ./plots_and_images/hist_008_test.JPG width="200"> |
|0.016 |  <img src= ./plots_and_images/hist_016_train.JPG width="200"> |  <img src= ./plots_and_images/hist_016_test.JPG width="200"> |
|0.032 |  <img src= ./plots_and_images/hist_032_train.JPG width="200"> |  <img src= ./plots_and_images/hist_032_test.JPG width="200"> |
|0.064 |  <img src= ./plots_and_images/hist_064_train.JPG width="200"> |  <img src= ./plots_and_images/hist_064_test.JPG width="200"> |
|0.128 |  <img src= ./plots_and_images/hist_128_train.JPG width="200"> |  <img src= ./plots_and_images/hist_128_test.JPG width="200"> |
|0.256 |  <img src= ./plots_and_images/hist_256_train.JPG width="200"> |  <img src= ./plots_and_images/hist_256_test.JPG width="200"> |
|0.512 |  <img src= ./plots_and_images/hist_512_train.JPG width="200"> |  <img src= ./plots_and_images/hist_512_test.JPG width="200"> |

### Table 2 : Display of u1, u2, u3 vectors as images
| u1 | u2 | u3 |
|----|-----|-----------|
|<img src= ./plots_and_images/u1.JPG width="300"> | <img src= ./plots_and_images/u2.JPG width="300"> | <img src= ./plots_and_images/u3.JPG width="300"> |


### Table 3 : Comparison of True vs corrupted images with different gamma
| gamma | true vs corrupted images |
|---------|----------------------------------------|
|0.001 |  <img src= ./plots_and_images/img_001.JPG width="200"> |
|0.002 |  <img src= ./plots_and_images/img_002.JPG width="200"> |
|0.004 |  <img src= ./plots_and_images/img_004.JPG width="200"> |
|0.008 |  <img src= ./plots_and_images/img_008.JPG width="200"> |
|0.016 |  <img src= ./plots_and_images/img_016.JPG width="200"> |
|0.032 |  <img src= ./plots_and_images/img_032.JPG width="200"> |
|0.064 |  <img src= ./plots_and_images/img_064.JPG width="200"> |
|0.128 |  <img src= ./plots_and_images/img_128.JPG width="200"> |
|0.256 |  <img src= ./plots_and_images/img_256.JPG width="200"> |
|0.512 |  <img src= ./plots_and_images/img_512.JPG width="200"> |

### Description of Dataset :
1. Training Dataset : 30k mosaic images from 50k modified CIFAR Train

2. Test Dataset 1 : 10k mosaic images from 50k modified CIFAR Train

3. Test Dataset 2 : 10k mosaic images from 10k modified CIFAR Test

4. Test Dataset 3 : 10k mosaic images from 50k True CIFAR Train

5. Test Dataset 4 : 10k mosaic images from 10k True CIFAR Test

### Table 4 : Observation Table for Training Dataset
| gamma | Avg Accuracy | Avg FTPT | Avg FFPT | Avg FTPF | Avg FFPF |
|-------|--------------|----------|----------|----------|--------------|
| 0     | 98.756   | 76.7397  | 22.0163 | 0.319667   | 0.924333 |
| 0.005 | 98.9857  | 74.2097  | 24.776  | 0.925      | 0.089333 |       
| 0.01  | 99.002   | 76.433   | 22.569  | 0.886667   | 0.111333 |        
| 0.015 | 98.7997  | 61.5663  | 37.2333 | 0.740333   | 0.46     |        
| 0.02  | 98.98    | 57.887   | 41.093  | 0.628      | 0.392    |        
| 0.025 | 99.173   | 62.2177  | 36.9553 | 0.429667   | 0.397333 |      
| 0.03  | 98.71    | 53.6553  | 45.0547 | 0.739667   | 0.550333 |         
| 0.035 | 99.1983  | 63.9243  | 35.274  | 0.529      | 0.272667 |          
| 0.04  | 98.9313  | 56.3473  | 42.584  | 0.67333    | 0.395333 |            
| 0.045 | 99.071   | 52.6753  | 46.3957 | 0.494333   | 0.434667 |         
| 0.05  | 99.2347  | 60.55    | 38.6847 | 0.575      | 0.190333 |        
| 0.055 | 98.9587  | 64.7017  | 34.257  | 0.833667   | 0.207667 |       
| 0.06  | 98.9387  | 56.4437  | 42.495  | 0.701667   | 0.359667 |        

### Table 5 : Observation Table for Testing Dataset 1
| gamma | Avg Accuracy | Avg FTPT | Avg FFPT | Avg FTPF | Avg FFPF |
|-------|--------------|----------|----------|----------|--------------|
| 0     | 85.773 |  69.683 |   16.09 |    3.85  | 10.377 |         
| 0.005 | 98.223 |  73.685 |  24.538 |   1.662  |  0.115 |         
| 0.01  | 98.571 |  75.689 |  22.882 |    1.31  |  0.119 |         
| 0.015 | 98.42  | 60.999  | 37.421  |  1.067   | 0.513  |         
| 0.02  | 98.743 |  57.141 |  41.602 |   0.832  |  0.425 |         
| 0.025 | 99.051 |  61.985 |  37.066 |    0.53  |  0.419 |         
| 0.03  | 98.38  | 53.292  | 45.088  |  1.032   | 0.588  |         
| 0.035 | 98.996 |  63.638 |  35.358 |    0.64  |  0.364 |         
| 0.04  | 98.753 |  56.262 |  42.491 |   0.791  |  0.456 |         
| 0.045 | 98.778 |  52.768 |   46.01 |   0.673  |  0.549 |         
| 0.05  | 99.153 |  60.547 |  38.606 |   0.638  |  0.209 |         
| 0.055 | 98.775 |  64.367 |  34.408 |   0.992  |  0.233 |         
| 0.06  | 98.674 |  56.151 |  42.523 |   0.871  |  0.455 |         

### Table 6 : Observation Table for Testing Dataset 2
| gamma | Avg Accuracy | Avg FTPT | Avg FFPT | Avg FTPF | Avg FFPF |
|-------|--------------|----------|----------|----------|--------------|
| 0     | 65.97  | 46.855  |19.115  | 9.633   | 24.397   |         
| 0.005 | 96.103 |  71.273 |  24.83 |  3.733  |   0.164  |        
| 0.01  | 97.203 |  74.321 | 22.882 |  2.635  |   0.162  |         
| 0.015 | 97.31  | 59.709  |37.601  | 2.196   |  0.494   |         
| 0.02  | 97.909 |  56.472 | 41.437 |  1.608  |   0.483  |         
| 0.025 | 98.693 |  61.548 | 37.145 |  0.821  |   0.486  |         
| 0.03  | 97.88  |  52.71  | 45.17  | 1.528   |  0.592   |         
| 0.035 | 98.781 |  63.123 | 35.658 |   0.81  |   0.409  |         
| 0.04  | 98.664 |  55.811 | 42.853 |  0.886  |    0.45  |         
| 0.045 | 98.581 |  52.182 | 46.399 |  0.791  |   0.628  |         
| 0.05  | 98.851 |  60.296 | 38.555 |   0.92  |   0.229  |         
| 0.055 | 98.692 |   64.49 | 34.202 |  1.101  |   0.207  |         
| 0.06  | 98.568 |  55.862 | 42.706 |  0.992  |    0.44  |         

### Table 7 : Observation Table for Testing Dataset 3
| gamma | Avg Accuracy | Avg FTPT | Avg FFPT | Avg FTPF | Avg FFPF |
|-------|--------------|----------|----------|----------|--------------|
| 0     | 86.124 | 70.164  |   15.96  |   3.664 |  10.212 |           
| 0.005 | 32.822 |  5.697  |  27.125  |   9.596 |  57.582 |           
| 0.01  | 34.003 |  5.879  |  28.124  |   8.003 |  57.994 |           
| 0.015 | 32.806 |  4.003  |  28.803  |  13.472 |  53.722 |          
| 0.02  | 33.164 |  3.963  |  29.201  |  11.644 |  55.192 |           
| 0.025 | 33.59  | 4.609   | 28.981   | 11.903  | 54.507  |           
| 0.03  | 33.417 |  4.084  |  29.333  |  12.319 |  54.264 |           
| 0.035 | 33.6   | 4.161   | 29.439   | 11.362  | 55.038  |           
| 0.04  | 32.869 |  3.292  |  29.577  |  14.803 |  52.328 |           
| 0.045 | 33.348 |  3.204  |  30.144  |  12.661 |  53.991 |           
| 0.05  | 33.002 |  4.183  |  28.819  |  11.963 |  55.035 |           
| 0.055 | 33.304 |  3.476  |  29.828  |   13.1  |  53.596 |           
| 0.06  | 33.934 |  3.555  |  30.379  |  12.844 |  53.222 |           

### Table 8 : Observation Table for Testing Dataset 4
| gamma | Avg Accuracy | Avg FTPT | Avg FFPT | Avg FTPF | Avg FFPF |
|-------|--------------|----------|----------|----------|--------------|
| 0     | 65.97  | 46.855  | 19.115  |  9.633  | 24.397   |        
| 0.005 | 32.994 |   5.422 |  27.572 |   9.005 |  58.001  |        
| 0.01  | 32.905 |   5.802 |  27.103 |   7.639 |  59.456  |        
| 0.015 | 32.895 |   3.957 |  28.938 |  13.224 |  53.881  |        
| 0.02  | 33.017 |    3.96 |  29.057 |   11.23 |  55.753  |        
| 0.025 | 32.801 |   4.386 |  28.415 |  11.542 |  55.657  |        
| 0.03  | 33.042 |   3.828 |  29.214 |   12.1  |  54.858  |        
| 0.035 | 32.915 |   3.868 |  29.047 |  11.079 |  56.006  |        
| 0.04  | 32.995 |   2.935 |   30.06 |   14.42 |  52.585  |        
| 0.045 | 33.035 |   3.108 |  29.927 |  12.707 |  54.258  |        
| 0.05  | 33.21  |  4.104  | 29.106  | 11.873  | 54.917   |        
| 0.055 | 32.99  |  3.147  | 29.843  |  13.11  |  53.9    |        
| 0.06  | 33.639 |   3.275 |  30.364 |  12.971 |   53.39  |        

### Plots:
Plot for Training Accuracy

<img src= ./plots_and_images/train_acc.JPG width="400">

<img src= ./plots_and_images/test_all_1.JPG width="400">
<img src= ./plots_and_images/test_all_2.JPG width="400">
<img src= ./plots_and_images/test_all_3.JPG width="400">
<img src= ./plots_and_images/test_all_4.JPG width="400">

<img src= ./plots_and_images/train_vs_all_ftpt.JPG width="400">
<img src= ./plots_and_images/train_vs_all_ffpt.JPG width="400">
<img src= ./plots_and_images/train_vs_all_ftpf.JPG width="400">
<img src= ./plots_and_images/train_vs_all_ffpf.JPG width="400">
