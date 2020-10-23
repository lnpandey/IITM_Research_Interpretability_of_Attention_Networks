### Creation of datasets
- First, we have created 10000 Mosaic images, such that Foreground image is always at index 0 (which does not affect training of the network).
- Labels of every Mosaic image is the class of foreground image present in that image.
- Dataset 'i' will contain 10000 image. Where each image is weighted average of 9 images present in Mosaic image. 
- Dataset 1 to Dataset 9 are made from same 10k Mosaic Images.
- In Dataset 'i', weight_of_random_image = i/9 and weight_of_rest_all_image = (9-i)/8*9. 

### Datasets:
number of correct averaging happened for dataset 1 is 1051
the averaging are done as  [1051 1145 1064 1091 1140 1163 1109 1108 1129]
number of correct averaging happened for dataset 2 is 1129
the averaging are done as  [1129 1119 1083 1131 1099 1122 1116 1148 1053]
number of correct averaging happened for dataset 3 is 1126
the averaging are done as  [1126 1138 1125 1105 1128 1130 1077 1071 1100]
number of correct averaging happened for dataset 4 is 1102
the averaging are done as  [1102 1112 1104 1133 1091 1120 1119 1072 1147]
number of correct averaging happened for dataset 5 is 1121
the averaging are done as  [1121 1075 1104 1104 1093 1100 1141 1097 1165]
number of correct averaging happened for dataset 6 is 1092
the averaging are done as  [1092 1103 1125 1064 1138 1088 1135 1145 1110]
number of correct averaging happened for dataset 7 is 1087
the averaging are done as  [1087 1129 1083 1123 1139 1078 1120 1148 1093]
number of correct averaging happened for dataset 8 is 1125
the averaging are done as  [1125 1087 1080 1103 1127 1101 1126 1175 1076]
number of correct averaging happened for dataset 9 is 1152
the averaging are done as  [1152 1072 1110 1165 1104 1086 1115 1069 1127]

### Experiment brief:
- Model ( what network) is trained on Dataset 'i', and Tested on all Dataset 'j', where j is not equal to i, j belongs to 1 to 9.


### Analysis of Accuracy on Training & Testing Data

| train\ test  | test on dataset 1 | test on dataset 2 | test on dataset 3 | test on dataset 4 | test on dataset 5 | test on dataset 6 | test on dataset 7 | test on dataset 8 | test on dataset 9|
|----------|-----|-----|-----|-----|-----|-----|-----|-----|----|
| train on dataset 1      | - | 87| 57 | 46 | 41 | 39| 38 | 38 | 37 |
| train on dataset 2      | 85 | - | 54 | 46 | 41 | 39 | 38 | 37 | 36 |
| train on dataset 3      | 59 | 56 | - | 47 | 44 | 41 |40 | 38 | 38 |     
| train on dataset 4      | 46 | 46 | 46 | - | 44 | 43 | 41 | 40 | 40 |
| train on dataset 5      | 43 | 42| 44 | 44 | - | 43 | 42 | 42| 41| 
| train on dataset 6      | 38 | 40 | 41 | 42 | 43 | - | 43 | 42 | 42 | 
| train on dataset 7      | 37 | 38 | 40| 42 |43| 44 | - | 43| 43 | 
| train on dataset 8      | 36 | 36| 38 | 40 | 42 | 42 | 43 | - | 42 | 
| train on dataset 9      | 35 | 35 | 37 | 39 | 41| 41 | 42 | 42 | - | 


### Plot of Training loss for all the Datasets :
 ![](train_loss.JPG)



### Architecture of the Model
```python
class Conv_module(nn.Module):
    def __init__(self,inp_ch,f,s,k,pad):
        super(Conv_module,self).__init__()
        self.inp_ch = inp_ch
        self.f = f
        self.s = s 
        self.k = k 
        self.pad = pad
        self.conv = nn.Conv2d(self.inp_ch,self.f,k,stride=s,padding=self.pad)
        self.bn = nn.BatchNorm2d(self.f)
        self.act = nn.ReLU()
    def forward(self,x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.act(x)
        return x
        
class inception_module(nn.Module):
    def __init__(self,inp_ch,f0,f1):
        super(inception_module, self).__init__()
        self.inp_ch = inp_ch
        self.f0 = f0
        self.f1 = f1
        self.conv1 = Conv_module(self.inp_ch,self.f0,1,1,pad=0)
        self.conv3 = Conv_module(self.inp_ch,self.f1,1,3,pad=1)
    def forward(self,x):
        x1 = self.conv1.forward(x)
        x3 = self.conv3.forward(x)
        x = torch.cat((x1,x3),dim=1)
        return x
        
class downsample_module(nn.Module):
    def __init__(self,inp_ch,f):
        super(downsample_module,self).__init__()
        self.inp_ch = inp_ch
        self.f = f
        self.conv = Conv_module(self.inp_ch,self.f,2,3,pad=0)
        self.pool = nn.MaxPool2d(3,stride=2,padding=0)
    def forward(self,x):
        x1 = self.conv(x)
        x2 = self.pool(x)
        x = torch.cat((x1,x2),dim=1)
        return x,x1

class inception_net(nn.Module):
    def __init__(self):
        super(inception_net,self).__init__()
        self.conv1 = Conv_module(3,96,1,3,0)
        self.incept1 = inception_module(96,32,32)
        self.incept2 = inception_module(64,32,48)
        self.downsample1 = downsample_module(80,80)
        self.incept3 = inception_module(160,112,48)
        self.incept4 = inception_module(160,96,64)
        self.incept5 = inception_module(160,80,80)
        self.incept6 = inception_module(160,48,96)
        self.downsample2 = downsample_module(144,96)
        self.incept7 = inception_module(240,176,60)
        self.incept8 = inception_module(236,176,60)
        self.pool = nn.AvgPool2d(5)
        self.linear = nn.Linear(236,3)
    def forward(self,x):
        x = self.conv1.forward(x)
        x = self.incept1.forward(x)
        x = self.incept2.forward(x)
        x,act4 = self.downsample1.forward(x)
        x = self.incept3.forward(x)
        x = self.incept4.forward(x)
        x = self.incept5.forward(x)
        x = self.incept6.forward(x)
        x,act9 = self.downsample2.forward(x)
        x = self.incept7.forward(x)
        x = self.incept8.forward(x)
        x = self.pool(x)
        x = x.view(-1,1*1*236)
        x = self.linear(x) 
        return x

```

