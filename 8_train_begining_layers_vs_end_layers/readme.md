## Experiment Setup:
Train CNN-x-layer on CIFAR 10 classification and MNIST 10 class classification. Now perform the following experiments on both CIFAR and MNIST:
1. Freeze first x/2 layers and train rest x/2 layers for 10 class classification. (Freeze means load the trained weights and requires grad = False)
2. Train first x/2 layers and freeze rest x/2 layers for 10 class classification. (Freeze means load the trained weights and requires grad = False)

## Table 1: MNIST 10 Class Classification
| Model used | Epoch | Train Accuracy | Test Accuracy |
|------------|-------|----------------|---------------|
|CNN 6 layer | 10 | 99 | 99 |
|CNN 8 Layer | 8 | 99 | 99 |
|CNN 10 Layer | 10 | 99 | 99 |

## Table 2 : Experiments performed using pretrained weights from Table 1
| Model used | Loaded trained weights in | random init of weights in | Epoch | Train Accuracy | Test Accuracy |
|------------|---------------------------|---------------------------|-------|----------------|---------------|
|CNN 6 layer | first 3 layers | last 3 layers | 5 | 99 | 99 |
|CNN 6 layer | last 3 layers | first 3 layers | 7 | 99 | 99 |
|CNN 8 layer | first 4 layers | last 4 layers | 3 | 99 | 99 |
|CNN 8 layer | last 4 layers | first 4 layers | 6 | 99 | 99 |
|CNN 10 layer | first 5 layers | last 5 layers | 3 | 99 | 99 |
|CNN 10 layer | last 5 layers | first 5 layers | 8 | 99 | 99 |

## Table 3: CIFAR 10 Class Classification
| Model used | Epoch | Train Accuracy | Test Accuracy |
|------------|-------|----------------|---------------|
|CNN 6 layer | 104 | 99 | 81 |
|CNN 8 Layer | 85 | 99 | 79 |
|CNN 10 Layer | 98 | 99 | 79 |

## Table 4 : Experiments performed using pretrained weights from Table 3
| Model used | Loaded trained weights in | random init of weights in | Epoch | Train Accuracy | Test Accuracy |
|------------|---------------------------|---------------------------|-------|----------------|---------------|
|CNN 6 layer | first 3 layers | last 3 layers | 68 | 99 | 80 |
|CNN 6 layer | last 3 layers | first 3 layers | 258 | 99 | 80 |
|CNN 8 layer | first 4 layers | last 4 layers | 55 | 99 | 79 |
|CNN 8 layer | last 4 layers | first 4 layers | 206 | 99 | 77 |
|CNN 10 layer | first 5 layers | last 5 layers | 57 | 99 | 80 |
|CNN 10 layer | last 5 layers | first 5 layers | 198 | 99 | 77 |
