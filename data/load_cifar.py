import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision import datasets
def cifarset():
	'''
        	returns trainset and testset for cifar10 dataset
	'''
	
	print('==> Preparing data..')
	transform_train = transforms.Compose([
     		transforms.RandomCrop(32, padding=4),
     		transforms.RandomHorizontalFlip(),
     		transforms.ToTensor(),
     		transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))])

	transform_test = transforms.Compose([
     		transforms.ToTensor(),
     		transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
  		])

	trainset = datasets.CIFAR10(root='./data', train=True, download=True, 				transform=transform_train)
	testset = datasets.CIFAR10(root='./data', train=False, download=True, 				transform=transform_test)
	return trainset,testset
def load_data(trainset,testset,train_batch,test_batch,shuffle=True):
	'''
		returns trainloader and testloader object
	'''
	testloader = DataLoader(testset, batch_size=test_batch, shuffle=shuffle,num_workers=2)
	trainloader = DataLoader(trainset, batch_size=train_batch,shuffle=shuffle,num_workers=2)
	return trainloader,testloader
	