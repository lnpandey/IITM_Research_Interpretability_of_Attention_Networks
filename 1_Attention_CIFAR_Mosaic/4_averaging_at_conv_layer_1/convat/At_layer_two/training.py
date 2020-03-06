#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Models import Module1,Focus_Module,Classification_Module
from Mosaic import mosaic_data, MosaicDataset
from torch.utils.data import Dataset,DataLoader
import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim

import torch.nn as nn

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)


# In[2]:


transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5) )])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)


testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size=10, shuffle=True)
testloader = torch.utils.data.DataLoader(testset, batch_size=10, shuffle=False)


# In[3]:


mosaic_list_of_images,mosaic_label,fore_idx = mosaic_data(trainloader,30000,50000)


# In[4]:


batch = 1000
msd = MosaicDataset(mosaic_list_of_images, mosaic_label , fore_idx)
mosaic_loader = DataLoader( msd,batch_size= batch ,shuffle=True)


# In[5]:


focus_net =  Focus_Module(3,1).double()


# In[6]:


focus_net = focus_net.to(device)


# In[7]:


i,_,_ = iter(mosaic_loader).next()


# In[8]:


avg_data,alpha = focus_net(i.to(device))


# In[9]:


avg_data.shape,alpha.shape


# In[10]:


classification_net  = Classification_Module(16,3).double()


# In[11]:


classification_net = classification_net.to(device)


# In[12]:


classification_net(avg_data)


# In[13]:


optimizer_focus = optim.SGD(focus_net.parameters(),lr = 0.001)
optimizer_classification = optim.SGD(classification_net.parameters(),lr =0.001)


# In[14]:


criterion = nn.CrossEntropyLoss()


# In[ ]:


for epoch in range(1000):  # loop over the dataset multiple times
    running_loss = 0.0
    cnt=0
    iteration = 30000 // batch
    
    for i, data in  enumerate(mosaic_loader):
        inputs , labels , fgrnd_idx = data
        inputs,labels = inputs.to(device),labels.to(device)
        optimizer_focus.zero_grad()
        optimizer_classification.zero_grad()
        avg_data , alphas = focus_net(inputs)
        outputs = classification_net(avg_data)
        _, predicted = torch.max(outputs.data, 1)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer_focus.step()
        optimizer_classification.step()
        running_loss += loss.item()
        mini = 30
        if cnt % mini == mini-1:    # print every mini mini-batches
            print('[%d, %5d] loss: %.3f' %(epoch + 1, cnt + 1, running_loss / mini))
            running_loss = 0.0
        cnt=cnt+1
print('Finished Training')    
            


# In[ ]:


train_acc = 0 
for data in mosaic_loader:
    inputs,labels,_ = data
    inputs,labels = inputs.to(device), labels.to(device)
    avg_inp,alphas = focus_net(inputs)
    outputs = classification_net(avg_inp)
    _,predicted = torch.max(outputs.data,1)
    #print(predicted.cpu().numpy(),"labels",labels.cpu().numpy())
    train_acc+=sum(predicted.cpu().numpy()== labels.cpu().numpy())
print("mosaic_data_training_accuracy :",train_acc/30000)


# In[ ]:

torch.save(focus_net.state_dict(),"focus_net.pt")
torch.save(classification_net.state_dict(),"classification_net.pt")

#train_acc/30000


# In[ ]:




