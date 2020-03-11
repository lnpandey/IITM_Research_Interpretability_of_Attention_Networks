import numpy as np
import torch.nn as nn
from Models import Module1,Focus_Module,Classification_Module
from Mosaic import mosaic_data, MosaicDataset
from torch.utils.data import Dataset,DataLoader

import torchvision.transforms as transforms
import torchvision
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=False, transform=transform)


testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=False, transform=transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size=10, shuffle=True)
testloader = torch.utils.data.DataLoader(testset, batch_size=10, shuffle=False)



focus_net =  Focus_Module(3,1).double()


# In[6]:


focus_net = focus_net.to(device)




classification_net  = Classification_Module(3,3).double()


# In[11]:


classification_net = classification_net.to(device)


# In[12]:



focus_net.load_state_dict(torch.load("focus_net.pt"))
classification_net.load_state_dict(torch.load("classification_net.pt"))



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

