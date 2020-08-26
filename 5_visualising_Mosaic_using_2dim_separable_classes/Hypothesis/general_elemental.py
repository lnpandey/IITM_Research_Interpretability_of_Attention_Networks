# -*- coding: utf-8 -*-
"""General_Elemental.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PxgaOkRCzJ3-487eVBicxo7J7mY7EAFP
"""

from sklearn.datasets import make_classification
from train_model import train_network
import torch
import numpy as np
from matplotlib import pyplot as plt
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

n_mosaic = 3000
K = 10
d = 4
n_classes = 5

x,y = make_classification(n_samples=500,n_features=d,n_informative=d,n_redundant=0,n_repeated= 0,n_classes=n_classes,n_clusters_per_class=1,flip_y=0.2,random_state=1234)   #D_4 random_state 1234

data = {'X':x,'Y':y}
np.save("data_2.npy",data)

# fg vs bg
y1 = np.zeros(y.shape,dtype=np.long)
indices = np.logical_or(y == 0,y==1) 
y1[indices] = 0
y1[np.logical_not(indices)] = 1

# fg1 vs fg2
index = np.logical_or(y==0,y==1)
x2 = x[index,:]
y2 = np.zeros(index.shape,dtype=np.long)
y2 = y[index]

# Commented out IPython magic to ensure Python compatibility.
import torch.nn as nn
import torch.optim as optim
# %matplotlib inline
from torch.utils.data import Dataset, DataLoader

class Net(nn.Module):
  def __init__(self):
    super(Net,self).__init__()
    self.linear1 = nn.Linear(d,2)
    # self.linear2 = nn.Linear(50,50)
    # self.linear3 = nn.Linear(50,50)
    # self.linear4 = nn.Linear(50,2)
  def forward(self,x):
    x = self.linear1(x)
    # x = F.relu(self.linear2(x))
    # x = F.relu(self.linear3(x))
    # x = F.relu(self.linear4(x))
    return x

class MosaicDataset(Dataset):
  """MosaicDataset dataset."""

  def __init__(self, mosaic_list, mosaic_label):
    """
      Args:
        csv_file (string): Path to the csv file with annotations.
        root_dir (string): Directory with all the images.
        transform (callable, optional): Optional transform to be applied
            on a sample.
    """
    self.mosaic = mosaic_list
    self.label = mosaic_label
    

  def __len__(self):
    return len(self.label)

  def __getitem__(self, idx):
    return self.mosaic[idx] , self.label[idx]

batch = 250
# dataset = MosaicDataset(x2,y2)
# traindataloader = DataLoader( dataset,batch_size= batch ,shuffle=True)

dataset = MosaicDataset(x,y1)
traindataloader = DataLoader( dataset,batch_size= batch ,shuffle=True)
net = Net().double()
net =net.to(device)
train_model =train_network(net,traindataloader)
train_model.training(epochs=200,mini=1)

_,_=train_model.predict(traindataloader,True)
plt.plot(train_model.train_loss)

dataset = MosaicDataset(x2,y2)
traindataloader = DataLoader( dataset,batch_size= batch ,shuffle=True)
net = Net().double()
net =net.to(device)
train_model =train_network(net,traindataloader)
train_model.training(epochs=100,mini=1)

_,_=train_model.predict(traindataloader,True)
plt.plot(train_model.train_loss)

from plots import plot_analysis,focus_map,classification_map
from Models_Elemental import Focus_linear,Classification_linear
from Models_Elemental import Focus_deep,Classification_deep
from train_mosaic_new import train_mosaic_network



idx= []
for i in range(n_classes):
    print(i,sum(y==i))
    idx.append(y==i)

foreground_classes = {'class_0' ,'class_1'}

background_classes = {'class_2','class_3'}#,'class_4', 'class_5', 'class_6','class_7', 'class_8', 'class_9'}

mosaic_list =[]
mosaic_label = []
fore_idx=[]
for j in range(n_mosaic):
    fg_class  = np.random.randint(0,len(foreground_classes))
    fg_idx = np.random.randint(0,K)
    a = []
    for i in range(K):
        if i == fg_idx:
            b = np.random.choice(np.where(idx[fg_class]==True)[0],size=1)
            a.append(x[b])
#             print("foreground "+str(fg_class)+" present at " + str(fg_idx))
        else:
            bg_class = np.random.randint(len(foreground_classes),n_classes)
            b = np.random.choice(np.where(idx[bg_class]==True)[0],size=1)
            a.append(x[b])
#             print("background "+str(bg_class)+" present at " + str(i))
    a = np.concatenate(a,axis=0)
    mosaic_list.append(np.reshape(a,(d*K,1)))
    mosaic_label.append(fg_class)
    fore_idx.append(fg_idx)

mosaic_list = np.concatenate(mosaic_list,axis=1).T
mosaic_list.shape

np.unique(mosaic_label)

mosaic_data = {"X":mosaic_list,"Y":mosaic_label,"foreground_indices":fore_idx}
np.save("mosaic_data_4.npy",mosaic_data)

from sklearn.svm import SVC
sv = SVC(C=100,kernel="linear")
sv.fit(mosaic_list,mosaic_label)
print(sv.score(mosaic_list,mosaic_label))

class MosaicDataset(Dataset):
  """MosaicDataset dataset."""

  def __init__(self, mosaic_list, mosaic_label, fore_idx):
    """
      Args:
        csv_file (string): Path to the csv file with annotations.
        root_dir (string): Directory with all the images.
        transform (callable, optional): Optional transform to be applied
            on a sample.
    """
    self.mosaic = mosaic_list
    self.label = mosaic_label
    self.fore_idx = fore_idx

  def __len__(self):
    return len(self.label)

  def __getitem__(self, idx):
    return self.mosaic[idx] , self.label[idx], self.fore_idx[idx]

batch = 250
msd = MosaicDataset(mosaic_list, mosaic_label , fore_idx)
train_loader = DataLoader( msd,batch_size= batch ,shuffle=True)

where = Focus_linear(d,1,K,d).double()
what = Classification_linear(d,2).double()

train_mosaic = train_mosaic_network(where,what,train_loader,elemental=False,lr=0.01)

train_mosaic.training(epochs=200,mini=3)

plot_analysis(np.array(train_mosaic.train_analysis))

plt.plot(train_mosaic.train_loss)

_,_,_,_ = train_mosaic.predict(train_loader,True)

where_deep = Focus_deep(d,1,K,d).double()
what_deep = Classification_deep(d,2).double()

train_mosaic_deep = train_mosaic_network(where_deep,what_deep,train_loader,elemental=False,lr =0.01)
train_mosaic_deep.training(epochs=700,mini=3)

plot_analysis(np.array(train_mosaic_deep.train_analysis))

plt.plot(train_mosaic_deep.train_loss)

_,_,_,_ = train_mosaic_deep.predict(train_loader,True)

