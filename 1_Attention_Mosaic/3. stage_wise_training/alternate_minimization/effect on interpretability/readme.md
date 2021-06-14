# effects of alternate minimization on interpretability

## DATA 1 : Synthetic elliptical blobs data 

## Method 1.1: alternate minimization Without Sparsity Regulariser
### Table 1.1.1: Average performance of alternate minimization with 'every_what_epoch' over 10 runs

|experiment | avg FTPT | avg FFPT | avg FTPF | avg FFPF | avg Accuracy |
|----------------|----|-----|-----|-----|--------------|
| simultaneous             | 74.71 | 25.26 | 0.023 | 0     | 99.97 | 
| every 1 (focus-classify) | 91.42 | 8.55  | 0.016 | 0     | 99.97 | 
| every 1 (classify-focus) | 90.74 | 9.25  | 0     | 0     | 99.99 |   
| every 5 (focus-classify) | 82.92 | 17.07 | 0.003 | 0.003 | 99.99 | 
| every 5 (classify-focus) | 89.85 | 5.49  | 0     | 4.65  | 95.34 | 
| every 10 (focus-classify)| 74.55 | 25.41 | 0.02  | 0.006 | 99.96 | 
| every 10 (classify-focus)| 76.01 | 14.73 | 0.003 | 9.25  | 90.74 | 
| every 20 (focus-classify)| 74.83 | 25.12 | 0.043 | 0     | 99.95 |
| every 20 (classify-focus)| 82.10 | 13.27 | 0.013 | 4.61  | 95.37 |  


### Table 1.1.2: Trend of alternate minimization with 'every_what_epoch'

| #runs | simultaneous | every 1 (focus-classify) | every 1 (classify-focus) | every 20 (focus-classify) | every 20 (classify-focus)|
|-------|--------------|--------------------------|--------------------------|---------------------------|------------------|
| run1 | <img src=./blob_plots/without_entropy/simultaneous/run1.png width="150">  | <img src=./blob_plots/without_entropy/where_what/every1/run1.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every1/run1.png width="150">  |<img src=./blob_plots/without_entropy/where_what/every20/run1.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every20/run1.png width="150">  |
| run2 | <img src=./blob_plots/without_entropy/simultaneous/run2.png width="150">  | <img src=./blob_plots/without_entropy/where_what/every1/run2.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every1/run2.png width="150">  |<img src=./blob_plots/without_entropy/where_what/every20/run2.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every20/run2.png width="150">  | 
| run3 | <img src=./blob_plots/without_entropy/simultaneous/run3.png width="150">  | <img src=./blob_plots/without_entropy/where_what/every1/run3.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every1/run3.png width="150">  |<img src=./blob_plots/without_entropy/where_what/every20/run3.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every20/run3.png width="150">  | 
| run4 | <img src=./blob_plots/without_entropy/simultaneous/run4.png width="150">  | <img src=./blob_plots/without_entropy/where_what/every1/run4.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every1/run4.png width="150">  |<img src=./blob_plots/without_entropy/where_what/every20/run4.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every20/run4.png width="150">  | 
| run5 | <img src=./blob_plots/without_entropy/simultaneous/run5.png width="150">  | <img src=./blob_plots/without_entropy/where_what/every1/run5.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every1/run5.png width="150">  |<img src=./blob_plots/without_entropy/where_what/every20/run5.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every20/run5.png width="150">  |
| run6 | <img src=./blob_plots/without_entropy/simultaneous/run6.png width="150">  | <img src=./blob_plots/without_entropy/where_what/every1/run6.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every1/run6.png width="150">  |<img src=./blob_plots/without_entropy/where_what/every20/run6.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every20/run6.png width="150">  |
| run7 | <img src=./blob_plots/without_entropy/simultaneous/run7.png width="150">  | <img src=./blob_plots/without_entropy/where_what/every1/run7.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every1/run7.png width="150">  |<img src=./blob_plots/without_entropy/where_what/every20/run7.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every20/run7.png width="150">  |
| run8 | <img src=./blob_plots/without_entropy/simultaneous/run8.png width="150">  | <img src=./blob_plots/without_entropy/where_what/every1/run8.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every1/run8.png width="150">  |<img src=./blob_plots/without_entropy/where_what/every20/run8.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every20/run8.png width="150">  |
| run9 | <img src=./blob_plots/without_entropy/simultaneous/run9.png width="150">  | <img src=./blob_plots/without_entropy/where_what/every1/run9.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every1/run9.png width="150">  |<img src=./blob_plots/without_entropy/where_what/every20/run9.png width="150">  |<img src=./blob_plots/without_entropy/what_where/every20/run9.png width="150">  |
| run10| <img src=./blob_plots/without_entropy/simultaneous/run10.png width="150"> | <img src=./blob_plots/without_entropy/where_what/every1/run10.png width="150"> |<img src=./blob_plots/without_entropy/what_where/every1/run10.png width="150"> |<img src=./blob_plots/without_entropy/where_what/every20/run10.png width="150"> |<img src=./blob_plots/without_entropy/what_where/every20/run10.png width="150"> |

## Method 1.2: alternate minimization with Sparsity Regulariser
### Table 1.2.1: Average performance of alternate minimization with 'every_what_epoch' over 10 runs with k = 0.005 (Sparsity Regulariser)

|experiment | avg FTPT | avg FFPT | avg FTPF | avg FFPF | avg Accuracy |
|----------------|----|-----|-----|-----|--------------|
| simultaneous with k = 0.005 (Sparsity Regulariser)             | 85.63 | 14.36 |  0 | 0 | 99.99 |
| every 1 (focus-classify) with k = 0.005 (Sparsity Regulariser) | 94.35 | 5.65  |  0 | 0 |  99.9 |
| every 1 (classify-focus) with k = 0.005 (Sparsity Regulariser) | 91.34 | 8.66  |  0 | 0 |  99 |
| every 5 (focus-classify) with k = 0.005 (Sparsity Regulariser) | 95.19 | 4.80  |  0 | 0 | 99.99 |
| every 5 (classify-focus) with k = 0.005 (Sparsity Regulariser) | 85.18 | 10.19 |  0 | 4.62 | 95.37 |
| every 10 (focus-classify) with k = 0.005 (Sparsity Regulariser) | 89.07 | 10.93 |  0 |  0 | 100 |
| every 10 (classify-focus) with k = 0.005 (Sparsity Regulariser) | 87.75 |  7.58 | 0  | 4.66 | 95.33 |
| every 20 (focus-classify) with k = 0.005 (Sparsity Regulariser) | 81.80 | 18.19 |  0 |  0 | 99.99 |
| every 20 (classify-focus) with k = 0.005 (Sparsity Regulariser) | 93.99 |  6.01 |  0 |  0 | 100 |


### Table 1.2.2: Trend of alternate minimization with 'every_what_epoch' with k = 0.005 (Sparsity Regulariser)

| #runs | simultaneous | every 1 (focus-classify) | every 1 (classify-focus) | every 20 (focus-classify) | every 20 (classify-focus)|
|-------|--------------|--------------------------|--------------------------|---------------------------|------------------|
| run1 | <img src=./blob_plots/with_entropy/simultaneous/run1.png width="150">  | <img src=./blob_plots/with_entropy/where_what/every1/run1.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every1/run1.png width="150">  |<img src=./blob_plots/with_entropy/where_what/every20/run1.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every20/run1.png width="150">  |
| run2 | <img src=./blob_plots/with_entropy/simultaneous/run2.png width="150">  | <img src=./blob_plots/with_entropy/where_what/every1/run2.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every1/run2.png width="150">  |<img src=./blob_plots/with_entropy/where_what/every20/run2.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every20/run2.png width="150">  | 
| run3 | <img src=./blob_plots/with_entropy/simultaneous/run3.png width="150">  | <img src=./blob_plots/with_entropy/where_what/every1/run3.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every1/run3.png width="150">  |<img src=./blob_plots/with_entropy/where_what/every20/run3.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every20/run3.png width="150">  | 
| run4 | <img src=./blob_plots/with_entropy/simultaneous/run4.png width="150">  | <img src=./blob_plots/with_entropy/where_what/every1/run4.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every1/run4.png width="150">  |<img src=./blob_plots/with_entropy/where_what/every20/run4.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every20/run4.png width="150">  | 
| run5 | <img src=./blob_plots/with_entropy/simultaneous/run5.png width="150">  | <img src=./blob_plots/with_entropy/where_what/every1/run5.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every1/run5.png width="150">  |<img src=./blob_plots/with_entropy/where_what/every20/run5.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every20/run5.png width="150">  |
| run6 | <img src=./blob_plots/with_entropy/simultaneous/run6.png width="150">  | <img src=./blob_plots/with_entropy/where_what/every1/run6.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every1/run6.png width="150">  |<img src=./blob_plots/with_entropy/where_what/every20/run6.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every20/run6.png width="150">  |
| run7 | <img src=./blob_plots/with_entropy/simultaneous/run7.png width="150">  | <img src=./blob_plots/with_entropy/where_what/every1/run7.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every1/run7.png width="150">  |<img src=./blob_plots/with_entropy/where_what/every20/run7.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every20/run7.png width="150">  |
| run8 | <img src=./blob_plots/with_entropy/simultaneous/run8.png width="150">  | <img src=./blob_plots/with_entropy/where_what/every1/run8.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every1/run8.png width="150">  |<img src=./blob_plots/with_entropy/where_what/every20/run8.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every20/run8.png width="150">  |
| run9 | <img src=./blob_plots/with_entropy/simultaneous/run9.png width="150">  | <img src=./blob_plots/with_entropy/where_what/every1/run9.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every1/run9.png width="150">  |<img src=./blob_plots/with_entropy/where_what/every20/run9.png width="150">  |<img src=./blob_plots/with_entropy/what_where/every20/run9.png width="150">  |
| run10| <img src=./blob_plots/with_entropy/simultaneous/run10.png width="150"> | <img src=./blob_plots/with_entropy/where_what/every1/run10.png width="150"> |<img src=./blob_plots/with_entropy/what_where/every1/run10.png width="150"> |<img src=./blob_plots/with_entropy/where_what/every20/run10.png width="150"> |<img src=./blob_plots/with_entropy/what_where/every20/run10.png width="150"> |

## DATA 2 : Type4 data: FG classes in convex hull of BG classes 

## Method 2.1: alternate minimization Without Sparsity Regulariser
### Table 2.1.1: Average performance of alternate minimization with 'every_what_epoch' over 10 runs

|experiment | avg FTPT | avg FFPT | avg FTPF | avg FFPF | avg Accuracy |
|----------------|----|-----|-----|-----|--------------|
| simultaneous             | 84.35 | 15.59 | 0.003 | 0.02  | 99.95 |  
| every 1 (focus-classify) | 84.47 | 15.46 | 0.003 | 0.03  | 99.93 |  
| every 1 (classify-focus) | 83.39 | 16.54 | 0.026 | 0.036 | 99.95 |  
| every 5 (focus-classify) | 71.17 | 28.72 | 0.046 | 0.056 | 99.89 | 
| every 5 (classify-focus) | 84.80 | 15.16 | 0.016 | 0.02  | 99.96 |  
| every 10 (focus-classify)| 72.13 | 22.83 | 0.24  | 4.79  | 94.96 |  
| every 10 (classify-focus)| 86.13 | 13.85 | 0.016 | 0     | 99.98 | 
| every 20 (focus-classify)| 52.49 | 32.84 | 0.73  | 13.93 | 85.33 | 
| every 20 (classify-focus)| 83.88 | 16.08 | 0.03  | 0.003 | 99.96 |  
| every 100 (focus-classify)| 9.63 | 34.68 | 0.27  | 55.41 | 44.31 | 
| every 100 (classify-focus)| 92.09 | 7.88 | 0.02  | 0.003 | 99.96 |

### Table 2.1.2: Trend of alternate minimization with 'every_what_epoch'

| #runs | simultaneous | every 1 (focus-classify) | every 1 (classify-focus) | every 20 (focus-classify) | every 20 (classify-focus)|
|-------|--------------|--------------------------|--------------------------|---------------------------|------------------|
| run1 | <img src=./type4_plots/without_entropy/simultaneous/run1.png width="150">  | <img src=./type4_plots/without_entropy/where_what/every1/run1.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every1/run1.png width="150">  |<img src=./type4_plots/without_entropy/where_what/every20/run1.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every20/run1.png width="150">  |
| run2 | <img src=./type4_plots/without_entropy/simultaneous/run2.png width="150">  | <img src=./type4_plots/without_entropy/where_what/every1/run2.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every1/run2.png width="150">  |<img src=./type4_plots/without_entropy/where_what/every20/run2.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every20/run2.png width="150">  | 
| run3 | <img src=./type4_plots/without_entropy/simultaneous/run3.png width="150">  | <img src=./type4_plots/without_entropy/where_what/every1/run3.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every1/run3.png width="150">  |<img src=./type4_plots/without_entropy/where_what/every20/run3.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every20/run3.png width="150">  | 
| run4 | <img src=./type4_plots/without_entropy/simultaneous/run4.png width="150">  | <img src=./type4_plots/without_entropy/where_what/every1/run4.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every1/run4.png width="150">  |<img src=./type4_plots/without_entropy/where_what/every20/run4.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every20/run4.png width="150">  | 
| run5 | <img src=./type4_plots/without_entropy/simultaneous/run5.png width="150">  | <img src=./type4_plots/without_entropy/where_what/every1/run5.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every1/run5.png width="150">  |<img src=./type4_plots/without_entropy/where_what/every20/run5.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every20/run5.png width="150">  |
| run6 | <img src=./type4_plots/without_entropy/simultaneous/run6.png width="150">  | <img src=./type4_plots/without_entropy/where_what/every1/run6.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every1/run6.png width="150">  |<img src=./type4_plots/without_entropy/where_what/every20/run6.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every20/run6.png width="150">  |
| run7 | <img src=./type4_plots/without_entropy/simultaneous/run7.png width="150">  | <img src=./type4_plots/without_entropy/where_what/every1/run7.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every1/run7.png width="150">  |<img src=./type4_plots/without_entropy/where_what/every20/run7.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every20/run7.png width="150">  |
| run8 | <img src=./type4_plots/without_entropy/simultaneous/run8.png width="150">  | <img src=./type4_plots/without_entropy/where_what/every1/run8.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every1/run8.png width="150">  |<img src=./type4_plots/without_entropy/where_what/every20/run8.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every20/run8.png width="150">  |
| run9 | <img src=./type4_plots/without_entropy/simultaneous/run9.png width="150">  | <img src=./type4_plots/without_entropy/where_what/every1/run9.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every1/run9.png width="150">  |<img src=./type4_plots/without_entropy/where_what/every20/run9.png width="150">  |<img src=./type4_plots/without_entropy/what_where/every20/run9.png width="150">  |
| run10| <img src=./type4_plots/without_entropy/simultaneous/run10.png width="150"> | <img src=./type4_plots/without_entropy/where_what/every1/run10.png width="150"> |<img src=./type4_plots/without_entropy/what_where/every1/run10.png width="150"> |<img src=./type4_plots/without_entropy/where_what/every20/run10.png width="150"> |<img src=./type4_plots/without_entropy/what_where/every20/run10.png width="150"> |

### Architecures of Focus and Classification Net
```python
class Focus_deep(nn.Module):
    '''
       deep focus network averaged at zeroth layer
       input : elemental data
    '''
    def __init__(self,inputs,output,K,d):
        super(Focus_deep,self).__init__()
        self.inputs = inputs
        self.output = output
        self.K = K
        self.d  = d
        self.linear1 = nn.Linear(self.inputs,50)  #,self.output)
        self.linear2 = nn.Linear(50,self.output) 
    def forward(self,z):
        batch = z.shape[0]
        x = torch.zeros([batch,self.K],dtype=torch.float64)
        y = torch.zeros([batch,self.d], dtype=torch.float64)
        x,y = x.to("cuda"),y.to("cuda")
        for i in range(self.K):
            x[:,i] = self.helper(z[:,i] )[:,0]  # self.d*i:self.d*i+self.d
        x = F.softmax(x,dim=1)   # alphas
        x1 = x[:,0]
        for i in range(self.K):
            x1 = x[:,i]          
            y = y+torch.mul(x1[:,None],z[:,i])  # self.d*i:self.d*i+self.d
        return y , x 
    def helper(self,x):
      x = F.relu(self.linear1(x))
      x = self.linear2(x)
      return x
```

```python
class Classification_deep(nn.Module):
    '''
       input : elemental data
       deep classification module data averaged at zeroth layer
    '''
    def __init__(self,inputs,output):
        super(Classification_deep,self).__init__()
        self.inputs = inputs
        self.output = output
        self.linear1 = nn.Linear(self.inputs,50)
        self.linear2 = nn.Linear(50,self.output)

    def forward(self,x):
      x = F.relu(self.linear1(x))
      x = self.linear2(x)
      return x    
```
