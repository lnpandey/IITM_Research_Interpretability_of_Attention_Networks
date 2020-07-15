import numpy as np
def corrupt_data(trainset,corrupt_per):
  '''
   add label noise to trainset data based on given corruption percentage
   trainset: given training set
   corrupt_perc: percentage of labels needs to be corrupted
  '''
  if corrupt_per != 0:
    np.random.seed(1234)
    data_length = len(trainset.targets)
    mask = np.random.uniform(0,1,data_length) < corrupt_per
    a = np.array(trainset.targets)
    #print("true",a[mask])
		#print(np.sum(mask))
    a[mask] = np.random.randint(0,10,sum(mask))
    #print("randomized",a[mask])
    trainset.targets = list(a)
    return trainset,mask
  else:
    return trainset,[[]]