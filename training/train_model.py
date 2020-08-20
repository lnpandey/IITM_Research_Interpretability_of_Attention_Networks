import torch
from matplotlib import pyplot as plt
import numpy as np
from plots import plot_analysis,save_fig
import torch.optim as optim
import torch.nn as nn
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class train_network():
  '''
     train mosaic data 
  '''
  def __init__(self,net,trainloader,testloader=None):
    super(train_network,self).__init__()
    self.net = net
    self.trainloader = trainloader
    self.testloader = testloader
    self.optimizer = optim.SGD(self.net.parameters(),lr = 0.01,momentum=0.9)
    self.criterion = criterion = nn.CrossEntropyLoss() 
    self.train_loss = [] 
  def train_epoch(self,epoch,mini=80 ):
    '''
       trains a one epoch
       mini: print loss after mini number of batches default value 80
    '''
    running_loss = 0
    cnt = 0
    ep_loss = []
    self.net.train()
    for i, data in  enumerate(self.trainloader):
      inputs , labels = data
      inputs,labels = inputs.to(device),labels.to(device)
  
      self.optimizer.zero_grad()
    
      outputs = self.net(inputs)
    
      _, predicted = torch.max(outputs.data, 1)
      loss = self.criterion(outputs, labels)
      loss.backward()
    
      self.optimizer.step()
    
      running_loss += loss.item()
      #mini = 80
    
      if cnt % mini == mini-1:    # print every mini mini-batches
        print('[%d, %5d] loss: %.3f' %(epoch + 1, cnt + 1, running_loss / mini))
        ep_loss.append(running_loss/mini)
        running_loss = 0.0  
      cnt=cnt+1
        
    return ep_loss


  def training(self,epochs=100000,tol=0.01,mini=80, epochs_or_loss_flag = True):
    '''
       train given models for number of epochs 
       epochs=100000 by default
       train_loss=0.001 by default
       epochs_or_loss_flag = True , if training by epochs, if epochs_or_loss_flag = False, then train by training loss.
       mini : print loss after mini number of batches default value 80
       analyse=True , if you want to plot Focus-prediction analysis plot
    '''
    print("Training started...")
    for epoch in range(epochs):
      epoch_loss = self.train_epoch(epoch,mini)
      
      self.train_loss.append(np.mean(epoch_loss))
        
      if np.mean(epoch_loss ) <= tol and epochs_or_loss_flag == False:
        break
    print("Finished Training")

  def predict(self,dataloader,print_accuracy=False):
    '''
    given dataloader predict for the network
    '''
    train_acc = 0
    true = []
    pred = []
    total = 0 
    self.net.eval()
    with torch.no_grad():
      for i, data in enumerate(dataloader):
        inputs,labels = data
        true.append(labels)
        inputs,labels = inputs.to(device), labels.to(device)
        outputs = self.net(inputs)
        _,predicted = torch.max(outputs.data,1)
        total += len(predicted) 
        pred.append(predicted.cpu().numpy())
      # print(predicted.detach().cpu().numpy())
        train_acc += sum(predicted.cpu().numpy() == labels.cpu().numpy())
    pred = np.concatenate(pred,axis=0)
    true = np.concatenate(true,axis=0)
    if print_accuracy == True:
      print("percentage accuracy: ",train_acc/total) 
    return true,pred

  def save_models(self):
    '''
       save models
    '''
    torch.save(self.net.state_dict(),"net.pt")
