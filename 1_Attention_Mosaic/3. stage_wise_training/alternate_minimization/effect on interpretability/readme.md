### effects of alternate minimisation on interpretability

DATA: Synthetic elliptical blobs data 

### Table 1: Average performance of alternate minimisation with 'every_what_epoch' over 10 runs

|experiment | FTPT | FFPT | FTPF | FFPF | Avg Accuracy |
|----------------|----|-----|-----|-----|--------------|
| simultaneous |  |  |  |  | |
| every 1 (focus-classify) | | | | | | 
| every 1 (classify-focus) | | | | | |
| every 5 (focus-classify) | | | | | |
| every 5 (classify-focus) | | | | | |
| every 10 (focus-classify)| | | | | |
| every 10 (classify-focus)| | | | | |
| every 20 (focus-classify)| | | | | |
| every 20 (classify-focus)| | | | | |

<!---| 100 | 76.92 / 16.93 | 90.16 / 9.83  | 99.1 / 0.9    | 87.67 / 12.32 |
| 200 | 86.78 / 7.00  | 86.45 / 7.32  | 97.56 / 2.44  | 99.97 / 0.026 |
| 300 | 99.76 / 0.226 | 90.14 / 3.87  | 99.96 / 0.04  | 99.98 / 0.013 |--->

### Table 2: Trend of alternate minimisation with 'every_what_epoch'

| #runs | simultaneous | every 1 (focus-classify) | every 1 (classify-focus) | every 20 (focus-classify) | every 20 (classify-focus)|
|-------|--------------|--------------------------|--------------------------|---------------------------|------------------|
| run1 | <img src=./simultaneous/run1.png width="150">  | <img src=./where_what/every1/run1.png width="150">  |<img src=./what_where/every1/run1.png width="150">  |<img src=./where_what/every20/run1.png width="150">  |<img src=./what_where/every20/run1.png width="150">  |
| run2 | <img src=./simultaneous/run2.png width="150">  | <img src=./where_what/every1/run2.png width="150">  |<img src=./what_where/every1/run2.png width="150">  |<img src=./where_what/every20/run2.png width="150">  |<img src=./what_where/every20/run2.png width="150">  | 
| run3 | <img src=./simultaneous/run3.png width="150">  | <img src=./where_what/every1/run3.png width="150">  |<img src=./what_where/every1/run3.png width="150">  |<img src=./where_what/every20/run3.png width="150">  |<img src=./what_where/every20/run3.png width="150">  | 
| run4 | <img src=./simultaneous/run4.png width="150">  | <img src=./where_what/every1/run4.png width="150">  |<img src=./what_where/every1/run4.png width="150">  |<img src=./where_what/every20/run4.png width="150">  |<img src=./what_where/every20/run4.png width="150">  | 
| run5 | <img src=./simultaneous/run5.png width="150">  | <img src=./where_what/every1/run5.png width="150">  |<img src=./what_where/every1/run5.png width="150">  |<img src=./where_what/every20/run5.png width="150">  |<img src=./what_where/every20/run5.png width="150">  |
| run6 | <img src=./simultaneous/run6.png width="150">  | <img src=./where_what/every1/run6.png width="150">  |<img src=./what_where/every1/run6.png width="150">  |<img src=./where_what/every20/run6.png width="150">  |<img src=./what_where/every20/run6.png width="150">  |
| run7 | <img src=./simultaneous/run7.png width="150">  | <img src=./where_what/every1/run7.png width="150">  |<img src=./what_where/every1/run7.png width="150">  |<img src=./where_what/every20/run7.png width="150">  |<img src=./what_where/every20/run7.png width="150">  |
| run8 | <img src=./simultaneous/run8.png width="150">  | <img src=./where_what/every1/run8.png width="150">  |<img src=./what_where/every1/run8.png width="150">  |<img src=./where_what/every20/run8.png width="150">  |<img src=./what_where/every20/run8.png width="150">  |
| run9 | <img src=./simultaneous/run9.png width="150">  | <img src=./where_what/every1/run9.png width="150">  |<img src=./what_where/every1/run9.png width="150">  |<img src=./where_what/every20/run9.png width="150">  |<img src=./what_where/every20/run9.png width="150">  |
| run10| <img src=./simultaneous/run10.png width="150"> | <img src=./where_what/every1/run10.png width="150"> |<img src=./what_where/every1/run10.png width="150"> |<img src=./where_what/every20/run10.png width="150"> |<img src=./what_where/every20/run10.png width="150"> |


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
