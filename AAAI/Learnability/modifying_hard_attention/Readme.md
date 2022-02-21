WILL UPLOAD NOTEBOOKS FROM KAGGLE
#### Hypothesis under which the focus optimiisation objective is
#### \sum_i w_i \sum_j \alpha_{ij} l_{ij}

#### Classification objective is always
#### \sum_i \sum_j \alpha_{ij} l_{ij}

#### Option 1 for w : w_i = e^{-\min_{j} l_{ij}}

#### w_i will be large when \min_{j} l_{ij} is small.
#### Assumption: whenver min_j l_{ij} is very small, it is because the FG loss is small.
#### Under abaove assumption w_i will be large for all mosaic patches where FG loss is smallest.
#### Hence encouraging the focus net to give larger values to FG for those mosaic images.
#### Example situation :
#### Two patches: [0.1, 0.5, 0.5, 0.5,0.5] ,  [0.9, 0.5, 0.9, 0.9, 0.9]
#### Optimising focus net. If no w_i : Focus net is  incentivised equally to increase \alpha_11 and \alpha_22
#### If w_i : Then Focus net is  incentivised more to increase \alpha_11 than \alpha_22

#### Another example two patches: [0.1, 0.5, 0.5, 0.5,0.5] ,  [0.5, 0.1, 0.5, 0.5, 0.5]
#### Optimising focus net. If no w_i : Focus net is  incentivised equally to increase \alpha_11 and \alpha_22
#### With or without w_i : Then Focus net is  incentivised equally to increase \alpha_11 than \alpha_22


### Assumption : There is a positive correlation between there being a large classification loss in all patches of a
### mosaic input and the BG loss is lesser than FG loss.

### w_i = 2 if min_j l_{ij}<0.7
### w_i = 0 if min_j l_{ij}>0.7

### w_i = 1.5 if min_j l_{ij}<0.7
### w_i = 0.5 if min_j l_{ij}>0.7
