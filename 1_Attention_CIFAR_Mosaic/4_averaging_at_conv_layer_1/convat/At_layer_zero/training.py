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
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=False, transform=transform)


testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=False, transform=transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size=10, shuffle=True)
testloader = torch.utils.data.DataLoader(testset, batch_size=10, shuffle=False)


# In[3]:


mosaic_list_of_images,mosaic_label,fore_idx = mosaic_data(trainloader,desired_num=30000,total=50000)


# In[4]:


batch = 250
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


print(avg_data.shape,alpha.shape)


# In[10]:


classification_net  = Classification_Module(3,3).double()


# In[11]:


classification_net = classification_net.to(device)


# In[12]:


classification_net(avg_data)


# In[13]:


optimizer_focus = optim.SGD(focus_net.parameters(),lr = 0.01)
optimizer_classification = optim.SGD(classification_net.parameters(),lr =0.01)


# In[14]:


criterion = nn.CrossEntropyLoss()


# In[ ]:


for epoch in range(250):  # loop over the dataset multiple times
    running_loss = 0.0
    cnt=0
    iteration = 30000 // batch
    
    for i, data in  enumerate(mosaic_loader):
        inputs , labels , fgrnd_idx = data
        inputs,labels = inputs.to("cuda"),labels.to("cuda")
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
        mini = 40
        if cnt % mini == mini-1:    # print every mini mini-batches
            print('[%d, %5d] loss: %.3f' %(epoch + 1, cnt + 1, running_loss / mini))
            running_loss = 0.0
        cnt=cnt+1
print('Finished Training')    
            


# In[ ]:


train_acc = 0
for i, data in enumerate(mosaic_loader):
    inputs,labels,_ = data
    inputs,labels = inputs.to(device), labels.to(device)
    
    avg_data,alphas = focus_net(inputs)
    outputs = classification_net(avg_data)
    _,predicted = torch.max(outputs.data,1)
    # print(predicted.detach().cpu().numpy())
    train_acc += sum(predicted.cpu().numpy() == labels.cpu().numpy())
print("percentage train accuracy: ",train_acc/300) 

torch.save(focus_net.state_dict(),"focus_net.pt")
torch.save(classification_net.state_dict(),"classification_net.pt")
 
'''
mimages_val,mlabel_val,fidx_val = mosaic_data(trainloader,desired_num=10000,total=50000)


batch = 250
msd_val = MosaicDataset(mimages_val, mlabel_val , fidx_val)
mloader_val = DataLoader( msd_val,batch_size= batch ,shuffle=True)


val_acc = 0
for i, data in enumerate(mloader_val):
    inputs,labels,_ = data
    inputs,labels = inputs.to(device), labels.to(device)

    avg_data,alphas = focus_net(inputs)
    outputs = classification_net(avg_data)
    _,predicted = torch.max(outputs.data,1)

    val_acc +=sum(predicted.cpu().numpy() == labels.cpu().numpy())
print("percentage validation accuracy: ",val_acc/100)




mimages_test,mlabel_test,fidx_test = mosaic_data(testloader,desired_num=10000,total=10000)


batch = 250
msd_test = MosaicDataset(mimages_test, mlabel_test , fidx_test)
mloader_test = DataLoader( msd_test,batch_size= batch ,shuffle=True)


test_acc = 0
for i, data in enumerate(mloader_test):
    inputs,labels,_ = data
    inputs,labels = inputs.to(device), labels.to(device)

    avg_data,alphas = focus_net(inputs)
    outputs = classification_net(avg_data)
    _,predicted = torch.max(outputs.data,1)

    test_acc +=sum(predicted.cpu().numpy() == labels.cpu().numpy())
print("percentage test accuracy: ",test_acc/100)
'''
