import torch
from matplotlib import pyplot as plt
import numpy as np

def plot_scatter(x,y,title,legend = True):
  fig = plt.figure(figsize = (6,6))
  ax = fig.gca()
  n = len(np.unique(y))
  for i in range(n):
    ax.scatter(x[y==i,0],x[y==i,1],label="class_"+str(i))
  if legend == True:
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  fig.savefig(title + ".png")
  fig.savefig(title + ".pdf")

def focus_map(focus_net):
  fig = plt.figure(figsize=(6,6))
  ax = fig.gca()
  X,Y = torch.meshgrid(torch.linspace(-5,150,500), torch.linspace(-5,150,500))
  n=X.shape[0]*X.shape[1]
  data = torch.zeros((n,2)).double()
  data[:,0]=X.reshape((-1,))
  data[:,1]=Y.reshape((-1,))
  Z = []
  batch = 50
  iter = data.shape[0]//batch
  for i in range(iter):
    #print(data[i*batch:(i+1)*batch].shape)
    Z_ = focus_net.helper(data[i*batch:(i+1)*batch]).detach().numpy()
    Z.append(Z_)
  Z = np.concatenate(Z,axis=0)
  Z = Z.reshape(X.shape)
  ax.set_title("focus_map")
  cax = ax.contourf(X,Y,Z,)
  fig.colorbar(cax)

def classification_map(class_net):
  fig = plt.figure(figsize=(6,6))
  ax = fig.gca()
  X,Y = torch.meshgrid(torch.linspace(-5,150,500), torch.linspace(-5,150,500))
  n=X.shape[0]*X.shape[1]
  data = torch.zeros((n,2)).double()
  data[:,0]=X.reshape((-1,))
  data[:,1]=Y.reshape((-1,))
  Z = []
  batch =50
  iter = data.shape[0]//batch
  for i in range(iter):
    #print(data[i*batch:(i+1)*batch].shape)
    Z_ = class_net(data[i*batch:(i+1)*batch]).detach().numpy()
    Z.append(Z_)
  Z = np.concatenate(Z,axis=0)
  Z1 = Z[:,0].reshape(X.shape)
  Z2 = Z[:,1].reshape(X.shape)
  ax.set_title("classification map")
  cmap_val= torch.sigmoid(torch.Tensor(Z1- Z2) ).numpy() 
  cax = ax.contourf(X,Y,Z1)
  fig.colorbar(cax)


def disp_plot(data,avg_data,true_label,pred_label,alpha,true_idx):
    fig = plt.figure(figsize=(6,6))
    ax = fig.gca()
    data = data.numpy()
    alpha = alpha.detach().numpy()
    avg_data = avg_data.detach().numpy()
 
    x = data[:,0:2]
    y = data[:,2:4]
    z = data[:,4:6]
    colors = ['b','g','r','c','m','y','k','teal','indigo','peru']
    for i in range(len(x)):
        ax.plot([x[i,0],y[i,0]],[x[i,1],y[i,1]],color= colors[i])
        ax.plot([z[i,0],y[i,0]],[z[i,1],y[i,1]],color= colors[i])
        ax.plot([x[i,0],z[i,0]],[x[i,1],z[i,1]],color= colors[i])
        ax.plot(avg_data[i,0], avg_data[i,1],marker="x", markersize=12, color= colors[i])

def plot_training_metric(data,title):
  fig = plt.figure(figsize = (6,6))
  ax = fig.gca()
  ax.plot(data,label = title)
  fig.savefig(title + ".png")
  fig.savefig(title + ".pdf")

def plot_analysis(data,title,legend =True):
  columns = data.columns
  fig = plt.figure(figsize = (6,6))
  ax = fig.gca()
  ax.plot(data[columns[0]],data[columns[1]], label =columns[1])
  ax.plot(data[columns[0]],data[columns[2]], label =columns[2])
  ax.plot(data[columns[0]],data[columns[3]], label =columns[3]) 
  ax.plot(data[columns[0]],data[columns[4]], label =columns[4])
  if legend == True:
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  ax.xlabel("epochs")
  ax.ylabel("data")
  fig.savefig(title+".png")
  fig.savefig(title+".pdf")
    