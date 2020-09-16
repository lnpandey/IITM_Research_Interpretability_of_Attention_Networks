## Experiment Setup
Take for example one configuration ad protocol (CNN-6layer:CNN 6-layer: Random-random-both for simplicity) 

We can define 9 possible distributions on mosaic images based on train test CIFAR10 split:

FG images from (50k training, 10k testing, 60k entire CIFAR) and similarly BG images from (50k training, 10k testing, 60k entire CIFAR), for a total of 3*3 distributions.

Train on 30k mosaic samples from each of the 9 distributions, and test by drawing 10k samples from each of the nine distributions. So you would have trained 9 networks, and each network will be tested on 9 test distributions. Fill the test accuracies using 9x9 table, with  one row for each training dataset. Add a training accuracy at the end of each row as well for reference.

We want to see how well the network generalises to completely unseen CIFAR images.

### Table 1 : Data available in CIFAR10
| CIFAR10 | FG datapoints | BG datapoints |
|---------|--------------|--------------|
| Trainset | 15k |  35k |
| Testset | 3k |  7k |
| Combined | 18k |  42k |

### Table 2 : Datasets in Details
All datasets have 30k training mosaic images and 10k testing mosaic images.
| Dataset | FG used from | BG used from |
|---------|--------------|--------------|
| dataset 1 | Train 15k | Train 35k |
| dataset 2 | Train 15k | Test 7k |
| dataset 3 | Train 15k | Combined 42k |
| dataset 4 | Test 3k | Train 35k |
| dataset 5 | Test 3k | Test 7k |
| dataset 6 | Test 3k | Combined 42k |
| dataset 7 | Combined 18k | Train 35k |
| dataset 8 | Combined 18k | Test 7k |
| dataset 9 | Combined 18k | Combined 42k |

### Table 3 : Analysis of Accuracy on Training & Testing Data

|   | test on dataset1 | test on dataset2 | test on dataset3 | test on dataset4 | test on dataset5 | test on dataset6 | test on dataset7 | test on dataset8 | test on dataset9| Train Accuracy |
|----------|-----|-----|-----|-----|-----|-----|-----|-----|----|----|
| train on dataset1      | 93 | 89 | 93 | 83 | 79 | 82 | 92 | 87 | 90 | 99 |
| train on dataset2      | 82 | 96 | 84 | 73 | 86 | 74 | 80 | 95 | 83 | 99 |
| train on dataset3      | 93 | 92 | 92 | 81 | 80 | 81 | 91 | 90 | 91 | 98 |     
| train on dataset4      | 71 | 68 | 71 | 97 | 95 | 97 | 76 | 72 | 75 | 99 |
| train on dataset5      | 66 | 77 | 67 | 90 | 98 | 90 | 70 | 80 | 71 | 99 |
| train on dataset6      | 71 | 71 | 72 | 97 | 97 | 97 | 75 | 76 | 75 | 99 |
| train on dataset7      | 92 | 88 | 92 | 93 | 87 | 91 | 92 | 87 | 91 | 98 |
| train on dataset8      | 82 | 96 | 84 | 83 | 96 | 85 | 83 | 96 | 84 | 99 |
| train on dataset9      | 91 | 91 | 91 | 90 | 91 | 91 | 91 | 91 | 91 | 99 |
