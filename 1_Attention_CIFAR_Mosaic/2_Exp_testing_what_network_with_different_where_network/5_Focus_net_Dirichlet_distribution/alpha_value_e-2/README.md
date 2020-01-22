### Focus net output as Dirichlet Distribution


### Creation of datasets
- First, we have created 20000 Mosaic images.
- Labels of every Mosaic image is the class of foreground image present in that image.
- Dataset 'i' will contain 10000 image. Where each image is weighted average of 9 images present in Mosaic image. 
- Dataset 1 to Dataset 9 are made from same 10k Mosaic Images.
- Dataset 10 is made from 10000 to 20000 Mosaic Images which only contains the true Foreground Image present in every Mosaic Image.
- We have modeled the output of Focus network using the Dirichlet distribution with parameters alpha 
- Since we know exactly where the foreground image is present in the Mosaic image, therefore Dataset 'i', weight_of_foreground_image = a_i*alpha and weight_of_background_image = alpha. 
- Therefore Average Image in Dataset 'i' = w_fg * I_fg + sum_over_all_background_images( w_bg * I_bg ) 
- Where w_fg = weight_of_foreground_image, w_bg = weight_of_background_image, I_fg = Foreground_Image, I_bg = Background_Image
- w_fg = a_i*alpha, w_bg= alpha
- a_i can be calculated by a_i/ (a_i + 8*alpha) = i/9 where i in [1,8] where 'i' refer to 'i'th Dataset. 
- For Dataset 9, only Foreground Image is considered.

### Alpha value in Dirichlet Distribution:
>> alpha = 0.001 for this experiment

### Datasets:
- Parameter of distribution for Dataset 1 will be alpha for every image from mosaic.
- Parameter of distribution for Dataset 2 will be 16/7*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 3 will be 4*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 4 will be 32/5*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 5 will be 10*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 6 will be 16*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 7 will be 28*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 8 will be 64*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 9 will be 1*alpha for foreground image from mosaic and 0*alpha for backgroud image.
- Dataset 10 will contain true foreground images of Mosaic Images from 10000 to 20000.

### Experiment brief:
- Model ( what network) is trained on Dataset 'i', and Tested on all Dataset 'j', where j is not equal to i, j belongs to 1 to 9.
- We want to see, as the "Where" network perform better, i.e from Dataset 1 to Dataset 9 ( "Where" network learns to focus better),  how the "what" network behaves.
