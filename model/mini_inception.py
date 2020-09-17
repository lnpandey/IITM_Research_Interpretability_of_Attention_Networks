import torch.nn as nn
import torch
import torch.nn.functional as F
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
        #self.conv1 = nn.Conv2d(3,self.f0,1)
        #self.conv3 = nn.Conv2d(3,self.f1,3,padding=1)
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
        #print(x1.shape)
        x2 = self.pool(x)
        #print(x2.shape)
        x = torch.cat((x1,x2),dim=1)
        
        return x

class inception_net(nn.Module):
    def __init__(self,inputs,outputs):
        super(inception_net,self).__init__()
        self.inputs  = inputs
        self.outputs = outputs
        self.conv1 = Conv_module(self.inputs,96,1,3,0)
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
        self.linear = nn.Linear(236,self.outputs)

    def forward(self,x):
        x = self.conv1.forward(x)
        x = self.incept1.forward(x)
        x = self.incept2.forward(x)
        x = self.downsample1.forward(x)
        x = self.incept3.forward(x)
        x = self.incept4.forward(x)
        x = self.incept5.forward(x)
        x = self.incept6.forward(x)
        x = self.downsample2.forward(x)
        x = self.incept7.forward(x)
        x = self.incept8.forward(x)
        x = self.pool(x)
        #print(x.shape)
        x = x.view(-1,1*1*236)
        x = self.linear(x) 
        return x