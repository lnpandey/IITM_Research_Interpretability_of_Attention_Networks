Take MNIST and create training data x_i, z_i as follows. Let x_i be the MNIST images, and y_i be the MNIST labels. The training labels z_i are simply given as follows:

z_i = y_i if y_i is either 0 or 1
z_i is randomly 0 or 1 otherwise.

Train a network on this x_i, z_i data and predict labels on all test images. Check the accuracy on just the zero and one labelled test images. 

