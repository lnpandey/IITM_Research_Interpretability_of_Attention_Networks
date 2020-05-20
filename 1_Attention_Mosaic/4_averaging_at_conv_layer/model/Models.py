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
    
    self.conv1 = nn.Conv2d(self.input, 6, 5)
    self.pool = nn.MaxPool2d(2, 2)
    self.conv2 = nn.Conv2d(6, 12, 5)
    self.conv3 = nn.Conv2d(12,20,5)
    self.fc1 = nn.Linear(20 * 6 * 6, 120)
    self.fc2 = nn.Linear(120, 84)
    self.fc3 = nn.Linear(84, 10)
    self.fc4 = nn.Linear(10,self.output)

  def forward(self,x):
    x = self.pool(F.relu(self.conv1(x)))
    x = F.relu(self.conv2(x))
    x = F.relu(self.conv3(x))
    #print(x.shape)
    x = x.view(-1, 20* 6 * 6)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.fc3(x))
    x = self.fc4(x)
    return x

class Module2(nn.Module):
  
  '''
  Input :  32X32X3 image
  Convolutional Network with 4 Conv layers 
  '''
  def __init__(self,inp,out):
    super(Module2,self).__init__()
    self.input = inp
    self.output = out
    
    self.conv1 = nn.Conv2d(self.input, 6, 5)
    self.pool = nn.MaxPool2d(2, 2)
    self.conv2 = nn.Conv2d(6, 12, 5)
    self.conv3 = nn.Conv2d(12,20,5)
    self.fc1 = nn.Linear(20 * 6 * 6, 120)
    self.fc2 = nn.Linear(120, 84)
    self.fc3 = nn.Linear(84, 10)
    self.fc4 = nn.Linear(10,self.output)

  def forward(self,x):
    x = self.pool(F.relu(self.conv1(x)))
    x = F.relu(self.conv2(x))
    x = self.conv3(x)
    #print(x.shape)
    x1 = F.tanh(x)
    x = F.relu(x)
    x = x.view(-1, 20* 6 * 6)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.fc3(x))
    x = self.fc4(x)
    return x,x1
		

class Focus_Module2(nn.Module):
  '''
  Focus Network uses Module 2
  '''
  def __init__(self,inp,out):
    super(Focus_Module2, self).__init__()
    self.input = inp
    self.output = out
    self.module = Module2(self.input,self.output)

  def forward(self, z):
    #print("flag1",z.shape)
    #print("flag2",z[:,0].shape)
    batch = z.shape[0]
    x = torch.zeros([batch,9],dtype=torch.float64)
    y = torch.zeros([batch,20, 6,6], dtype=torch.float64)
    feature = torch.zeros([batch,9,20,6,6],dtype=torch.float64)
    x,y = x.to(device),y.to(device)
    feature = feature.to(device)
    for i in range(9):
      alp,ftr= self.helper(z[:,i])
      #print("flag3",ftr.shape)
      x[:,i] = alp[:,0]
      feature[:,i] = ftr
      
      
    x = F.softmax(x,dim=1)   # alphas
    
    #x1 = x[:,0]
    #torch.mul(x1[:,None,None,None],z[:,0])

    for i in range(9):            
      x1 = x[:,i]          
      y = y + torch.mul(x1[:,None,None,None],feature[:,i])
    return y , x 
  
  def helper(self,x):
    x,features = self.module(x)
    #print(x.shape)
    return x,features




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
    print(z.shape)
    print()
    batch = z.shape[0]
    x = torch.zeros([batch,9],dtype=torch.float64)
    y = torch.zeros([batch,self.input, 32,32], dtype=torch.float64)
    x,y = x.to(device),y.to(device)
    for i in range(9):
      x[:,i] = self.helper(z[:,i])[:,0]
    x = F.softmax(x,dim=1)   # alphas
    
    #x1 = x[:,0]
    #torch.mul(x1[:,None,None,None],z[:,0])

    for i in range(9):            
      x1 = x[:,i]          
      y = y + torch.mul(x1[:,None,None,None],z[:,i])
    return y , x 
  
  def helper(self,x):
    x = self.module1(x)
    #print(x.shape)
    return x

class Classification_Module(nn.Module):
  '''
  Classification Network  
  '''
  def __init__(self,inp,out):
    super(Classification_Module,self).__init__()
    self.input = inp
    self.output = out
    self.conv1 = nn.Conv2d(self.input, 6, 5)
    self.pool = nn.MaxPool2d(2, 2)
    self.conv2 = nn.Conv2d(6, 8, 5)
    self.fc1 = nn.Linear(8 * 5 * 5, 120)
    self.fc2 = nn.Linear(120, 84)
    self.fc3 = nn.Linear(84, 10)
    self.fc4 = nn.Linear(10,self.output)
  def forward(self,x):
    x = self.pool(F.relu(self.conv1(x)))
    x = self.pool(F.relu(self.conv2(x)))
    x = x.view(-1,8*5*5)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.fc3(x))
    x = self.fc4(x)
    return x

class Classification_Module2(nn.Module):
  '''
  Classification Network  
  '''
  def __init__(self,inp,out):
    super(Classification_Module2,self).__init__()
    self.input = inp
    self.output = out
    #self.conv1 = nn.Conv2d(self.input, 8, 3)
    #self.pool = nn.MaxPool2d(2, 2)
    #self.conv2 = nn.Conv2d(24, 32, 3)
    self.fc1 = nn.Linear(20 *6  *6 , 120)
    self.fc2 = nn.Linear(120, 84)
    self.fc3 = nn.Linear(84, 10)
    self.fc4 = nn.Linear(10,self.output)
  def forward(self,x):
    #x = self.pool(F.relu(self.conv1(x)))
    #x = F.relu(self.conv2(x))
    #print("flag1",x.shape)
    x = x.view(-1,20*6*6)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.fc3(x))
    x = self.fc4(x)
    return x



    
