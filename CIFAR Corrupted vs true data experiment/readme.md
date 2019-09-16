Finding out how the trend is if we corrupt cifar labels by 0,10,20,30,40,50 percentage.
Efficient Net is used.

####Please read the REPORT FILE attached


######A better version of code and report is present in Inception Net Folder, where I have used a smaller version of inception net.
weights of inception net is also available in inception net folder.


|      Analysis of Accuracy on Training & Testing Data      |                                        |               |        |                                       |              |        |                            |
|:---------------------------------------------------------:|----------------------------------------|---------------|--------|---------------------------------------|--------------|--------|----------------------------|
| corruption level                                          | Train accuracy on corrupted train-data |               |        | Test accuracy on corrupted test data  |              |        | Test accuracy on true data |
|                                                           | corrupted                              | un-corrupted  | full   | corrupted                             | un-corrupted | full   |                            |
| 0%                                                        | -NIL-                                  | 1             | 1      | -NIL-                                 | -NIL-        | -NIL-  | 0.83                       |
| 5%                                                        | 1                                      | 1             | 1      | 0.0858                                | 0.7830       | 0.7481 | 0.78                       |
| 10%                                                       | 1                                      | 1             | 1      | 0.1028                                | 0.7509       | 0.6841 | 0.75                       |
| 20%                                                       | 1                                      | 1             | 1      | 0.1028                                | 0.6659       | 0.5505 | 0.66                       |
| 30%                                                       | 1                                      | 1             | 1      | 0.1019                                | 0.5864       | 0.4405 | 0.58                       |
| 40%                                                       | 1                                      | 1             | 1      | 0.1031                                | 0.5058       | 0.3462 | 0.50                       |
| 50%                                                       | 1                                      | 1             | 1      | 0.0970                                | 0.4252       | 0.2625 | 0.42                       |
| 100%                                                      | 0.99                                   | -NIL-         | 0.99   | 0.1084                                | -NIL-        | 0.1084 | 010                        |
|                                                           |                                        |               |        |                                       |              |        |                            |
| Analysis of Cross Entropy Loss on Training & Testing Data |                                        |               |        |                                       |              |        |                            |
| corruption level                                          | Train cross entropy loss on train-data |               |        | Test cross entropy loss on train-data |              |        | Test CE loss on true data  |
|                                                           | corrupted                              | un-corrupted  | full   | corrupted                             | un-corrupted | full   |                            |
| 0%                                                        | -NIL-                                  | 0.0014        | 0.0014 | -NIL-                                 | -NIL-        | -NIL-  | 0.7550                     |
| 5%                                                        | 0.0008                                 | 0.0001        | 0.0002 | 11.9317                               | 1.0995       | 1.6422 | 1.1018                     |
| 10%                                                       | 0.0005                                 | 0.0001        | 0.0002 | 11.2546                               | 1.3577       | 2.3781 | 1.3478                     |
| 20%                                                       | 0.0004                                 | 0.0001        | 0.0002 | 10.2894                               | 1.8734       | 3.5995 | 1.8783                     |
| 30%                                                       | 0.0004                                 | 0.0001        | 0.0002 | 9.8259                                | 2.4355       | 4.6615 | 2.4304                     |
| 40%                                                       | 0.0004                                 | 0.0002        | 0.0002 | 9.3006                                | 2.9981       | 5.4971 | 3.0478                     |
| 50%                                                       | 0.0004                                 | 0.0002        | 0.0003 | 9.1102                                | 3.9016       | 6.4840 | 3.9291                     |
| 100%                                                      | 0.0014                                 | -NIL-         | 0.0014 | 9.1871                                | -NIL-        | 9.1871 |                            |
