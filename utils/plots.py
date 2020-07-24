import torch
from matplotlib import pyplot as plt
import numpy as np

def plot_scatter(x,y,title,legend = True,save =False):
  fig = plt.figure(figsize = (6,6))
  ax = fig.gca()
  n = len(np.unique(y))
  for i in range(n):
    ax.scatter(x[y==i,0],x[y==i,1],label="class_"+str(i))
  if legend == True:
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  if save == True:
    fig.savefig(title + ".png")
    fig.savefig(title + ".pdf")

def focus_map(focus_net):
  fig = plt.figure(figsize=(6,6))
  ax = fig.gca()
  X,Y = torch.meshgrid(torch.linspace(-10,155,500), torch.linspace(-10,155,500))
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
  #ax.scatter(x[y==0,0],x[y==0,1])
  #ax.scatter(x[y==1,0],x[y==1,1])
  fig.colorbar(cax)

def classification_map(class_net,x,y):
  fig = plt.figure(figsize=(6,6))
  ax = fig.gca()
  X,Y = torch.meshgrid(torch.linspace(-10,155,500), torch.linspace(-10,155,500))
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
  ax.scatter(x[y==0,0],x[y==0,1],s = 50,c= 'tab:orange')
  ax.scatter(x[y==1,0],x[y==1,1],s = 50,c = 'r')
  ax.scatter(x[y==2,0],x[y==2,1],s = 50,c = 'y')
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

def plot_analysis(ax, data,legend =True):
  #columns = data.columns
  #fig = plt.figure(figsize = (6,6))
  #ax = fig.gca()
  ax.plot(data[0],data[1], label ="ftpt")
  ax.plot(data[0],data[2], label ="ffpt")
  ax.plot(data[0],data[3], label = "ftpf") 
  ax.plot(data[0],data[4], label ="ffpf")
  #if legend == True:
    #ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  ax.set_xlabel("epochs")
  ax.set_ylabel("data")
  #fig.savefig(title+".png")
  #fig.savefig(title+".pdf")
  return ax

def save_fig(fig,title):
  fig.savefig(title+".png")
  fig.savefig(title+".pdf")  
def imshow(img):
  img = img / 2 + 0.5     # unnormalize
  #npimg = img#.numpy()
  fig = plt.figure(figsize=(6,6))
  ax = fig.gca()
  ax.imshow(np.transpose(npimg, (1, 2, 0)))
  ax.show()
    