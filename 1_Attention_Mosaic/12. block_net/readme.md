##Experiment Setup
Train a block network such that input shape = 27,32,32 (Mosaic images reshaed at input channel dimension) and output is vector of length 3 ( 3-class classification).

|  Model used | Train Accuracy |  Test Accuracy | CE Loss plot vs Epochs for training and testing | 
|  ------------------ | --------------------------- |  ----------- | --------------------------- | 
| CNN 6 Layer | 99 | 42 | <img src= ./plots_and_images/loss_cnn.JPG width="250">  |
| CNN 6 Layer | 100 | 39 | <img src= ./plots_and_images/loss_mini.JPG width="250">  | 
| CNN 6 Layer | 100 | 39.13 | <img src= ./plots_and_images/loss_resnet18.JPG width="250">  | 
