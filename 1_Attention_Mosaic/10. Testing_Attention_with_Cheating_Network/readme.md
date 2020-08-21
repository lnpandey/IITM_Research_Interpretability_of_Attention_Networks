### CNN - 3 Layer Architecture for Focus Net
```python
class Focus(nn.Module):
  def __init__(self):
    super(Focus, self).__init__()
    self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=0)
    self.pool = nn.MaxPool2d(2, 2)
    self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=0)
    self.conv3 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=0)
    self.fc1 = nn.Linear(1024, 512)
    self.fc2 = nn.Linear(512, 64)
    self.fc3 = nn.Linear(64, 10)
    self.fc4 = nn.Linear(10, 2)

  def forward(self,z):  #y is avg image #z batch of list of 9 images
    y = torch.zeros([batch,3, 32,32], dtype=torch.float64)
    x = torch.zeros([batch,9],dtype=torch.float64)
    y = y.to("cuda")
    x = x.to("cuda")    
    for i in range(9):
        x[:,i] = self.helper(z[:,i])[:,0]
    x = F.softmax(x,dim=1)
    x1 = x[:,0]
    torch.mul(x1[:,None,None,None],z[:,0])
    for i in range(9):            
      x1 = x[:,i]          
      y = y + torch.mul(x1[:,None,None,None],z[:,i])
    return x, y
    
  def helper(self, x):
    x = self.pool(F.relu(self.conv1(x)))
    x = self.pool(F.relu(self.conv2(x)))
    # print(x.shape)
    x = (F.relu(self.conv3(x)))
    x =  x.view(x.size(0), -1)
    # print(x.shape)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.fc3(x))
    x = self.fc4(x)
    return x
```
### CNN - 3 Layer Architecture for Classify Net
```python
class Classification(nn.Module):
  def __init__(self):
    super(Classification, self).__init__()
    self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=0)
    self.pool = nn.MaxPool2d(2, 2)
    self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=0)
    self.conv3 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=0)
    self.fc1 = nn.Linear(1024, 512)
    self.fc2 = nn.Linear(512, 64)
    self.fc3 = nn.Linear(64, 10)
    self.fc4 = nn.Linear(10,3)

  def forward(self, x):
    x = self.pool(F.relu(self.conv1(x)))
    x = self.pool(F.relu(self.conv2(x)))
    # print(x.shape)
    x = (F.relu(self.conv3(x)))
    x =  x.view(x.size(0), -1)
    # print(x.shape)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.fc3(x))
    x = self.fc4(x)
    return x
```
### CNN - 6 Layer Architecture for Focus Net
```python
class Focus(nn.Module):
  def __init__(self):
    super(Focus, self).__init__()
    self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=0)
    self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=0)
    self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=0)
    self.conv4 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=0)
    self.conv5 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=0)
    self.conv6 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1)
    self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
    self.batch_norm1 = nn.BatchNorm2d(32)
    self.batch_norm2 = nn.BatchNorm2d(128)
    self.dropout1 = nn.Dropout2d(p=0.05)
    self.dropout2 = nn.Dropout2d(p=0.1)
    self.fc1 = nn.Linear(128,64)
    self.fc2 = nn.Linear(64, 32)
    self.fc3 = nn.Linear(32, 10)
    self.fc4 = nn.Linear(10, 2)

  def forward(self,z):  #y is avg image #z batch of list of 9 images
    y = torch.zeros([batch,3, 32,32], dtype=torch.float64)
    x = torch.zeros([batch,9],dtype=torch.float64)
    y = y.to("cuda")
    x = x.to("cuda")    
    for i in range(9):
        x[:,i] = self.helper(z[:,i])[:,0]
    x = F.softmax(x,dim=1)
    x1 = x[:,0]
    torch.mul(x1[:,None,None,None],z[:,0])
    for i in range(9):            
      x1 = x[:,i]          
      y = y + torch.mul(x1[:,None,None,None],z[:,i])
    return x, y
    
  def helper(self, x):
    x = self.conv1(x)
    x = F.relu(self.batch_norm1(x))
    x = (F.relu(self.conv2(x)))
    x = self.pool(x)    
    x = self.conv3(x)
    x = F.relu(self.batch_norm2(x))
    x = (F.relu(self.conv4(x)))
    x = self.pool(x)
    x = self.dropout1(x)
    x = self.conv5(x)
    x = F.relu(self.batch_norm2(x))
    x = (F.relu(self.conv6(x)))
    x = self.pool(x)
    x = x.view(x.size(0), -1)
    x = self.dropout2(x)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = self.dropout2(x)
    x = F.relu(self.fc3(x))
    x = self.fc4(x)
    return x
```
### CNN - 6 Layer Architecture for Classify Net
```python
class Classification(nn.Module):
  def __init__(self):
    super(Classification, self).__init__()
    self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=0)
    self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=0)
    self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=0)
    self.conv4 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=0)
    self.conv5 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=0)
    self.conv6 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1)
    self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
    self.batch_norm1 = nn.BatchNorm2d(32)
    self.batch_norm2 = nn.BatchNorm2d(128)
    self.dropout1 = nn.Dropout2d(p=0.05)
    self.dropout2 = nn.Dropout2d(p=0.1)
    self.fc1 = nn.Linear(128,64)
    self.fc2 = nn.Linear(64, 32)
    self.fc3 = nn.Linear(32, 10)
    self.fc4 = nn.Linear(10, 3)

  def forward(self,x):  
    x = self.conv1(x)
    x = F.relu(self.batch_norm1(x))
    x = (F.relu(self.conv2(x)))
    x = self.pool(x)    
    x = self.conv3(x)
    x = F.relu(self.batch_norm2(x))
    x = (F.relu(self.conv4(x)))
    x = self.pool(x)
    x = self.dropout1(x)
    x = self.conv5(x)
    x = F.relu(self.batch_norm2(x))
    x = (F.relu(self.conv6(x)))
    x = self.pool(x)
    x = x.view(x.size(0), -1)
    x = self.dropout2(x)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = self.dropout2(x)
    x = F.relu(self.fc3(x))
    x = self.fc4(x)
    return x
```

## Table 1: 10 Class classification on CIFAR 10
|Model Used| Epochs | Train Accuracy | Test Accuracy |
|----------|--------|----------------|---------------|
|Mini-Inception | 23 | 100| 86 |
|CNN - 6 Layers | 91 | 99| 81 |
|CNN - 3 Layers | 47 | 99| 74 |

### Table 2: Using this CNN - 6 Layer, Trained Focus and Classify net
|Network| Epochs | Train Accuracy | Test Accuracy |
|----------|--------|----------------|---------------|
|Focus Net (Binary classification for fg) | 73 | 99| 89 |
|Classify Net (3 class classification within fg classes) | 70 | 99| 89 |

### Table 3: Using this CNN - 3 Layer, Trained Focus and Classify net
|Network| Epochs | Train Accuracy | Test Accuracy |
|----------|--------|----------------|---------------|
|Focus Net (Binary classification for fg) | 56 | 100 | 86 |
|Classify Net (3 class classification within fg classes) | 48 | 100 | 90 |


### Tabel 4: Using Focus and Classify net of CNN - 6 Layer, following 16 experiments were performed
|Sno.|Focus init |Classify init| Which module to be trained | Epoch | Train Acc | Test Acc | Train FTPT | Train FFPT | Train FTPF | Train FFPF | Test FTPT | Test FFPT | Test FTPF | Test FFPF | 
|----|-------------------------|---------------------------------|----------------------------|-------|----------------|---------------|------------|------------|------------|------------|-----------|-----------|-----------|-----------|
| 1 | Random | Random | - | 0 | 33 | 33 | 6 | 27 | 9 | 57 | 6 | 27 | 9 | 56 |
| 2 | Random | Random | Both | 46 | 99 | 93 | 84 | 14 | 0 | 0 | 79 | 13 | 2 | 3 |
| 3 | Random | Random | Focus | 50 | 33 | 32 | 2 | 30 | 5 | 61 | 2 | 31 | 5 | 61 |
| 4 | Random | Random | Classify | 51 | 99 | 43 | 11 | 87 | 0 | 0 | 5 | 38 | 6 | 49 |
| 5 | Pre-Trained | Random | - | 0 | 33 | 33 | 14 | 18 | 30 | 36 | 14 | 18 | 30 | 36 |
| 6 | Pre-Trained | Random | Both | 19 | 99 | 97 | 86 | 13 | 0 | 0 | 85 | 12 | 1 | 0 |
| 7 | Pre-Trained | Random | Focus | 50 | 33 | 33 | 0 | 32 | 4 | 62 | 0 | 33 | 4 | 62 |
| 8 | Pre-Trained | Random | Classify | 113 | 99 | 90 | 99 | 0 | 0 | 0 | 90 | 0 | 9 | 0 | 
| 9 | Random | Pre-Trained | - | 0 | 47 | 47 | 5 | 41 | 6 | 46 | 5 | 41 | 6 | 46 |
| 10 | Random | Pre-Trained | Both | 52 | 99 | 94 | 86 | 12 | 0 | 0 | 82 | 12 | 1 | 3 |
| 11 | Random | Pre-Trained | Focus | 148 | 99 | 95 | 90 | 8 | 0 | 0 | 86 | 8 | 1 | 3 |
| 12 | Random | Pre-Trained | Classify | 60 | 99 | 44 | 13 | 85 | 0 | 0 | 6 | 38 | 7 | 47 |
| 13 | Pre-Trained | Pre-Trained | - | 0 | 97 | 97 | 97 | 0 | 2 | 0 | 97 | 0 | 2 | 0 |
| 14 | Pre-Trained | Pre-Trained | Both | 3 | 99 | 99 | 99 | 0 | 0 | 0 | 99 | 0 | 0 | 0 |
| 15 | Pre-Trained | Pre-Trained | Focus | 50| 39 | 39 | 9 | 29 | 0 | 59 | 9 | 30 | 0 | 59 |
| 16 | Pre-Trained | Pre-Trained | Classify | 11 | 99 | 96 | 99 | 0 | 0 | 0 | 95 | 0 | 4 | 0 |


<!--- ## Analysis of FTPT, FFPT, FTPF. FFPF for the above experiments 
#### Row 2 : | 2 | Focus is Random | Classify is Random | Train Both | 46 | 99 | 94 |
On Training Data 
![](./plots_and_images/train2.PNG)
On Testing Data
![](./plots_and_images/test2.PNG)
#### Row 3 : | 3 | Focus is Random | Classify is Random | Train Focus | 50 | 33 | 32 |
On Training Data
![](./plots_and_images/train3.PNG)
On Testing Data
![](./plots_and_images/test3.PNG)
#### Row 4 : | 4 | Focus is Random | Classify is Random | Train Classify | 51 | 99 | 43 |
On Training Data
![](./plots_and_images/train4.PNG)
On Testing Data
![](./plots_and_images/test4.PNG)
#### Row 6 : | 6 | Focus is Pre-Trained | Classify is Random | Train Both | 19 | 99 | 97 |
On Training Data
![](./plots_and_images/train6.PNG)
On Testing Data
![](./plots_and_images/test6.PNG)
#### Row 7 : | 7 | Focus is Pre-Trained | Classify is Random | Train Focus | 50 | 33 | 33 |
On Training Data
![](./plots_and_images/train7.PNG)
On Testing Data
![](./plots_and_images/test7.PNG)
#### Row 8 : | 8 | Focus is Pre-Trained | Classify is Random | Train Classify | 113 | 99 | 90 |
On Training Data
![](./plots_and_images/train8.PNG)
On Testing Data
![](./plots_and_images/test8.PNG)
#### Row 10 : | 10 | Focus is Random | Classify is Pre-Trained | Train Both | 52 | 99 | 93 |
On Training Data
![](./plots_and_images/train10.PNG)
On Testing Data
![](./plots_and_images/test10.PNG)
#### Row 11 : | 11 | Focus is Random | Classify is Pre-Trained | Train Focus | 20 | 47 | 45 |
On Training Data
![](./plots_and_images/train11.PNG)
On Testing Data
![](./plots_and_images/test11.PNG)
#### Row 12 : | 12 | Focus is Random | Classify is Pre-Trained | Train Classify | 60 | 99 | 44 |
On Training Data
![](./plots_and_images/train12.PNG)
On Testing Data
![](./plots_and_images/test12.PNG)
#### Row 14 : | 14 | Focus is Pre-Trained | Classify is Pre-Trained | Train Both | 4 | 99 | 99 |
On Training Data
![](./plots_and_images/train14.PNG)
On Testing Data
![](./plots_and_images/test14.PNG)
#### Row 15 : | 15 | Focus is Pre-Trained | Classify is Pre-Trained | Train Focus | 200 | 40 | 39 |
On Training Data
![](./plots_and_images/train15_1.PNG)
![](./plots_and_images/train15_2.PNG)
On Testing Data
![](./plots_and_images/test15_1.PNG)
![](./plots_and_images/test15_2.PNG)
#### Row 16 : | 16 | Focus is Pre-Trained | Classify is Pre-Trained | Train Classify | 11 | 99 | 96 |
On Training Data
![](./plots_and_images/train16.PNG)
On Testing Data
![](./plots_and_images/test16.PNG)--->


### Tabel 5: Using Focus and Classify net of CNN - 3 Layer, following 16 experiments were performed
|Sno.|Focus init |Classify init| Which module to be trained | Epoch | Train Acc | Test Acc | Train FTPT | Train FFPT | Train FTPF | Train FFPF | Test FTPT | Test FFPT | Test FTPF | Test FFPF | 
|----|-------------------------|---------------------------------|----------------------------|-------|----------------|---------------|------------|------------|------------|------------|-----------|-----------|-----------|-----------|
| 1 | Random | Random | - | 0 | 33 | 33 | 2 | 31 | 11 | 54 | 2 | 30 | 12 | 54 |
| 2 | Random | Random | Both | 65 | 99 | 91 | 82 | 17 | 0 | 0 | 76 | 14 | 2 | 5 |
| 3 | Random | Random | Focus | 50 | 33 | 33 | 3 | 30 | 5 | 61 | 3 | 30 | 5 | 61 |
| 4 | Random | Random | Classify | 77 | 99 | 41 | 9 | 90 | 0 | 0 | 4 | 37 | 5 | 53 |
| 5 | Pre-Trained | Random | - | 0 | 33 | 33 | 0 | 33 | 0 | 66 | 0 | 32 | 0 | 67 |
| 6 | Pre-Trained | Random | Both | 25 | 99 | 96 | 80 | 19 | 0 | 0 | 77 | 18 | 2 | 1 |
| 7 | Pre-Trained | Random | Focus | 50 | 33 | 32 | 0 | 33 | 0 | 66 | 0 | 32 | 0 | 67 |
| 8 | Pre-Trained | Random | Classify | 17 | 97 | 87 | 97 | 0 | 2 | 0 | 87 | 0 | 12 | 0 | 
| 9 | Random | Pre-Trained | - | 0 | 33 | 34 | 5 | 28 | 6 | 59 | 5 | 28 | 6 | 58 |
| 10 | Random | Pre-Trained | Both | 60 | 99 | 93 | 83 | 15 | 0 | 0 | 78 | 14 | 1 | 5 |
| 11 | Random | Pre-Trained | Focus | 56 | 99 | 91 | 84 | 14 | 0 | 0 | 79 | 12 | 1 | 6 |
| 12 | Random | Pre-Trained | Classify | 71 | 99 | 42 | 14 | 85 | 0 | 0 | 6 | 35 | 7 | 50 |
| 13 | Pre-Trained | Pre-Trained | - | 0 | 65 | 64 | 65 | 0 | 34 | 0 | 64 | 0 | 35 | 0 |
| 14 | Pre-Trained | Pre-Trained | Both | 22 | 99 | 98 | 99 | 0 | 0 | 0 | 97 | 0 | 1 | 0 |
| 15 | Pre-Trained | Pre-Trained | Focus | 50 | 37 | 37 | 5 | 31 | 0 | 62 | 5 | 31 | 0 | 62 |
| 16 | Pre-Trained | Pre-Trained | Classify | 23 | 99 | 90 | 99 | 0 | 0 | 0 | 90 | 0 | 9 | 0 |
