
Take CIFAR10 and create training data x_i, z_i as follows. Let x_i be the CIFAR10 images, and y_i be the CIFAR10 labels. The training labels z_i are simply given as follows:

z_i = y_i if y_i is either 0 or 1 or 2, z_i is randomly 0 or 1 or 2 otherwise.

Train a network on this x_i, z_i data and predict labels on all test images. Check the accuracy on just the 0,1,2 labelled test images.
