
Take CIFAR10 and create training data x_i, z_i as follows. Let x_i be the CIFAR10 images, and y_i be the CIFAR10 labels. The training labels z_i are simply given as follows:

z_i = y_i if y_i is either 0 or 1 or 2, z_i is randomly 0 or 1 or 2 otherwise.

Train a network on this x_i, z_i data and predict labels on all test images. Check the accuracy on just the 0,1,2 labelled test images.

#### TABLE 1 : Break down of Training Data 

|true training data  | true 0 | true 1 | true 2 | Corrupted Training Data (ctd) | ctd 0 | ctd 1 | ctd 2| 
|--------------------|-----------------|--------|-------------------------------|-------|-------|------|
| 500                | 35000  | 19  |   | 
| 1000               | 35000  | 19  |   | 
| 2000               | 35000  | 21  |   | 
| 4000               | 35000  | 21  |   | 
| 6000               | 35000  | 20  |67 | 
| 8000               | 2733|2619|2648|35000  | 11714|11651|11635|  
| 10000              | 3331| 3354|3315|35000  |11696|11699|11605|
| 12000              | 4015|3905|4080|35000  |11680|11642|11678|
| 15000              | 5014|4977|5009|35000  | 11662|11718|11620|


#### TABLE 2 : Analysis on Training Data and Test Data

|true training data  | Corrupted Training Data | Total Training Data | Training Accuracy | Test Accuracy | Test Accuracy 0-1-2 | 
|--------------------| ----------------------- | ------------------- | ----------------- |---------------|---------------------|
| 500                | 35000                   | 35500               | 100               |               |   | 
| 1000               | 35000                   | 36000               | 100               |               |   | 
| 2000               | 35000                   | 37000               | 100               |               |   | 
| 4000               | 35000                   | 39000               | 100               |               |   | 
| 6000               | 35000                   | 41000               | 100               |               |   | 
| 8000               | 35000                   | 43000               | 100               | 20            | 67  |
| 10000              | 35000                   | 45000               | 100               | 21            | 71  |
| 12000              | 35000                   | 47000               | 100               | 22            | 73  | 
| 15000              | 35000                   | 50000               | 100               | 23            | 78  |
