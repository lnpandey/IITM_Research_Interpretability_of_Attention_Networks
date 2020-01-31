
Take CIFAR10 and create training data x_i, z_i as follows. Let x_i be the CIFAR10 images, and y_i be the CIFAR10 labels. The training labels z_i are simply given as follows:

z_i = y_i if y_i is either 0 or 1 or 2, z_i is randomly 0 or 1 or 2 otherwise.

Train a network on this x_i, z_i data and predict labels on all test images. Check the accuracy on just the 0,1,2 labelled test images.

#### TABLE 1 : Break down of Training Data 

|true training data  | true 0 | true 1 | true 2 | Corrupted Training Data (ctd) | ctd 0 | ctd 1 | ctd 2| 
|--------------------|--------|--------|--------|-------------------------------|-------|-------|------|
| 1000               | 341    |325     | 334     | 35000                        | 11659 | 11732 | 11609|
| 2000               | 653    | 691    | 656     | 35000                        | 11669 | 11615 | 11716|
| 4000               | 1388   | 1300   | 1312    | 35000                        | 11620 | 11723 | 11657| 
| 6000               | 1973   | 2031   | 1996    | 35000                        | 11700 | 11678 | 11622|
| 8000               | 2733   | 2619   | 2648    | 35000                        | 11714 | 11651 | 11635|  
| 10000              | 3331   | 3354   | 3315    | 35000                        | 11696 | 11699 | 11605|
| 12000              | 4015   | 3905   | 4080    | 35000                        | 11680 | 11642 | 11678|
| 15000              | 5014   | 4977   | 5009    | 35000                        | 11662 | 11718 | 11620|

- ctd 0 means number of data points (belonging from any class other than 0,1,2) which are labeled as zero.
- ctd 1 means number of data points (belonging from any class other than 0,1,2) which are labeled as one.
- ctd 2 means number of data points (belonging from any class other than 0,1,2) which are labeled as two.

#### TABLE 2 : Analysis on Training Data and Test Data On Complex Model


|true training data  | Corrupted Training Data | Total Training Data | Training Accuracy | Test Accuracy | Test Accuracy 0-1-2 | 
|--------------------| ----------------------- | ------------------- | ----------------- |---------------|---------------------|
| 1000               | 35000                   | 36000               | 100               | 11            | 38                  | 
| 2000               | 35000                   | 37000               | 100               | 14            | 49                  | 
| 4000               | 35000                   | 39000               | 100               | 16            | 56                  | 
| 6000               | 35000                   | 41000               | 100               | 19            | 63                  | 
| 8000               | 35000                   | 43000               | 100               | 20            | 67                  |
| 10000              | 35000                   | 45000               | 100               | 21            | 71                  |
| 12000              | 35000                   | 47000               | 100               | 22            | 73                  | 
| 15000              | 35000                   | 50000               | 100               | 23            | 78                  |

#### TABLE 3 : Analysis on Training Data and Test Data On Simple Model


|true training data  | Corrupted Training Data | Total Training Data | Training Accuracy | Test Accuracy | Test Accuracy 0-1-2 | 
|--------------------| ----------------------- | ------------------- | ----------------- |---------------|---------------------|
| 1000               | 35000                   | 36000               | 97              | 11            | 38                  | 
| 2000               | 35000                   | 37000               | 98               | 12            | 40                  | 
| 4000               | 35000                   | 39000               | 99               | 14            | 47                  | 
| 6000               | 35000                   | 41000               | 99               | 16            | 55                  | 
| 8000               | 35000                   | 43000               | 99               | 17            | 57                  |
| 10000              | 35000                   | 45000               | 99               | 17            | 58                  |
| 12000              | 35000                   | 47000               | 100               | 19            | 64                  | 
| 15000              | 35000                   | 50000               | 99               | 19            | 66                  |

#### TABLE 4 : Analysis on True Training Data and Test Data On Complex Model


|true training data  | Corrupted Training Data | Total Training Data | Training Accuracy | Test Accuracy | Test Accuracy 0-1-2 | 
|--------------------| ----------------------- | ------------------- | ----------------- |---------------|---------------------|
| 1000               | 0                   | 1000               | 100               | 24            | 80                  | 
| 2000               | 0                   | 2000               | 100               | 24            | 82                  | 
| 4000               | 0                   | 4000               | 100               | 25            | 85                  | 
| 6000               | 0                   | 6000               | 100               | 25            | 86                  | 
| 8000               | 0                   | 8000               | 100               | 26            | 88                  |
| 10000              | 0                   | 10000               | 99               | 26            | 89                  |
| 12000              | 0                   | 12000               | 100               | 26            | 88                  | 
| 15000              | 0                   | 15000               | 100               | 26            | 88                  |


##### Weights Link : 
> Complex Model: https://drive.google.com/open?id=1wI02qlAv8T2tFa8Qh0qUaRjrxi5vSBBd

> Simple Model:  https://drive.google.com/open?id=18SLDU4nYw5Rd9ptEXWzNIgfaKdwyROca

#### Architecture for Models
To be done
