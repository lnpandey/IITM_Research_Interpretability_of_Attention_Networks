## Experiment Setup
In the previous folder, We observed in Table 4 that There has to a transition or threshold between row 9 to row 13 and row 5 to row 13.

| Row | Experiment Name | Focus_net Representation | Classify_net Representation|
|-----|-----------------|--------------------------|----------------------------|
| Row 5 | Focus Pretrained Classify Random no epoch | f5 | g5 |
| Row 9 | Focus Random Classify Pretrained no epoch | f9 | g9 |
| Row 13 | Focus Pretrained Classify Pretrained no epoch | f13 | g13 |

### Experiment 1: Between Row 9 and Row 13
To see if the Pretrained Classification Net detect small changes or not (i.e find threshold between row 9 to row 13):

We can create a multiple Attention networks with Focus and classify net as:
- focus net f = (1-beta)\*f9 + beta*f13, where beta lies between 0 & 1.
- classify net g = g9 = g13

Plot the results without training, i.e before 0th epoch.

### Table 1: Observations for Experiment 1 as beta increases from 0 to 1

| Plot Name | On Training Dataset | On Testing Dataset |
|-----------|---------------------|--------------------|
| Argmax trend   | <img src= ./plots_and_images/tr_argmax_focus.JPG width="400"> | <img src= ./plots_and_images/te_argmax_focus.JPG width="400"> |
| ftpt trend   | <img src= ./plots_and_images/tr_ftpt_focus.JPG width="400"> | <img src= ./plots_and_images/te_ftpt_focus.JPG width="400"> |
| Accuracy trend   | <img src= ./plots_and_images/acc_focus.JPG width="400"> | <img src= ./plots_and_images/acc_focus.JPG width="400"> |

### Experiment 2: Between Row 5 and Row 13
To see if the Pretrained Focus Net detect small changes or not (i.e find threshold between row 5 to row 13):

We can create a multiple Attention networks with Focus and classify net as:
- focus net f = f5 = f13, where beta lies between 0 & 1.
- classify net g = (1-beta)\*g5 + beta*g13

Plot the results without training, i.e before 0th epoch.

### Table 2: Observations for Experiment 2 as beta increases from 0 to 1

| Plot Name | On Training Dataset | On Testing Dataset |
|-----------|---------------------|--------------------|
| Argmax trend   | <img src= ./plots_and_images/tr_argmax_classify.JPG width="400"> | <img src= ./plots_and_images/te_argmax_classify.JPG width="400"> |
| ftpt trend   | <img src= ./plots_and_images/tr_ftpt_classify.JPG width="400"> | <img src= ./plots_and_images/te_ftpt_classify.JPG width="400"> |
| Accuracy trend   | <img src= ./plots_and_images/acc_classify.JPG width="400"> | <img src= ./plots_and_images/acc_classify.JPG width="400"> |


