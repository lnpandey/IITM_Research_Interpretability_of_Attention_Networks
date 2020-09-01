## Table 1: 10 Class classification on CIFAR 10
|Model Used| Epochs | Train Accuracy | Test Accuracy |
|----------|--------|----------------|---------------|
|Mini-Inception | 23 | 100| 86 |
|CNN - 6 Layers | 91 | 99| 81 |
|CNN - 3 Layers | 47 | 99| 74 |

### Table 2: Using this CNN - 6 Layer, Trained Focus and Classify net
|Network| Epochs | Train Accuracy | Test Accuracy |
|----------|--------|----------------|---------------|
|Focus Net (Binary classification for fg) | 73 | 99| 86 |
|Classify Net (3 class classification within fg classes) | 70 | 99| 86 |

### Table 3: Using this CNN - 3 Layer, Trained Focus and Classify net
|Network| Epochs | Train Accuracy | Test Accuracy |
|----------|--------|----------------|---------------|
|Focus Net (Binary classification for fg) | 56 | 100 | 86 |
|Classify Net (3 class classification within fg classes) | 48 | 100 | 90 |


### Tabel 4: Using Focus and Classify net of CNN - 3 Layer, following 16 experiments were performed
|Sno.|Focus init |Classify init| Which module to be trained | Epoch | Train Acc | Test Acc | Train FTPT | Train FFPT | Train FTPF | Train FFPF | Test FTPT | Test FFPT | Test FTPF | Test FFPF | 
|----|-------------------------|---------------------------------|----------------------------|-------|----------------|---------------|------------|------------|------------|------------|-----------|-----------|-----------|-----------|
| 1 | Random | Random | - | 0 | 33 | 33 | 2 | 31 | 11 | 54 | 2 | 30 | 12 | 54 |
| 2 | Random | Random | Both | 65 | 99 | 91 | 82 | 17 | 0 | 0 | 76 | 14 | 2 | 5 |
| 3 | Random | Random | Focus | 50 | 33 | 33 | 3 | 30 | 5 | 61 | 3 | 30 | 5 | 61 |
| 4 | Random | Random | Classify | 77 | 99 | 41 | 9 | 90 | 0 | 0 | 4 | 37 | 5 | 53 |
| 5 | Pre-Trained | Random | - | 0 | 33 | 32 | 33 | 0 | 66 | 0 | 32 | 0 | 67 |  0 |
| 6 | Pre-Trained | Random | Both | 32 | 99 | 95 | 92 | 6 | 0 | 0 | 89 | 6 | 1 | 2 |
| 7 | Pre-Trained | Random | Focus | 50 | 33 | 33 | 33 | 0 | 66 | 0 | 33 | 0 | 66 |  0 |
| 8 | Pre-Trained | Random | Classify | 18 | 99 | 97 | 99 | 0 | 0 | 0 | 97 | 0 | 2 | 0 | 
| 9 | Random | Pre-Trained | - | 0 | 33 | 34 | 5 | 28 | 6 | 59 | 5 | 28 | 6 | 58 |
| 10 | Random | Pre-Trained | Both | 60 | 99 | 93 | 83 | 15 | 0 | 0 | 78 | 14 | 1 | 5 |
| 11 | Random | Pre-Trained | Focus | 56 | 99 | 91 | 84 | 14 | 0 | 0 | 79 | 12 | 1 | 6 |
| 12 | Random | Pre-Trained | Classify | 71 | 99 | 42 | 14 | 85 | 0 | 0 | 6 | 35 | 7 | 50 |
| 13 | Pre-Trained | Pre-Trained | - | 0 | 100 | 100 | 100 | 0 | 0 | 0 | 100 | 0 | 0 | 0 |
| 14 | Pre-Trained | Pre-Trained | Both | 1 | 100 | 100 |100 | 0 | 0 | 0 | 100 | 0 | 0 | 0 |
| 15 | Pre-Trained | Pre-Trained | Focus | 1 | 100 | 100 |100 | 0 | 0 | 0 | 100 | 0 | 0 | 0 |
| 16 | Pre-Trained | Pre-Trained | Classify | 1 | 100 | 100 |100 | 0 | 0 | 0 | 100 | 0 | 0 | 0 |


### Tabel 5: Using Focus and Classify net of CNN - 3 Layer, analysis of FTPT, FFPT, FTPF, FFPF in above 16 experiments.
|Exp No.|Focus init |Classify init| Which module to be trained | analysis of FTPT, FFPT, FTPF, FFPF on Training Data | analysis of FTPT, FFPT, FTPF, FFPF on Testing Data |
|----|-----------|-------------|----------------------------|-----------------------------------------------------|----------------------------------------------------|
| 2  | Random | Random | Both | <img src= ./plots_and_images/3layer_cnn/train2.JPG width="800">  |  <img src= ./plots_and_images/3layer_cnn/test2.JPG width="800"> |
| 3  | Random | Random | Focus | <img src= ./plots_and_images/3layer_cnn/train3.JPG width="800">  |  <img src= ./plots_and_images/3layer_cnn/test3.JPG width="800"> |
| 4  | Random | Random | Classify | <img src= ./plots_and_images/3layer_cnn/train4.JPG width="800">  |  <img src= ./plots_and_images/3layer_cnn/test4.JPG width="800"> |
| 6  | Pre-Trained | Random | Both | <img src= ./plots_and_images/3layer_cnn/train6.JPG width="800">  |  <img src= ./plots_and_images/3layer_cnn/test6.JPG width="800"> |
| 7  | Pre-Trained | Random | Focus | <img src= ./plots_and_images/3layer_cnn/train7.JPG width="800">  |  <img src= ./plots_and_images/3layer_cnn/test7.JPG width="800"> |
| 8  | Pre-Trained | Random | Classify | <img src= ./plots_and_images/3layer_cnn/train8.JPG width="800">  |  <img src= ./plots_and_images/3layer_cnn/test8.JPG width="800"> |
| 10  | Random | Pre-Trained | Both | <img src= ./plots_and_images/3layer_cnn/train10.JPG width="800">  |  <img src= ./plots_and_images/3layer_cnn/test10.JPG width="800"> |
| 11  | Random | Pre-Trained | Focus | <img src= ./plots_and_images/3layer_cnn/train11.JPG width="800">  |  <img src= ./plots_and_images/3layer_cnn/test11.JPG width="800"> |
| 12  | Random | Pre-Trained | Classify | <img src= ./plots_and_images/3layer_cnn/train12.JPG width="800">  |  <img src= ./plots_and_images/3layer_cnn/test12.JPG width="800"> |



### Tabel 6: Using Focus and Classify net of CNN - 6 Layer, following 16 experiments were performed
|Sno.|Focus init |Classify init| Which module to be trained | Epoch | Train Acc | Test Acc | Train FTPT | Train FFPT | Train FTPF | Train FFPF | Test FTPT | Test FFPT | Test FTPF | Test FFPF | 
|----|-------------------------|---------------------------------|----------------------------|-------|----------------|---------------|------------|------------|------------|------------|-----------|-----------|-----------|-----------|
| 1 | Random | Random | - | 0 | 33 | 32 | 6 | 26 | 7 | 59 | 6 | 26 | 6 | 60 |
| 2 | Random | Random | Both | 42 | 99 | 93 | 85 | 14 | 0 | 0 | 80 | 12 | 2 | 4 |
| 3 | Random | Random | Focus | 50 | 33 | 33 | 3 | 30 | 9 | 56 | 2 | 31 | 10 | 55 |
| 4 | Random | Random | Classify | 50 | 99 | 44 | 11 | 87 | 0 | 0 | 5 | 38 | 6 | 49 |
| 5 | Pre-Trained | Random | - | 0 | 33 | 33 | 33 | 0 | 66 | 0 | 33 | 0 | 66 | 0 |
| 6 | Pre-Trained | Random | Both | 25 | 99 | 97 | 97 | 2 | 0 | 0 | 94 | 2 | 1 | 1 |
| 7 | Pre-Trained | Random | Focus | 50 | 32 | 33 | 32 | 0| 66 | 0 | 33 | 0 | 66 | 0 |
| 8 | Pre-Trained | Random | Classify | 28 | 99 | 98 | 99 | 0 | 0 | 0 | 98 | 0 | 1 | 0 | 
| 9 | Random | Pre-Trained | - | 0 | 47 | 47 | 7 | 40 | 7 | 45 | 7 | 40 | 7 | 45 |
| 10 | Random | Pre-Trained | Both | 45 | 99 | 93 | 86 | 13 | 0 | 0 | 82 | 11 | 2 | 3 |
| 11 | Random | Pre-Trained | Focus | 211 | 99 | 95 | 90 | 8 | 0 | 0 | 87 | 7 | 0 | 3 |
| 12 | Random | Pre-Trained | Classify | 55 | 98 | 44 | 11 | 87 | 0 | 0 | 5 | 39 | 6 | 48 |
| 13 | Pre-Trained | Pre-Trained | - | 0 | 99 | 99 | 99 | 0 | 0 | 0 | 99 | 0 | 0 | 0 |
| 14 | Pre-Trained | Pre-Trained | Both | 3 | 99 | 99 | 99 | 0 | 0 | 0 | 99 | 0 | 0 | 0 |
| 15 | Pre-Trained | Pre-Trained | Focus | 1 | 99 | 99 | 99 | 0 | 0 | 0 | 99 | 0 | 0 | 0 |
| 16 | Pre-Trained | Pre-Trained | Classify | 23 | 99 | 97 | 96 | 3 | 0 | 0 | 95 | 2 | 0 | 1 |


### Tabel 7: Using Focus and Classify net of CNN - 6 Layer, analysis of FTPT, FFPT, FTPF, FFPF in above 16 experiments.
|Exp No.|Focus init |Classify init| Which module to be trained | analysis of FTPT, FFPT, FTPF, FFPF on Training Data | analysis of FTPT, FFPT, FTPF, FFPF on Testing Data |
|----|-----------|-------------|----------------------------|-----------------------------------------------------|----------------------------------------------------|
| 2  | Random | Random | Both | <img src= ./plots_and_images/6layer_cnn/train2.JPG width="800">  |  <img src= ./plots_and_images/6layer_cnn/test2.JPG width="800"> |
| 3  | Random | Random | Focus | <img src= ./plots_and_images/6layer_cnn/train3.JPG width="800">  |  <img src= ./plots_and_images/6layer_cnn/test3.JPG width="800"> |
| 4  | Random | Random | Classify | <img src= ./plots_and_images/6layer_cnn/train4.JPG width="800">  |  <img src= ./plots_and_images/6layer_cnn/test4.JPG width="800"> |
| 6  | Pre-Trained | Random | Both | <img src= ./plots_and_images/6layer_cnn/train6.JPG width="800">  |  <img src= ./plots_and_images/6layer_cnn/test6.JPG width="800"> |
| 7  | Pre-Trained | Random | Focus | <img src= ./plots_and_images/6layer_cnn/train7.JPG width="800">  |  <img src= ./plots_and_images/6layer_cnn/test7.JPG width="800"> |
| 8  | Pre-Trained | Random | Classify | <img src= ./plots_and_images/6layer_cnn/train8.JPG width="800">  |  <img src= ./plots_and_images/6layer_cnn/test8.JPG width="800"> |
| 10  | Random | Pre-Trained | Both | <img src= ./plots_and_images/6layer_cnn/train10.JPG width="800">  |  <img src= ./plots_and_images/6layer_cnn/test10.JPG width="800"> |
| 11  | Random | Pre-Trained | Focus | <img src= ./plots_and_images/6layer_cnn/train11.JPG width="800">  |  <img src= ./plots_and_images/6layer_cnn/test11.JPG width="800"> |
| 12  | Random | Pre-Trained | Classify | <img src= ./plots_and_images/6layer_cnn/train12.JPG width="800">  |  <img src= ./plots_and_images/6layer_cnn/test12.JPG width="800"> |
| 16  | Pre-Trained | Pre-Trained | Classify | <img src= ./plots_and_images/6layer_cnn/train16.JPG width="800">  |  <img src= ./plots_and_images/6layer_cnn/test16.JPG width="800"> |

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
