import numpy as np

def fg_bg_data(labels,fg_labels):
  ''' 
     given cifar data convert into fg and background data
     inputs : original cifar labels as list, foreground labels as list
     returns cifar labels as binary labels with foreground data as class 0 and background      data as class 1 
  '''  
  labels = np.array(labels)
  fg_indices = np.logical_or(np.logical_or(labels==fg_labels[0],labels==fg_labels[1]),labels==fg_labels[2]) 
  bg_indices = np.logical_not(train_indices_fg)
  labels[fg_indices] = 0 
  labels[bg_indices] = 1
  return list(labels)

def fg_data(data,labels,fg_labels):
  '''
     given cifar data convert into foreground data
     inputs : original cifar labels as list, foreground labels as list
     returns cifar labels as binary labels with foreground data as class 0 class 1 and so on
  '''
  labels = np.array(labels)
  fg_indices = np.logical_or(np.logical_or(labels==fg_labels[0],labels==fg_labels[1]),labels==fg_labels[2]) 
  cls_max = np.max(fg_labels)
  labels = labels[fg_indices] - cls_max
  return data[fg_indices],labels