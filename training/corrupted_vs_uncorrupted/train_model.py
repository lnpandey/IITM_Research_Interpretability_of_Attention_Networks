from corrupt_data import corrupt_data
import torch.nn as nn
import torch.optim as optim
import torch 
import numpy as np
device = 'cuda' if torch.cuda.is_available() else 'cpu'
def accuracy( a, b):
  length = a.shape
  correct = a==b
  return sum(correct)/length
  
def train(net,trainloader,criterion,optimizer,epoch):
  print('\nEpoch: %d' % epoch)
  net.train()
  train_loss = 0
  correct = 0
  total = 0
  for batch_idx, (inputs, targets) in enumerate(trainloader):
    inputs, targets = inputs.to(device), targets.to(device)
    optimizer.zero_grad()
    outputs = net(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()
    train_loss += loss.item()
    _, predicted = outputs.max(1)
    total += targets.size(0)
    correct += predicted.eq(targets).sum().item()
  print("train accuracy ", correct/total ,train_loss/391)
  return optimizer


def test(net,testloader,criterion,epoch):
  global best_acc
  net.eval()
  test_loss = 0
  correct = 0
  total = 0
  with torch.no_grad():
    for batch_idx, (inputs, targets) in enumerate(testloader):
      inputs, targets = inputs.to(device), targets.to(device)
      outputs = net(inputs)
      loss = criterion(outputs, targets)
      test_loss += loss.item()
      _, predicted = outputs.max(1)
      total += targets.size(0)
      correct += predicted.eq(targets).sum().item()
  print("test accuracy ", correct/total , test_loss/100)



def print_train(net,trainloader,criterion,mask):
  net.eval()
  train_loss = 0
  correct = 0
  total = 0
  true = []
  pred=[]
  out =[]
  with torch.no_grad():
    for batch_idx, (inputs, targets) in enumerate(trainloader):
      inputs, targets = inputs.to(device), targets.to(device)
      true.append(targets.cpu().numpy())
      outputs = net(inputs)
      out.append(outputs.cpu())
      loss = criterion(outputs, targets)
      train_loss += loss.item()
      _, predicted = outputs.max(1)
      pred.append(predicted.cpu().numpy())
      total += targets.size(0)
      correct += predicted.eq(targets).sum().item()
  print("train accuracy ", correct/total ,train_loss/391)
  true_targets = np.concatenate(true,axis=0)
  predicted_targets = np.concatenate(pred,axis =0)
  print("---"*20)
  print("Train accuracy on corrupt data",accuracy(true_targets[mask], 				predicted_targets[mask]))
  print("Train accuracy on un-corrupt data",accuracy(true_targets[~mask], 				predicted_targets[~mask]))
  print("Train accuracy on full data", accuracy(true_targets, predicted_targets))
  # print( sum (predicted_targets == np.argmax(out, axis =1)))
  l= np.where(mask ==True)
  p = np.where(mask == False)
  out = torch.cat(out, dim =0)
  print("Train cross entropy loss on corrupt data", criterion(out[l], torch.Tensor		(true_targets[l]).type(torch.LongTensor)))
  print("Train cross entropy loss on un-corrupt data",criterion(out[p], torch.Tensor		(true_targets[p]).type(torch.LongTensor)))
  print("Train cross entropy loss on full data",criterion(out, torch.Tensor				(true_targets).type(torch.LongTensor)))
  print("---"*20)


def print_test(net,testset, corrupt_per,criterion,mask1): 
  net.eval()
  test_loss = 0
  correct = 0
  total = 0
  true = []
  pred=[]
  out =[]
  with torch.no_grad():
    for batch_idx, (inputs, targets) in enumerate(testloader):
      inputs, targets = inputs.to(device), targets.to(device)
      true.append(targets.cpu().numpy())
      outputs = net(inputs)
      out.append(outputs.cpu())
      loss = criterion(outputs, targets)
      test_loss += loss.item()
      _, predicted = outputs.max(1)
      pred.append(predicted.cpu().numpy())
      total += targets.size(0)
      correct += predicted.eq(targets).sum().item()
  print("test accuracy ", correct/total ,test_loss/100)
  true_targets = np.concatenate(true,axis=0)
  predicted_targets = np.concatenate(pred,axis =0)
  print("---"*20)
  print("Test accuracy on corrupt data",accuracy(true_targets[mask1], predicted_targets[mask1]))
  print("Test accuracy on un-corrupt data",accuracy(true_targets[~mask1], predicted_targets[~mask1]))
  print("Test accuracy on full data", accuracy(true_targets, predicted_targets))

  l = np.where(mask1 ==True)
  p  = np.where(mask1 == False)
  out = torch.cat(out, dim =0)

  print("Test cross entropy loss on corrupt data", criterion(out[l], torch.Tensor(true_targets[l]).type(torch.LongTensor)))
  print("Test cross entropy loss on un-corrupt data",criterion(out[p], torch.Tensor(true_targets[p]).type(torch.LongTensor)))
  print("Test cross entropy loss on full data",criterion(out, torch.Tensor(true_targets).type(torch.LongTensor)))
  print("---"*20)
 



def training(net,trainloader,testloader,epochs,corrupt_per,train_mask,test_mask):
  lr = 0.01
  criterion = nn.CrossEntropyLoss()
  optimizer = optim.SGD(net.parameters(), lr, momentum=0.9, weight_decay=5e-4)
  for epoch in range(epochs):
    optimizer = train(net,trainloader,criterion,optimizer,epoch)
    test(net,testloader,criterion,epoch)
  if corrupt_per != 0:
    print_train(net,trainloader,criterion,train_mask)
    print_test( net,testloader,corrupt_per,criterion,test_mask)