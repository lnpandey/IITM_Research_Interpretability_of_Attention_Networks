col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]
col7=[]
col8=[]
col9=[]
col10=[]
col11=[]
col12=[]
col13=[]


def train_epoch(trainloader,testloader,focus_net,classification_net,optimizer,criterion,epoch,analyse=True):
  optimizer_focus = optimizer[0]
  optimizer_classification = optimizer[1]
  running_loss = 0
  cnt = 0
  for i, data in  enumerate(trainloader):
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
      ep_loss.append(running_loss/mini)
      running_loss = 0.0  
    cnt=cnt+1
   
  if analyse ==True:
    if epoch %5 ==0:
      predicted,alphas = predict(trainloader,focus_net,classification_net) 
      test_predicted,test_alphas = predict(testloader,focus_net,classification_net)
      ftpt,ffpt,ftpf,ffpf,amth,alth = analyse_data(alphas,predicted)
      tftpt,tffpt,tftpf,tffpf,tamth,talth = analyse_data(test_alphas,test_predicted)
      col1.append(epoch)
      col2.append(amth)
      col3.append(alth)
      col4.append(ftpt)
      col5.append(ffpt)
      col6.append(ftpf)
      col7.append(ffpf)
      col8.append(argmax_more_than_half)
      col9.append(argmax_less_than_half)
      col10.append(focus_true_pred_true)
      col11.append(focus_false_pred_true)
      col12.append(focus_true_pred_false)
      col13.append(focus_false_pred_false)
           
  optimizer = [optimizer_focus,optimizer_classification]
  return optimizer,ep_loss


def training(trainloader,testloader,focus_net,classification_net,optimizer,criterion,epochs):
  print("Training started...")
  train_loss = []
  for epoch in range(epochs):
    optimizer,epoch_loss = train_epoch(trainloader,testloader,focus_net,classification_net,optimizer,criterion,epoch)
    train_loss.append(np.mean(epoch_loss))
  print("Finished Training")

def predict(dataloader,focus_net,classification_net,print_accuracy=False):
  train_acc = 0
  for i, data in enumerate(dataloader):
    inputs,labels,_ = data
    inputs,labels = inputs.to(device), labels.to(device)
    
    avg_data,alphas = focus_net(inputs)
    outputs = classification_net(avg_data)
    _,predicted = torch.max(outputs.data,1)
    # print(predicted.detach().cpu().numpy())
    train_acc += sum(predicted.cpu().numpy() == labels.cpu().numpy())
  if print_accuracy == True:
    print("percentage train accuracy: ",train_acc/300) 
  return predicted,alphas

def save_models(focus_net,classification_net):
  torch.save(focus_net.state_dict(),"focus_net_at_zero.pt")
  torch.save(classification_net.state_dict(),"classification_net_at_zero.pt")

def analyse_data(alphas,predicted):
  batch = len(predicted)
  for j in range (batch):
    focus = torch.argmax(alphas[j])
    if(alphas[j][focus] >= 0.5):
      argmax_more_than_half +=1
    else:
      argmax_less_than_half +=1

    if(focus == fore_idx[j] and predicted[j] == labels[j]):
      focus_true_pred_true += 1

    elif(focus != fore_idx[j] and predicted[j] == labels[j]):
      focus_false_pred_true +=1

    elif(focus == fore_idx[j] and predicted[j] != labels[j]):
      focus_true_pred_false +=1

    elif(focus != fore_idx[j] and predicted[j] != labels[j]):
      focus_false_pred_false +=1
  return focus_true_pred_true,focus_false_pred_true,focus_true_pred_false,focus_false_pred_false,argmax_more_than_half,argmax_less_than_half

    
    