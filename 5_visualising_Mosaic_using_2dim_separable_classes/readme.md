# VISUALISING MOSAIC DATA BY GENERATING 2-DIM SEPARABLE DATA

### Generationtion of 10 Classes Using 2 Dimentional data 
  - We sampled 5000 (500 for every class approx) 2-dim data points from multivariate Normal with 10 different Mean vectors and same Covariance Matrix.
  - Covariance Matrix being the diagonal matrix with enteries [0.1, 0.1].

### Generation of Mosaic Data
- Available Classes = Class 0, Class 1, Class 2, Class 3, Class 4, Class 5, Class 6, Class 7, Class 8
- foreground_classes = Class 0, Class 1, Class 2
- background_classes = Class3, Class 4, Class 5, Class 6, Class 7, Class 8, Class 9
- Every class will have a 2-dim Data Point. 1 data point was chosen at random from any foreground class, and rest 8 data points are chosen from background classes
-  Now we have 9 datapoints which can be arranged randomly in 3 x 3 matrix. In particular Dimention of Matrix will be 3 x 6.
- Following is one of the mosaic image for the sake of visualisation:
![](./plots_and_images/sample_mosaic.png)

### MODEL
  - Model is developed as combination of 2 modules.
  - Module 1 learns "WHERE" the foreground image is present out of 9 images in Mosaic image.
  - Module 2 learns "WHAT" is the class of this foreground image out of those 3 foreground classes.

### Input to Model
- Mosaic image is input to Module 1 i.e "Where Network", and tries to focus on foreground image present in Mosaic Image.
- In Particular, Each image (2 x 1) is input to "Where Network" and hence a 18 x 1 tensor (9 images) is input to "Where Network".
- "Where Network" tries to Focus on Foreground image and returns weighted average of all 9 images.
- This image is now input to "What Network" which finally predicts the Class label of foreground Image.


### Visualising Different types of Generation of Classes through Scatter Plot :
##### Type 1 : Any 2 Classes are linearly separable
![](./plots_and_images/exp1_plot1.png)
##### Type 2 : Any 2 Foreground Classes are linearly separable, No Background Classes can be separable.
![](./plots_and_images/exp2_plot1.png)
##### Type 3 : Set of all Foreground Classes and set of all Background Classes are linearly separable. No 2 Background Classes or Foreground Classes can be separable.
![](./plots_and_images/exp3_plot1.png)
##### Type 4 : Foreground Classes are in Convex Hull of Background Classes. Any 2 Foreground Classes are linearly separable.
<img src= ./plots_and_images/exp4_plot1.JPG width="450"> 

##### Type 5 : For any classes, we have 2 Gaussian mixtures
<img src= ./plots_and_images/exp5_plot1.JPG width="450"> 



### Table 1: Analysis of Model on different Parameters
| Experiment No. | Total Epochs | "What" Learning Rate | "Where" Learning Rate | Training Accuracy  | Testing Accuracy |
|----------------|--------------|--------------------|---------------------|--------------------|------------------|
| Type 1 (architecture 1)       | 80          |  0.01               | 0.01                | 1               |1             |
| Type 2 (architecture 1)        | 10          |  0.01               | 0.01                | 1               |1             |
| Type 3 (architecture 1)        | 120         |  0.01               | 0.01                | 0.88            |0.89          |
| Type 4 (architecture 2)         | 164         |  0.01               | 0.01                | 0.99            | 0.99         |
| Type 5 (architecture 1)         | 150        |  0.01               | 0.01                | 0.99            | 0.99         |


### PLOTS For Experiments are as below:

| Dataset Type | Data visualisation | on training | on testing | testing Focus net |
|---------------|-------------------|-------------|------------|------------------|
| Type 1 |  <img src= ./plots_and_images/exp1_plot1.png width="400"> | <img src= ./plots_and_images/exp1_plot3.png width="400"> | <img src= ./plots_and_images/exp1_plot5.png width="400"> | <img src= ./plots_and_images/exp1_plot8.JPG width="400"> |
| Type 2 |  <img src= ./plots_and_images/exp2_plot1.png width="400"> | <img src= ./plots_and_images/exp2_plot3.png width="400"> | <img src= ./plots_and_images/exp2_plot5.png width="400"> | <img src= ./plots_and_images/exp2_plot8.JPG width="400"> |
| Type 3 |  <img src= ./plots_and_images/exp3_plot1.png width="400"> | <img src= ./plots_and_images/exp3_plot6.JPG width="400"> | <img src= ./plots_and_images/exp3_plot7.JPG width="400"> | <img src= ./plots_and_images/exp3_plot8.JPG width="400"> |
| Type 4 |  <img src= ./plots_and_images/exp4_plot1.JPG width="400"> | <img src= ./plots_and_images/exp4_plot2.JPG width="400"> | <img src= ./plots_and_images/exp4_plot3.JPG width="400"> | <img src= ./plots_and_images/testing_focus_net_500.JPG width="400"> |
| Type 5 |  <img src= ./plots_and_images/exp5_plot1.JPG width="400"> | <img src= ./plots_and_images/exp5_plot2.JPG width="400"> | <img src= ./plots_and_images/exp5_plot3.JPG width="400"> | <img src= ./plots_and_images/exp5_plot4.JPG width="400"> |

<!-- #### Experiment on TYPE 1: Total Epochs: 80, What lr: 0.01, Where lr: 0.01, train acc: 1, test acc: 1
  <!-- ![](./plots_and_images/exp1_plot2.png) 
  ![](./plots_and_images/exp1_plot3.png)
  <!-- ![](./plots_and_images/exp1_plot4.png) 
  ![](./plots_and_images/exp1_plot5.png)
  <img src= ./plots_and_images/exp1_plot8.JPG width="500">  
#### Experiment on TYPE 2: Total Epochs: 10, What lr: 0.01, Where lr: 0.01, train acc: 1, test acc: 1
  <!-- ![](./plots_and_images/exp2_plot2.png) 
  ![](./plots_and_images/exp2_plot3.png)
  <!-- ![](./plots_and_images/exp2_plot4.png) 
  ![](./plots_and_images/exp2_plot5.png)
  <img src= ./plots_and_images/exp2_plot8.JPG width="500">  
#### Experiment on TYPE 3: Total Epochs: 120, What lr: 0.01, Where lr: 0.01, train acc: 0.88, test acc: 0.89
  <!-- ![](./plots_and_images/exp3_plot2.png) 
  <img src= ./plots_and_images/exp3_plot6.JPG width="550"> 
  <!-- ![](./plots_and_images/exp3_plot4.png) 
  <img src= ./plots_and_images/exp3_plot7.JPG width="550">
  <img src= ./plots_and_images/exp3_plot8.JPG width="500">  
#### Experiment on TYPE 4: Total Epochs: 164, What lr: 0.01, Where lr: 0.01, train acc: 0.99, test acc: 0.99
  <img src= ./plots_and_images/exp4_plot2.JPG width="550"> 
  <img src= ./plots_and_images/exp4_plot3.JPG width="550"> 
  <img src= ./plots_and_images/testing_focus_net_100.JPG width="500">
  <img src= ./plots_and_images/testing_focus_net_500.JPG width="500">  
#### Experiment on TYPE 5: Total Epochs: 154, What lr: 0.01, Where lr: 0.01, train acc: 0.99, test acc: 0.99
  <img src= ./plots_and_images/exp5_plot2.JPG width="550"> 
  <img src= ./plots_and_images/exp5_plot3.JPG width="550"> 
  <img src= ./plots_and_images/exp5_plot4.JPG width="500"> -->
  
### Observation tables for Experiment "Testing Focus net with Dataset1-10" :

#### Table 1: for Type 1 Data
|   | test on dataset1 | test on dataset2 | test on dataset3 | test on dataset4 | test on dataset5 | test on dataset6 | test on dataset7 | test on dataset8 | test on dataset9| Train Accuracy |
|----------|-----|-----|-----|-----|-----|-----|-----|-----|----|----|
| train on dataset1      | 50 | 55 | 59 | 65 | 69 | 68 | 67 | 69 | 68 | 50 |
| train on dataset2      | 48 | 58 | 62 | 68 | 70 | 68 | 68 | 70 | 63 | 58 |
| train on dataset3      | 45 | 54 | 65 | 68 | 70 | 70 | 66 | 69 | 65 | 65 |     
| train on dataset4      | 46 | 55 | 63 | 71 | 71 | 70 | 68 | 69 | 66 | 71 |
| train on dataset5      | 46 | 54 | 63 | 70 | 71 | 70 | 69 | 70 | 64 | 71 |
| train on dataset6      | 45 | 56 | 63 | 68 | 70 | 70 | 71 | 69 | 66 | 70 |
| train on dataset7      | 45 | 52 | 56 | 60 | 64 | 68 | 70 | 70 | 69 | 70 |
| train on dataset8      | 43 | 51 | 57 | 62 | 65 | 67 | 69 | 69 | 69 | 69 |
| train on dataset9      | 43 | 51 | 58 | 64 | 66 | 68 | 69 | 69 | 69 | 69 |
  
  
### Architecture1 used for Type 1,2,3
```python
class Wherenet(nn.Module):
    def __init__(self):
        super(Wherenet,self).__init__()
        self.linear1 = nn.Linear(2,4)
        self.linear2 = nn.Linear(4,8)
        self.linear3 = nn.Linear(8,1)
    def forward(self,z):
        x = torch.zeros([batch,9],dtype=torch.float64)
        y = torch.zeros([batch,2], dtype=torch.float64)
        for i in range(9):
            x[:,i] = self.helper(z[:,2*i:2*i+2])[:,0]
        x = F.softmax(x,dim=1)   # alphas
        x1 = x[:,0]
        for i in range(9):
            x1 = x[:,i]          
            y = y+torch.mul(x1[:,None],z[:,2*i:2*i+2])
        return y , x 

    def helper(self,x):
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = self.linear3(x)
        return x


class Whatnet(nn.Module):
    def __init__(self):
        super(Whatnet,self).__init__()
        self.linear1 = nn.Linear(2,4)
        self.linear2 = nn.Linear(4,3)
    def forward(self,x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x
where = Wherenet().double()
what = Whatnet().double()
```
### Architecture2 used for Type 4
```python
class Wherenet(nn.Module):
    def __init__(self):
        super(Wherenet,self).__init__()
        self.linear1 = nn.Linear(2,50)
        self.linear2 = nn.Linear(50,50)
        self.linear3 = nn.Linear(50,1)
    def forward(self,z):
        x = torch.zeros([batch,9],dtype=torch.float64)
        y = torch.zeros([batch,2], dtype=torch.float64)
        for i in range(9):
            x[:,i] = self.helper(z[:,2*i:2*i+2])[:,0]
        x = F.softmax(x,dim=1)   # alphas
        x1 = x[:,0]
        for i in range(9):
            x1 = x[:,i]          
            #print()
            y = y+torch.mul(x1[:,None],z[:,2*i:2*i+2])
        return y , x 
    
    def helper(self,x):
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = self.linear3(x)
        return x

class Whatnet(nn.Module):
    def __init__(self):
        super(Whatnet,self).__init__()
        self.linear1 = nn.Linear(2,50)
        self.linear2 = nn.Linear(50,3)
    def forward(self,x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x
where = Wherenet().double()
what = Whatnet().double()
```

### Weights and CSV (containing focus_vs_pred values every 5 epoch) of above experiments can be found at following Gdrive link :
> https://drive.google.com/open?id=1ysJmEfdmLTnqRaYz6Z6NfXLTrw_QcLLl
