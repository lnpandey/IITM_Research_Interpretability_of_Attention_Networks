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
![](./plots_and_images/train_table.JPG)

### Table 5 : Observation Table for Testing Dataset 1
![](./plots_and_images/test_table1.JPG)

### Table 6 : Observation Table for Testing Dataset 2
![](./plots_and_images/test_table2.JPG)

### Table 7 : Observation Table for Testing Dataset 3
![](./plots_and_images/test_table3.JPG)

### Table 8 : Observation Table for Testing Dataset 4
![](./plots_and_images/test_table4.JPG)







### Table 9 : Observation Table for Training Dataset
| gamma | Avg Accuracy | Avg FTPT | Avg FFPT | Avg FTPF | Avg FFPF |
|-------|--------------|----------|----------|----------|--------------|
| 0     | 98.756   | 76.7397  | 22.0163 | 0.319667   | 0.924333 |
| 0.001 | 98.6857 | 76.4147  | 22.271  | 0.317333  | 0.997     |   
| 0.002 | 98.5367 | 77.6737  | 20.863  | 0.339     | 1.12433   |      
| 0.004 | 99.11   | 60.755   | 38.355  | 0.483     | 0.407     |    
| 0.008 | 98.725  | 77.803   | 20.922  | 1.18433   | 0.0906667 |        
| 0.016 | 98.8773 | 65.7233  | 33.154  | 0.882333  | 0.240333  |     
| 0.032 | 99.0077 | 50.7923  | 48.2153 | 0.578333  | 0.414     |     
| 0.064 | 99.0357 | 60.2253  | 38.8103 | 0.597333  | 0.367     |      
| 0.128 | 99.4077 | 82.0323  | 17.3753 | 0.504667  | 0.0876667 |            
| 0.256 | 99.421  | 89.9097  | 9.51133 |  0.476333 | 0.102667 |            
| 0.512 | 99.5447 | 99.4433  | 0.101333| 0.455333  |      0    |     
     

### Table 10 : Observation Table for Testing Dataset 1
| gamma | Avg Accuracy | Avg FTPT | Avg FFPT | Avg FTPF | Avg FFPF |
|-------|--------------|----------|----------|----------|--------------|
| 0     | 85.773 |  69.683 |   16.09 |    3.85  | 10.377 |         
| 0.001 | 85.728 |  68.771 |  16.957 |  3.794 | 10.478 |         
| 0.002 | 87.518 |  70.606 |  16.912 |  3.273 |  9.209 |         
| 0.004 | 98.452 |  60.912 |   37.54 |  0.946 |  0.602 |         
| 0.008 | 98.045 |  76.981 |  21.064 |  1.814 |  0.141 |          
| 0.016 | 98.107 |  64.603 |  33.504 |  1.564 |  0.329 |         
| 0.032 | 98.76  | 50.562  | 48.198  | 0.735  | 0.505  |        
| 0.064 | 98.84  | 60.053  | 38.787  | 0.793  | 0.367  |        
| 0.128 | 99.294 |  82.253 |  17.041 |  0.603 |  0.103 |         
| 0.256 | 99.341 | 89.906  | 9.435   | 0.535  | 0.124 |          
| 0.512 | 99.463 |  99.365 |   0.098 |  0.536 |  0.001 |         


### Table 11 : Observation Table for Testing Dataset 2
| gamma | Avg Accuracy | Avg FTPT | Avg FFPT | Avg FTPF | Avg FFPF |
|-------|--------------|----------|----------|----------|--------------|
| 0     | 65.97  | 46.855  |19.115  | 9.633   | 24.397   |         
| 0.001 | 66.284 | 46.523 | 19.761 |   9.35 | 24.366 |        
| 0.002 | 69.488 | 49.118 |  20.37 |  8.104 | 22.408 |         
| 0.004 | 96.584 |  57.35 | 39.234 |  2.624 |  0.792 |         
| 0.008 | 96.384 | 75.591 | 20.793 |  3.381 |  0.235 |         
| 0.016 | 96.852 | 63.381 | 33.471 |  2.775 |  0.373 |         
| 0.032 | 98.368 | 49.948 |  48.42 |  1.106 |  0.526 |         
| 0.064 | 98.712 | 59.957 | 38.755 |  0.915 |  0.373 |         
| 0.128 | 99.145 | 81.575 |  17.57 |  0.744 |  0.111 |         
| 0.256 | 99.322 |  89.71 |  9.612 |  0.578 |   0.1 |         
| 0.512 | 99.373 | 99.278 |  0.095 |  0.627 |      0 |         
     

### Table 12 : Observation Table for Testing Dataset 3
| gamma | Avg Accuracy | Avg FTPT | Avg FFPT | Avg FTPF | Avg FFPF |
|-------|--------------|----------|----------|----------|--------------|
| 0     | 86.124 | 70.164  |   15.96  |   3.664 |  10.212 |           
| 0.001 | 86.409  | 69.369  |  17.04 |  3.714  |  9.877 |          
| 0.002 | 82.944  | 66.508  | 16.436 |  6.527  | 10.529 |          
| 0.004 | 34.218  |  6.633  | 27.585 | 17.362  |  48.42 |         
| 0.008 | 33.143  |  5.765  | 27.378 |  8.944  | 57.913 |          
| 0.016 | 33.085  |  4.783  | 28.302 |  9.336  | 57.579 |          
| 0.032 | 33.723  |  3.755  | 29.968 | 18.783  | 47.494 |          
| 0.064 | 34.061  |  3.974  | 30.087 | 10.362  | 55.577 |          
| 0.128 | 33.247  |  2.316  | 30.931 | 11.892  | 54.861 |          
| 0.256 | 33.299  | 4.108  | 29.191  | 9.992  | 56.709 |          
| 0.512 | 34.305  |  5.572  | 28.733 | 10.107  | 55.588 |          
         

### Table 13 : Observation Table for Testing Dataset 4
| gamma | Avg Accuracy | Avg FTPT | Avg FFPT | Avg FTPF | Avg FFPF |
|-------|--------------|----------|----------|----------|--------------|
| 0     | 65.97  | 46.855  | 19.115  |  9.633  | 24.397   |        
| 0.001 | 66.258 |  46.5  |  19.758 |   9.356 |  24.386 |       
| 0.002 | 64.663 | 44.776 |  19.887 |  10.979 |  24.358 |       
| 0.004 | 33.42  | 5.967  | 27.453  | 16.204  | 50.376  |      
| 0.008 | 32.901 |  5.626 |  27.275 |   8.285 |  58.814 |       
| 0.016 | 32.91  | 4.704  | 28.206  |  8.965  | 58.125  |      
| 0.032 | 32.843 |  3.369 |  29.474 |  18.642 |  48.515 |       
| 0.064 | 33.485 |  3.931 |  29.554 |   10.4  |  56.115 |       
| 0.128 | 33.759 |  2.234 |  31.525 |  12.869 |  53.372 |       
| 0.256 | 33.706 |  4.485 | 29.221 | 10.012 | 56.282 |       
| 0.512 | 34.162 |  5.553 |  28.609 |  10.333 |  55.505 |       
 
### Plots:
Plot for Training Accuracy

<!--- <img src= ./plots_and_images/train_acc.JPG width="400">
<img src= ./plots_and_images/test_all_1.JPG width="400">
<img src= ./plots_and_images/test_all_2.JPG width="400">
<img src= ./plots_and_images/test_all_3.JPG width="400">
<img src= ./plots_and_images/test_all_4.JPG width="400">
<img src= ./plots_and_images/train_vs_all_ftpt.JPG width="400">
<img src= ./plots_and_images/train_vs_all_ffpt.JPG width="400">
<img src= ./plots_and_images/train_vs_all_ftpf.JPG width="400">
<img src= ./plots_and_images/train_vs_all_ffpf.JPG width="400"> -->


