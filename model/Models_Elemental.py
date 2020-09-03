import numpy as np
import torch.nn as nn
import torch.optim as optim
import torch
import torchvision
import torch.nn.functional as F
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

class Focus_linear(nn.Module):
    '''
       linear focus network
    '''
    def __init__(self,inputs,output,K,d,pretrained=False):
        super(Focus_linear,self).__init__()
        self.inputs = inputs
        self.output = output
        self.K = K
        self.d = d
        self.pretrained = pretrained
        self.linear1 = nn.Linear(self.inputs,self.output)
    def forward(self,z):
        batch = z.shape[0]
        x = torch.zeros([batch,self.K],dtype=torch.float64)
        y = torch.zeros([batch,self.d], dtype=torch.float64)
        #x,y = x.to("cuda"),y.to("cuda")
        for i in range(self.K):
            x[:,i] = self.helper(z[:,self.d*i:self.d*i+self.d])[:,0]
        x = F.softmax(x,dim=1)   # alphas
        x1 = x[:,0]
        for i in range(self.K):
            x1 = x[:,i]          
            y = y+torch.mul(x1[:,None],z[:,self.d*i:self.d*i+self.d])
        return y , x 
    def helper(self,x):
        x = self.linear1(x)
        if self.pretrained==True:
          x = x[:,0] - x[:,1]
          x = x[:,None]
        return x
class Classification_linear(nn.Module):
    '''
    linear classification network
    '''
    def __init__(self,inputs,output):
        super(Classification_linear,self).__init__()
        self.inputs= inputs
        self.output = output
        self.linear1 = nn.Linear(self.inputs,self.output)

    def forward(self,x):
      x = self.linear1(x)
      return x  

class Focus_deep(nn.Module):
    '''
       deep focus network averaged at zeroth layer
       input : elemental data
    '''
    def __init__(self,inputs,output,K,d,pretrained=False):
        super(Focus_deep,self).__init__()
        self.inputs = inputs
        self.output = output
        self.K = K
        self.d  = d
        self.pretrained = pretrained
        self.linear1 = nn.Linear(self.inputs,50)  #,self.output)
        self.linear2 = nn.Linear(50,self.output) 
    def forward(self,z):
        batch = z.shape[0]
        x = torch.zeros([batch,self.K],dtype=torch.float64)
        y = torch.zeros([batch,self.d], dtype=torch.float64)
        #x,y = x.to("cuda"),y.to("cuda")
        for i in range(self.K):
            x[:,i] = self.helper(z[:,self.d*i:self.d*i+self.d])[:,0]
        x = F.softmax(x,dim=1)   # alphas
        x1 = x[:,0]
        for i in range(self.K):
            x1 = x[:,i]          
            y = y+torch.mul(x1[:,None],z[:,self.d*i:self.d*i+self.d])
        return y , x 
    def helper(self,x):
      x = F.relu(self.linear1(x))
      x = self.linear2(x)
      #print(x.shape)
      if self.pretrained ==True:
        x = x[:,0]-x[:,1]
        x = x[:,None]
      return x

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
