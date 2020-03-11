import numpy as np
import torch.nn as nn
import torch.optim as optim
import torch
import torchvision
import torch.nn.functional as F
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

class Module1(nn.Module):
  
  '''
  Input :  32X32X3 image
  Convolutional Network with 4 Conv layers 
  '''
  def __init__(self,inp,out):
    super(Module1,self).__init__()
    self.input = inp
    self.output = out
    
    self.conv1 = nn.Conv2d(self.input, 8, 5)
    self.pool1 = nn.MaxPool2d(2, 2)
    self.conv2 = nn.Conv2d(8,16,5,padding=3)
    #self.pool2 = nn.MaxPool2d(2,2)
    self.conv3 = nn.Conv2d(16,16,5)
    self.conv4 = nn.Conv2d(16,16,3)
    self.linear1 = nn.Linear(16*10*10,self.output)

  def forward(self,x):
    x = F.relu(self.conv1(x))
    x = self.pool1(x)
    x = F.relu(self.conv2(x))
    #print(x.shape)
    x1 = x
    #x = self.pool2(x)
    x = F.relu(self.conv3(x))
    x = F.relu(self.conv4(x))
    #print("flag 1",x.shape)
    x = x.view(-1,16*10*10)
    x = self.linear1(x)
    
    
    return x,x1
		



class Focus_Module(nn.Module):
  '''
  Focus Network uses Module 1
  '''
  def __init__(self,inp,out):
    super(Focus_Module, self).__init__()
    self.input = inp
    self.output = out
    self.module1 = Module1(self.input,self.output)

  def forward(self, z):
    batch = z.shape[0]
    x = torch.zeros([batch,9],dtype=torch.float64)
    y = torch.zeros([batch,16, 16,16], dtype=torch.float64)
    x,y = x.to(device),y.to(device)
    z11 = []
    for i in range(9):
        ll,z1 = self.helper(z[:,i])
        x[:,i] = ll[:,0]
        z11.append(z1)
    print(x)
    x = F.softmax(x,dim=1)   # alphas
    #print(np.shape(z11))
    x1 = x[:,0]
    torch.mul(x1[:,None,None,None],z11[0])

    for i in range(9):
        x1 = x[:,i]          
        y = y + torch.mul(x1[:,None,None,None],z11[i])
    return y , x 
  
  def helper(self,x):
    x,x1 = self.module1(x)
    #print(x.shape)
    return x,x1

class Classification_Module(nn.Module):
  '''
  Classification Network  
  '''
  def __init__(self,inp,out):
    super(Classification_Module,self).__init__()
    self.input = inp
    self.output = out
    self.conv1 = nn.Conv2d(self.input, 32, 5,padding=3)
    self.pool1 = nn.MaxPool2d(2, 2)
    self.conv2 = nn.Conv2d(32,32,5,padding =1)
    #self.pool2 = nn.MaxPool2d(2,2)
    self.conv3 = nn.Conv2d(32,64,5,padding =1)
    self.conv4 = nn.Conv2d(64,64,3)
    self.linear1 = nn.Linear(64*3*3,self.output)
  def forward(self,x):
    x = F.relu(self.conv1(x))
    x = self.pool1(x)
    x = F.relu(self.conv2(x))
    #x = self.pool2(x)
    x = F.relu(self.conv3(x))
    x = F.relu(self.conv4(x))
    #print("flag 1",x.shape)
    x = x.view(-1,64*3*3)
    x = self.linear1(x)
    return x 



    
