Take MNIST and create training data x_i, z_i as follows. Let x_i be the MNIST images, and y_i be the MNIST labels. The training labels z_i are simply given as follows:

z_i = y_i if y_i is either 0 or 1 z_i is randomly 0 or 1 otherwise.

Train a network on this x_i, z_i data and predict labels on all test images. Check the accuracy on just the zero and one labelled test images.

#### TABLE 1 : Analysis on Training Data and Test Data On Simple Model


|true training data  | Corrupted Training Data | Total Training Data | Training Accuracy | Test Accuracy | Test Accuracy 0-1 | 
|--------------------| ----------------------- | ------------------- | ----------------- |---------------|---------------------|
| 100               | 47335                   | 47435               | 100               | 13            | 61                  | 
| 500               | 47335                   | 47835               | 100               | 16            | 80                  | 
| 1000               | 47335                   | 48335               | 100               | 17            | 83                  | 
| 2000               | 47335                   | 49335               | 100               | 19            | 92                  | 
| 4000               | 47335                   | 51335               | 100               | 20            | 95                  |
| 6000              | 47335                   | 53335               | 100               | 20            | 96                 |
| 8000              | 47335                   | 55335               | 100               | 20            | 96                  | 
| 12665              | 47335                   | 60000               | 100               | 20            | 98                  |

#### TABLE 2 : Analysis on Training Data and Test Data On Complex Model


|true training data  | Corrupted Training Data | Total Training Data | Training Accuracy | Test Accuracy | Test Accuracy 0-1 | 
|--------------------| ----------------------- | ------------------- | ----------------- |---------------|---------------------|
| 100               | 47335                   | 47435               | 100               | 14            | 69                  | 
| 500               | 47335                   | 47835               | 100               | 19            | 90                  | 
| 1000               | 47335                   | 48335               | 100               | 19            | 92                  | 
| 2000               | 47335                   | 49335               | 100               | 20            | 95                  | 
| 4000               | 47335                   | 51335               | 100               | 20            | 97                  |
| 6000              | 47335                   | 53335               | 100               | 20            | 97                |
| 8000              | 47335                   | 55335               | 100               | 20            | 98                  | 
| 12665              | 47335                   | 60000               | 100               | 20            | 99                  |


#### TABLE 3 : Analysis on Training Data and Test Data On Simple Model with ZERO Corruption

|true training data  | Corrupted Training Data | Total Training Data | Training Accuracy | Test Accuracy | Test Accuracy 0-1 | 
|--------------------| ----------------------- | ------------------- | ----------------- |---------------|---------------------|
| 100              | 0        | 100               | 100               | 20            | 98                  | 
| 500              | 0        | 500               | 100               | 21            | 99                  | 
| 1000             | 0        | 1000              | 100               | 21            | 99                  | 
| 2000             | 0        | 2000              | 100               | 21            | 99                  | 
| 4000             | 0        | 4000              | 100               | 21            | 99                  |
| 6000             | 0        | 6000              | 100               | 21            | 99                  |
| 8000             | 0        | 8000              | 100               | 21            | 99                  | 
| 12665            | 0        | 12665             | 100               | 21            | 99                  |

#### TABLE 4 : Analysis on Training Data and Test Data On Complex Model with ZERO Corruption

|true training data  | Corrupted Training Data | Total Training Data | Training Accuracy | Test Accuracy | Test Accuracy 0-1 | 
|--------------------| ----------------------- | ------------------- | ----------------- |---------------|---------------------|
| 100              | 0        | 100               | 100               | 19            | 93                  | 
| 500              | 0        | 500               | 100               | 21            | 99                  | 
| 1000             | 0        | 1000              | 100               | 21            | 99                  | 
| 2000             | 0        | 2000              | 100               | 21            | 99                  | 
| 4000             | 0        | 4000              | 100               | 21            | 99                  |
| 6000             | 0        | 6000              | 100               | 21            | 99                  |
| 8000             | 0        | 8000              | 100               | 21            | 99                  | 
| 12665            | 0        | 12665             | 100               | 21            | 99                  |

##### Weights Link : 
> Complex Model: https://drive.google.com/open?id=1H1yn0LLxcIq56CyQbxQ4VRRymRlNCJy6

> Simple Model:  https://drive.google.com/open?id=1MoGeKZO3G5uHsYlo6ufDmiZXqUXUUes8

> Complex Model with zero corruption: https://drive.google.com/open?id=1S0UL_QFPRy8LFLDnyfIN97UIZEN0i6_C

> Simple Model with zero corruption:  https://drive.google.com/open?id=1Gtf00xIUWqHf31ynQJluCJFYD29_KE6y


#### Architecture for Models
Simple Model : 3 Inception Module

Complex Model : Mini-Inception Net ( 8 Inception Modules )
