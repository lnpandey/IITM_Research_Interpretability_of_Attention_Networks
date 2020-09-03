import torch
from matplotlib import pyplot as plt
import numpy as np
from plots import plot_analysis,save_fig
from plots import focus_map,classification_map
import torch.optim as optim
import torch.nn as nn
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class train_mosaic_network():
  '''
     train mosaic data 
     elemental : True if data is 2 dimensional and we want to plot 2d data with network map
     pass x,y if True, else x,y takes default value None 
  '''
  def __init__(self,focus_net,classification_net,trainloader,testloader=None,elemental=False,x=None,y=None,lr=0.01):
    super(train_mosaic_network,self).__init__()
    self.focus_net = focus_net
    self.classification_net = classification_net
    self.trainloader = trainloader
    self.testloader = testloader
    self.lr = lr
    self.optimizer_focus = optim.SGD(focus_net.parameters(),lr = self.lr,momentum=0.9)
    self.optimizer_classification = optim.SGD(classification_net.parameters(),lr =self.lr, momentum=0.9)
    self.criterion = criterion = nn.CrossEntropyLoss() 
    self.train_loss = [] 
    self.train_analysis = []
    self.test_analysis = [] 
    self.elemental = elemental
    self.x = x
    self.y = y
  def train_epoch(self,epoch,analyse, train_loss, epochs_or_loss_flag,mini=80 ,train_focus=True,train_classify=True):
    '''
       trains a one epoch, if analyse =True the store the analysis data also
       mini: print loss after mini number of batches default value 80
       train focus: True if training focus
       train classification: True if training classification
    '''
    running_loss = 0
    cnt = 0
    ep_loss = []
    if self.elemental ==True:
      focus_map(self.focus_net,self.x,self.y)
      classification_map(self.classification_net,self.x,self.y)
    for i, data in  enumerate(self.trainloader):
      inputs , labels , fgrnd_idx = data
      inputs,labels = inputs.to(device),labels.to(device)
      if train_focus ==True and train_classify==True:  
        self.optimizer_focus.zero_grad()
        self.optimizer_classification.zero_grad()
      elif train_focus == False and train_classify ==True:
        self.optimizer_classification.zero_grad()
      elif train_focus == True and train_classify == False:
        self.optimizer_focus.zero_grad()
    
      avg_data , alphas = self.focus_net(inputs)
      outputs = self.classification_net(avg_data)
    
      _, predicted = torch.max(outputs.data, 1)
      loss = self.criterion(outputs, labels)
      loss.backward()
      if train_focus ==True and train_classify==True:  
        self.optimizer_focus.step()
        self.optimizer_classification.step()
      elif train_focus == False and train_classify ==True:
        self.optimizer_classification.step()
      elif train_focus == True and train_classify == False:
        self.optimizer_focus.step()
        
      #self.optimizer_focus.step()
      #self.optimizer_classification.step()
    
      running_loss += loss.item()
      #mini = 80
    
      if cnt % mini == mini-1:    # print every mini mini-batches
        print('[%d, %5d] loss: %.3f' %(epoch + 1, cnt + 1, running_loss / mini))
        ep_loss.append(running_loss/mini)
        running_loss = 0.0  
      cnt=cnt+1
   
    if analyse ==True:
      if epoch %5 ==4 or epoch == 0:
        tr_lbl,predicted,alphas,trn_findx = self.predict(self.trainloader) 
        train_analysis = self.analyse_data(alphas,tr_lbl,predicted,trn_findx)
        train_analysis.insert(0,epoch)        
        self.train_analysis.append(train_analysis)
        if self.testloader !=None:
          tst_lbl,tst_predicted,tst_alphas,tst_findx = self.predict(self.testloader)
          test_analysis = self.analyse_data(tst_alphas,tst_lbl,tst_predicted,tst_findx)
          test_analysis.insert(0,epoch)
          self.test_analysis.append(test_analysis)
        
        
    return ep_loss


  def training(self,epochs=100000,analyse=True,train_loss=0.001,mini=80, epochs_or_loss_flag = True,train_focus=True,train_classify=True):
    '''
       train given models for number of epochs 
       epochs=100000 by default
       train_loss=0.001 by default
       epochs_or_loss_flag = True , if training by epochs, if epochs_or_loss_flag = False, then train by training loss.
       mini : print loss after mini number of batches default value 80
       analyse=True , if you want to plot Focus-prediction analysis plot
       train_focus : True if training focus is training
       train_classification : True if classification is training
    '''
    print("Training started...")
    for epoch in range(epochs):
      epoch_loss = self.train_epoch(epoch,analyse,train_loss, epochs_or_loss_flag,mini,train_focus,train_classify)
      self.train_loss.append(np.mean(epoch_loss))
    print("Finished Training")

  def predict(self,dataloader,print_accuracy=False):
    '''
    given dataloader predict for the network
    '''
    train_acc = 0
    true = []
    pred = []
    alpha = []
    findx = []
    total = 0 
    with torch.no_grad():
      for i, data in enumerate(dataloader):
        inputs,labels,findices = data
        findx.append(findices)
        true.append(labels)
        inputs,labels = inputs.to(device), labels.to(device)
    
        avg_data,alphas = self.focus_net(inputs)
        alpha.append(alphas.cpu().numpy())
        
        outputs = self.classification_net(avg_data)
        _,predicted = torch.max(outputs.data,1)
        total += len(predicted) 
        pred.append(predicted.cpu().numpy())
      # print(predicted.detach().cpu().numpy())
        train_acc += sum(predicted.cpu().numpy() == labels.cpu().numpy())
    findx = np.concatenate(findx,axis=0)
    pred = np.concatenate(pred,axis=0)
    true = np.concatenate(true,axis=0)
    alpha = np.concatenate(alpha,axis=0)
    if print_accuracy == True:
      print("percentage accuracy: ",train_acc/total) 
    return true,pred,alpha,findx

  def save_models(self):
    '''
       save models
    '''
    torch.save(self.focus_net.state_dict(),"focus_net.pt")
    torch.save(self.classification_net.state_dict(),"classification_net.pt")

  def analyse_data(self,alphas,lbls,predicted,f_idx):
    '''
       analyse data is created here
    '''
    batch = len(predicted)
    amth,alth,ftpt,ffpt,ftpf,ffpf = 0,0,0,0,0,0
    for j in range (batch):
      focus = np.argmax(alphas[j])
      if(alphas[j][focus] >= 0.5):
        amth +=1
      else:
        alth +=1
      if(focus == f_idx[j] and predicted[j] == lbls[j]):
        ftpt += 1
      elif(focus != f_idx[j] and predicted[j] == lbls[j]):
        ffpt +=1
      elif(focus == f_idx[j] and predicted[j] != lbls[j]):
        ftpf +=1
      elif(focus != f_idx[j] and predicted[j] != lbls[j]):
        ffpf +=1
    return [ftpt,ffpt,ftpf,ffpf,amth,alth]

    
    