import numpy as np
import torch 
import torchvision
from torch.utils.data import DataLoader,Dataset


class Mosaic_Data():
  '''
     
  '''
  def __init__(self,dataloader,total,train_desired,test_desired,fg1=0,fg2=1,fg3=2):
    super(Mosaic_Data,self).__init__()
    self.dataloader = dataloader
    self.fg1 = fg1 
    self.fg2 = fg2
    self.fg3 = fg3
    self.total = total
    self.train_desired =train_desired
    self.test_desired = test_desired
    self.data = self.split_foreground_background(self.total)
    self.train_images,self.train_label,self.train_idx = self.mosaic_data(self.train_desired)
    self.test_images,self.test_label,self.test_idx    = self.mosaic_data(self.test_desired) 
  
  
  def split_foreground_background(self,total):
    '''
        input: Trainloader
        output: returns foreground and background instances with labels
    '''
    dataiter = iter(self.dataloader)
    background_data=[]
    background_label=[]
    foreground_data=[]
    foreground_label=[]
    batch_size=10
    iterator = total//batch_size
    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    foreground_classes = {classes[self.fg1], classes[self.fg2], classes[self.fg3]}
    all_classes = {'plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck'}
    background_classes = all_classes - foreground_classes
    # background_classes = {'plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog'} if fg1 = 7, fg2 = 8, fg3 = 9
    for i in range(iterator):
      images, labels = dataiter.next()
      for j in range(batch_size):
        if(classes[labels[j]] in background_classes):
          img = images[j].tolist()
          background_data.append(img)
          background_label.append(labels[j])
        else:
          img = images[j].tolist()
          foreground_data.append(img)
          foreground_label.append(labels[j])         
    foreground_data = torch.tensor(foreground_data)
    foreground_label = torch.tensor(foreground_label)
    background_data = torch.tensor(background_data)
    background_label = torch.tensor(background_label)
    return foreground_data,foreground_label,background_data,background_label


  def create_mosaic_img(self, bg_idx,fg_idx,fg): 
    """
    bg_idx : list of indexes of background_data[] to be used as background images in mosaic
    fg_idx : index of image to be used as foreground image from foreground data
    fg : at what position/index foreground image has to be stored out of 0-8
    """
    #foreground_data,foreground_label,background_data,background_label = data
    image_list=[]
    j=0
    for i in range(9):
      if i != fg:
        image_list.append(self.data[2][bg_idx[j]].type("torch.DoubleTensor"))
        j+=1
      else: 
        image_list.append(self.data[0][fg_idx].type("torch.DoubleTensor"))
        label = self.data[1][fg_idx]- self.fg1 # minus fg1 because our fore ground classes are fg1=0,fg2=1,fg3=2 but we have to store it as 0,1,2
    #image_list = np.concatenate(image_list ,axis=0)
    image_list = torch.stack(image_list) 
    return image_list,label



  def mosaic_data(self,desired_num):
   
    #print(data[0].shape)
    #desired_num = 30000
    mosaic_list_of_images =[]      # list of mosaic images, each mosaic image is saved as list of 9 images
    fore_idx =[]                   # list of indexes at which foreground image is present in a mosaic image i.e from 0 to 9               
    mosaic_label=[]                # label of mosaic image = foreground class present in that mosaic
    for i in range(desired_num):
      bg_idx = np.random.randint(0,self.data[2].shape[0],8)
      fg_idx = np.random.randint(0,self.data[0].shape[0])
      fg = np.random.randint(0,9)
      fore_idx.append(fg)
      image_list,label = self.create_mosaic_img(bg_idx,fg_idx,fg)
      mosaic_list_of_images.append(image_list)
      mosaic_label.append(label)
    return mosaic_list_of_images,mosaic_label,fore_idx



class MosaicDataset(Dataset):
  """MosaicDataset dataset."""
  
  def __init__(self, mosaic_list_of_images, mosaic_label, fore_idx):
    """
     Args:
        csv_file (string): Path to the csv file with annotations.
        root_dir (string): Directory with all the images.
        transform (callable, optional): Optional transform to be applied
            on a sample.
    """
    self.mosaic = mosaic_list_of_images
    self.label = mosaic_label
    self.fore_idx = fore_idx

  def __len__(self):
    return len(self.label)

  def __getitem__(self, idx):
    return self.mosaic[idx] , self.label[idx], self.fore_idx[idx]







