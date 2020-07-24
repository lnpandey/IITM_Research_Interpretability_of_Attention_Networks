import torch
from matplotlib import pyplot as plt
import numpy as np
from plots import plot_analysis,save_fig
import torch.optim as optim
import torch.nn as nn
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class train_mosaic_network():
  def __init__(self,focus_net,classification_net,trainloader,testloader):
    super(train_mosaic_network,self).__init__()
    self.focus_net = focus_net
    self.classification_net = classification_net
    self.trainloader = trainloader
    self.testloader = testloader
    self.optimizer_focus = optim.SGD(focus_net.parameters(),lr = 0.01,momentum=0.9)
    self.optimizer_classification = optim.SGD(classification_net.parameters(),lr =0.01, momentum=0.9)
    self.criterion = criterion = nn.CrossEntropyLoss() 
    self.train_loss = [] 
    self.train_analysis = []
    self.test_analysis = [] 
  def train_epoch(self,epoch,analyse = True):
    running_loss = 0
    cnt = 0
    ep_loss = []
    for i, data in  enumerate(self.trainloader):
      inputs , labels , fgrnd_idx = data
      inputs,labels = inputs.to(device),labels.to(device)
  
      self.optimizer_focus.zero_grad()
      self.optimizer_classification.zero_grad()
    
      avg_data , alphas = self.focus_net(inputs)
      outputs = self.classification_net(avg_data)
    
      _, predicted = torch.max(outputs.data, 1)
      loss = self.criterion(outputs, labels)
      loss.backward()
    
      self.optimizer_focus.step()
      self.optimizer_classification.step()
    
      running_loss += loss.item()
      mini = 80
    
      if cnt % mini == mini-1:    # print every mini mini-batches
        print('[%d, %5d] loss: %.3f' %(epoch + 1, cnt + 1, running_loss / mini))
        ep_loss.append(running_loss/mini)
        running_loss = 0.0  
      cnt=cnt+1
   
    if analyse ==True:
      if epoch %5 ==0:
        tr_lbl,predicted,alphas,trn_findx = self.predict(self.trainloader) 
        tst_lbl,tst_predicted,tst_alphas,tst_findx = self.predict(self.testloader)
        train_analysis = self.analyse_data(alphas,tr_lbl,predicted,trn_findx)
        test_analysis = self.analyse_data(tst_alphas,tst_lbl,tst_predicted,tst_findx)
        train_analysis.insert(0,epoch)
        test_analysis.insert(0,epoch)
        self.train_analysis.append(train_analysis)
        self.test_analysis.append(test_analysis)
    return ep_loss


  def training(self,epochs):
    print("Training started...")
    for epoch in range(epochs):
      epoch_loss = self.train_epoch(epoch)
      self.train_loss.append(np.mean(epoch_loss))
    print("Finished Training")

  def predict(self,dataloader,print_accuracy=False):
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
      print("percentage train accuracy: ",train_acc/total) 
    return true,pred,alpha,findx

  def save_models(self):
    torch.save(self.focus_net.state_dict(),"focus_net.pt")
    torch.save(self.classification_net.state_dict(),"classification_net.pt")

  def analyse_data(self,alphas,lbls,predicted,f_idx):
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

    
    