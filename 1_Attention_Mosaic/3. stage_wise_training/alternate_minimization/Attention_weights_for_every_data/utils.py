from matplotlib import pyplot as plt
import numpy as np
import torch 
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
batch  = 3000


def attn_avg(x,beta):
  y = torch.zeros([batch,2], dtype=torch.float64)
  y = y.to(device)
  alpha = F.softmax(beta,dim=1)   # alphas
  #print(alpha[0],x[0,:])
  for i in range(9):            
    alpha1 = alpha[:,i]      
    y = y + torch.mul(alpha1[:,None],x[:,i])
  return y,alpha


def plot_decision_boundary(net,xy,data,beta,averaged_data):
  '''
    plots the decision boundary with averaged data and fg data
    net: what network
    xy : Min Max values for x-axis and y-axis (minx, maxx,miny,maxy)
    fgdata : original data {first c classes are foreground} as dictionary with keys X and Y 
    beta : beta vectors for each data point
    averaged_data: averaged_data
  '''


  n_fg_classes = 3
  xx,yy= np.meshgrid(np.arange(xy[0],xy[1],0.01),np.arange(xy[2],xy[3],0.01))
  X = np.concatenate((xx.reshape(-1,1),yy.reshape(-1,1)),axis=1)
  
  
  X = torch.Tensor(X).double().to(device)
  Y1 = net(X)
  X = X.to("cpu")
  Y1 = Y1.to("cpu")
  Y1 = Y1.detach().numpy()
  Y1 = torch.softmax(torch.Tensor(Y1),dim=1)
  _,Z4= torch.max(Y1,1)
   
  x = data[0]["X"]
  y= data[0]["Y"]
  num_classes = len(np.unique(y))
  idx= []
  for i in range(num_classes):
    #print(i,sum(y==i))
    idx.append(y==i)
  
  fig = plt.figure(figsize=(6,6))
  Z4 = Z4.reshape(xx.shape)
  plt.contourf(xx, yy, Z4, alpha=0.4)
  for i in range(n_fg_classes):
    plt.scatter(x[idx[i],0],x[idx[i],1],label="class_"+str(i),alpha=0.8)
  plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  plt.scatter(averaged_data[:,0],averaged_data[:,1],alpha=0.2)
  plt.show()
  fig.savefig("decision_boundary.png",bbox_inches="tight")



def plot_analysis(data,columns,xticks_list= [0,50,100,150,200]):
  fig= plt.figure(figsize=(6,6))
  plt.plot(data[columns[0]],data[columns[3]], label ="focus_true_pred_true ")
  plt.plot(data[columns[0]],data[columns[4]], label ="focus_false_pred_true ")
  plt.plot(data[columns[0]],data[columns[5]], label ="focus_true_pred_false ")
  plt.plot(data[columns[0]],data[columns[6]], label ="focus_false_pred_false ")
  plt.title("On Train set")
  plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  plt.xlabel("epochs")
  plt.ylabel("percentage of data")
  plt.xticks(xticks_list)
  #plt.vlines(vline_list,min(min(df_train[columns[3]]/300),min(df_train[columns[4]]/300),min(df_train[columns[5]]/300),min(df_train[columns[6]]/300)), max(max(df_train[columns[3]]/300),max(df_train[columns[4]]/300),max(df_train[columns[5]]/300),max(df_train[columns[6]]/300)),linestyles='dotted')
  plt.show()
  fig.savefig("train_analysis.pdf")
  fig.savefig("train_analysis.png")






