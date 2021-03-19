### effects of complexity on interpretability

#### Table 1: Synthetic elliptical blobs data (Single run)

| fcs\cls | 100 | 200 | 300 |
| -       | -   | -   |  -  |  
|  50     |  <img src=./plots_images/trends_synthetic_50_100.png width="800">   |  <img src=./plots_images/trends_synthetic_50_200.png width="800">   |  <img src=./plots_images/trends_synthetic_50_300.png width="800">   |    
| 100     |  <img src=./plots_images/trends_synthetic_100_100.png width="800">   |    <img src=./plots_images/trends_synthetic_100_200.png width="800"> |  <img src=./plots_images/trends_synthetic_100_300.png width="800">   |   
| 200     |  <img src=./plots_images/trends_synthetic_200_100.png width="800">   |  <img src=./plots_images/trends_synthetic_200_200.png width="800">   |  <img src=./plots_images/trends_synthetic_200_300.png width="800">   |  
| 300     |  <img src=./plots_images/trends_synthetic_300_100.png width="800">   |  <img src=./plots_images/trends_synthetic_300_200.png width="800">   |  <img src=./plots_images/trends_synthetic_300_300.png width="800">   | 


<!---#### MNIST DATA
70
| fcs\cls | 100 | 200 | 300 |
| -       | -   | -   |  -  |  
|  50     |  <img src=./plots_images/trends_mnist_50_100.png width="800">   |  <img src=./plots_images/trends_mnist_50_200.png width="800">   |  <img src=./plots_images/trends_mnist_50_300.png width="800">   |    
| 100     |  <img src=./plots_images/trends_mnist_100_100.png width="800">   |    <img src=./plots_images/trends_mnist_100_200.png width="800"> |  <img src=./plots_images/trends_mnist_100_300.png width="800">   |   
| 200     |  <img src=./plots_images/trends_mnist_200_100.png width="800">   |  <img src=./plots_images/trends_mnist_200_200.png width="800">   |  <img src=./plots_images/trends_mnist_200_300.png width="800">   |  
| 300     |  <img src=./plots_images/trends_mnist_300_100.png width="800">   |  <img src=./plots_images/trends_mnist_300_200.png width="800">   |  <img src=./plots_images/trends_mnist_300_300.png width="800">   | --->

#### type 4 data
<img src=./plots_images/type4_distr.JPG width="250">   

Hypothesis - Increasing the classification network complexity, while keeping the focus network fixed decreases interpretability (As shown below for zeroth layer averaging). In the case of feature extracted from some other layer for averaging say first layer we are observing similar results but still needs to discuss some things (like as we change the complexity of focus network input to classification network changes in that case how to interpret the results ). One hidden layer model is used with specified hidden units.
#### zeroth layer averaging
###### Table 2: FTPT values averaged over 20 runs
| fcs\cls | 10  | 20  | 50 | 100 | 200 | 300 |
| -----   | --  |  -- | -- | --  | --  | --  | 
| 10      |   57.1 |  63.02   |  58.17  | 58.035    |  59.31   | 58.27 |
| 20      | 79.708    | 74.59    |  72.94  |  71.66   |  72.65   | 62.348 | 
| 50      |  82.06   | 82.90    | 75.51   |  74.44   |  69.82   | 70.13 | 
| 100      | 81.86    |  84.9   |  79.81  |  74.8   | 69.78    |  69.44| 
| 200      | 69.35    | 77.734   | 76.7   |  71.24   |  69.01   | 69.59 |
| 300      |  51.08   | 66.126    |   66.19 |  71.30   |  72.57   | 71.39 |

###### Table 3: FFPT values averaged over 20 runs
| fcs\cls | 10  | 20  | 50 | 100 | 200 | 300 |
| -----   | --  |  -- | -- | --  | --  | --  | 
| 10      |   28.13  |  27.12   |  29.51  |   31.53  |   30.77  | 33.28 |
| 20      |    18.86 |   25.22  |  26.94  |  28.16   |   27.18  | 30.165 | 
| 50      |  17.85   |  16.99   |  24.37   |  25.44   |  29.99   | 29.68  | 
| 100      |  12.64   |   14.9  |  20.08  |  25.06   | 30.06    |  30.39 | 
| 200      |  16.635   |  17.9   |   23.2 |   26.11  |  30.84   | 30.26 |
| 300      | 27.62    |   22.87  |  26.85  |   26.45  |  27.34   | 28.52 |

#### first layer averaging
For the first layer averaging we take features from output of first layer and use tanh activation function.

###### Table 4: FTPT values averaged over 20 runs
| fcs\cls | 10  | 20  | 50 | 100 | 200 | 300 |
| -----   | --  |  -- | -- | --  | --  | --  | 
| 10      |  81.26  |  79.74   | 80.81  |  75.69   |  78.97   | 79.16 |
| 20      |  76.32  |  75.90   | 71.78  | 72.398   |   72.015  | 76.42 | 
| 50      |   88.703  |  84.93   |   81.77  |  77.40   |  75.24  |  74.73 | 
| 100      | 83.08 (FFPF 9)  |  83.97(FFPF 6)   |  89.63  |   82.175  | 82.24    | 82.12  | 
| 200      |  32.415(FFPF 40.61)  | 55.34  |  47.88  | 67.26    | 77.415    | 71.50 |
| 300      |  -  |  - |  - | -    | 62.47 | 66.435 |

###### Table 5: FFPT values averaged over 20 runs
| fcs\cls | 10  | 20  | 50 | 100 | 200 | 300 |
| -----   | --  |  -- | -- | --  | --  | --  | 
| 10      |  18.5   | 20.12    | 19.003  |  24.11   |  20.85  | 20.64 |
| 20      |   17.265  |  23.93   |  28.040  |  27.40   |  27.78   | 23.38 | 
| 50      |  8.03   | 11.821    |   18.09  |  22.43   |  24.58  | 25.09  | 
| 100      |  7.34  | 9.62    |  10.25  |  17.71   | 17.60    |  17.72 | 
| 200      |  26.47  | 19.32  |  23.58  |  19.99   |  19.27   | 22.028 |
| 300      |   - |   -|  - |  -   | 22.115 | 27.098 |

[Sheet Link](https://docs.google.com/spreadsheets/d/1tKNCt3RkObySddCjx20FONrXO065BFwxu5SmSxtP5w0/edit#gid=0)
