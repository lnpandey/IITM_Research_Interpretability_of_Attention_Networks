### Creation of datasets
- First, we have created 20000 Mosaic images.
- Labels of every Mosaic image is the class of foreground image present in that image.
- Dataset 'i' will contain 10000 image. Where each image is weighted average of 9 images present in Mosaic image. 
- Dataset 1 to Dataset 9 are made from same 10k Mosaic Images.
- Dataset 10 is made from 10000 to 20000 Mosaic Images which only contains the true Foreground Image present in every Mosaic Image.
- Since we know exactly where the foreground image is present in the Mosaic image, there fore Dataset 'i', weight_of_foreground_image = i/9 and weight_of_background_image = (9-i)/8*9. 
- Therefore Average Image in Dataset 'i' = w_fg * I_fg + sum_over_all_background_images( w_bg * I_bg ) 
- Where w_fg = weight_of_foreground_image, w_bg = weight_of_background_image, I_fg = Foreground_Image, I_bg = Background_Image
- w_fg = i / 9 , w_bg= (9-i)/8*9

### Datasets:
- Dataset 1 will contain images which are 1/9 th of every image from mosaic.
- Dataset 2 will contain images which are 2/9 th of I_fg and 7/8*9 th of every I_bg from mosaic.
- Dataset 3 will contain images which are 3/9 th of I_fg and 6/8*9 th of every I_bg from mosaic.
- Dataset 4 will contain images which are 4/9 th of I_fg and 5/8*9 th of every I_bg from mosaic.
- Dataset 5 will contain images which are 5/9 th of I_fg and 4/8*9 th of every I_bg from mosaic.
- Dataset 6 will contain images which are 6/9 th of I_fg and 3/8*9 th of every I_bg from mosaic.
- Dataset 7 will contain images which are 7/9 th of I_fg and 2/8*9 th of every I_bg from mosaic.
- Dataset 8 will contain images which are 8/9 th of I_fg and 1/8*9 th of every I_bg from mosaic.
- Dataset 9 will contain images which are 9/9 th of I_fg and 0 th of every I_bg from mosaic.
- Dataset 10 will contain true foreground images of Mosaic Images from 10000 to 20000.

### Experiment brief:
- Model ( what network) is trained on Dataset 'i', and Tested on all Dataset 'j', where j is not equal to i, j belongs to 1 to 9.
- We want to see, as the "Where" network perform better, i.e from Dataset 1 to Dataset 9 ( "Where" network learns to focus better),  how the "what" network behaves.

### Architecture of the Model
```python
class Module2(nn.Module):
    def __init__(self):
        super(Module2, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
        self.fc4 = nn.Linear(10,3)

    def forward(self,z):  #z batch of list of 9 images
        y1 = self.pool(F.relu(self.conv1(z)))
        y1 = self.pool(F.relu(self.conv2(y1)))
        y1 = y1.view(-1, 16 * 5 * 5)
        y1 = F.relu(self.fc1(y1))
        y1 = F.relu(self.fc2(y1))
        y1 = F.relu(self.fc3(y1))
        y1 = self.fc4(y1)
        return y1
```

#### Weights and Datasets of Experiment can be found here :
>https://drive.google.com/open?id=1UR_EXMdGCx5Ee70ASQkTQJIH00IiyMyL


### Analysis of Accuracy on Training & Testing Data

| train\ test  | test on dataset 1 | test on dataset 2 | test on dataset 3 | test on dataset 4 | test on dataset 5 | test on dataset 6 | test on dataset 7 | test on dataset 8 | test on dataset 9| test on dataset 10 |
|----------|-----|-----|-----|-----|-----|-----|-----|-----|----|----|
| train on dataset 1      | 52 | 64 | 68 | 68 | 67 | 65 | 63 | 61 | 60 | 60 |
| train on dataset 2      | 65 | 100 | 92 | 83 | 76 | 73 | 69 | 67 | 65 | 63 |
| train on dataset 3      | 47 | 78 | 100 | 97 | 91 | 86 | 82 | 79 | 77 | 73 |     
| train on dataset 4      | 41 | 63 | 90 | 100 | 99 | 96 | 92 | 89 | 87 | 82 |
| train on dataset 5      | 39 | 55 | 78 | 96 | 100 | 99 | 97 | 94 | 91 | 85 |
| train on dataset 6      | 37 | 49 | 71 | 90 | 99 | 99 | 99 | 97 | 94 | 87 |
| train on dataset 7      | 35 | 41 | 57 | 77 | 91 | 99 | 100 | 99 | 98 | 91 |
| train on dataset 8      | 34 | 37 | 48 | 67 | 83 | 94 | 99 | 100 | 99 | 92 |
| train on dataset 9      | 35 | 37 | 46 | 61 | 76 | 89 | 97 | 99 | 100 | 92 |


### Plot of Training loss for all the Datasets :
 ![](training_loss_10k_cnn.png)
