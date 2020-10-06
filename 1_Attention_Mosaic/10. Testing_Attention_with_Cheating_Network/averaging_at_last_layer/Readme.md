### averaging at last layer

Base Models - 6 layer CNN Network



| - | - | Train Accuracy   |Test Accuracy     |
| - | - |--------- | -----   |
| FG_012 | FG vs BG | 99 | 90  |
| FG_012(Focus_random ) | FG1 vs FG2 vs Fg3 | 99 | 82 |
| FG_012(Focus_Pretrained) | FG1 vs FG2 vs Fg3 | 100 | 89 |
| FG_234 | FG vs BG | 99 | 86  |
| FG_234(Focus_random) | FG1 vs FG2 vs Fg3 | 99 |64 |
| FG_234(Focus_Pretrained) | FG1 vs FG2 vs Fg3 | 100 | 73 |


<!---#### Fg vs Bg Classification

Train Accuracy - 99

Test Accuarcy  - 90
#### Fg1 vs FG2 vs Fg3 classification
Train Accuracy - 99

Test Accuracy - 82 --->

```python
class Classification(nn.Module):
  def __init__(self):
    super(Classification, self).__init__()
    self.conv1 = nn.Conv2d(in_channels=256, out_channels=128, kernel_size=3, padding=1)
    self.conv2 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1)
    self.conv3 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1)
    self.conv4 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1)
    self.conv5 = nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, padding=1)
    self.conv6 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1)
    self.pool = nn.MaxPool2d(kernel_size=2, stride=2,padding=1)
    self.batch_norm1 = nn.BatchNorm2d(128,track_running_stats=False)
    self.batch_norm2 = nn.BatchNorm2d(256,track_running_stats=False)
    self.batch_norm3 = nn.BatchNorm2d(512,track_running_stats=False)
    self.dropout1 = nn.Dropout2d(p=0.05)
    self.dropout2 = nn.Dropout2d(p=0.1)
    self.global_average_pooling = nn.AvgPool2d(kernel_size=2)
    self.fc1 = nn.Linear(512,128)
    # self.fc2 = nn.Linear(128, 64)
    # self.fc3 = nn.Linear(64, 10)
    self.fc2 = nn.Linear(128, 3)
```
```python
class Focus(nn.Module):
  def __init__(self,pretrained =True):
    super(Focus, self).__init__()
    self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=0)
    self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=0)
    self.conv3 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=0)
    self.conv4 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=0)
    self.conv5 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=0)
    self.conv6 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1)
    self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
    self.batch_norm1 = nn.BatchNorm2d(32,track_running_stats=False)
    self.batch_norm2 = nn.BatchNorm2d(64,track_running_stats=False)
    self.batch_norm3 = nn.BatchNorm2d(256,track_running_stats=False)
    self.dropout1 = nn.Dropout2d(p=0.05)
    self.dropout2 = nn.Dropout2d(p=0.1)
    self.fc1 = nn.Linear(256,64)
    self.fc2 = nn.Linear(64, 32)
    self.fc3 = nn.Linear(32, 10)
    self.fc4 = nn.Linear(10, 2)
    self.pretrained = pretrained
```
## Note: Pretrained classification network is trained with Focus Random and Focus Pretrained(For following tables two numbers for classification pretrained(first one is focus random and second one is focus pretrained )) 

### FG 012
| | Focus init | Classification init | trained | train accuracy | test accuracy |
| - | ---------  | ------------------- | ------- | -------------  | ------------  |
|1| random | random | - | 33 |  32 |
|2| random | random | both | 99 | 95 |
|3| random | random | classify | 93 | 41 |
|4| random | random | focus    | 63 | 61 |
|5| pretrained | random | - | 33  |  32 |
|6| pretrained | random | both | 99 | 97|
|7| pretrained | random | classify | 96 | 94 |
|8| pretrained | random | focus    | 75 | 74 |
|9| random     | pretrained | -    | 46 | 46 |
|10| random    | pretrained | both | 99 | 92 |
|11| random    | pretrained | classify |  95 | 46 |
|12| random    | pretrained | focus   | 99  | 87 |
|13| pretrained | pretrained | - | 55/98 | 55/98 |
|14| pretrained | pretrained | both | 99/99 | 97/99 |
|15| pretrained | pretrained | classify |99/99 | 97/99 |
|16| pretrained | pretrained | focus    | 97/99 | 95/99 |

### FG 234

<!---#### Fg vs Bg Classification

Train Accuracy - 99

Test Accuarcy  - 86

#### Fg1 vs FG2 vs Fg3 classification
Train Accuracy - 99

Test Accuracy - 64--->


| | Focus init | Classification init | trained | train accuracy | test accuracy |
| - | ---------  | ------------------- | ------- | -------------  | ------------  |
|1| random | random | - | 33 |  32 |
|2| random | random | both |  99 | 90 |
|3| random | random | classify | 95 | 37 |
|4| random | random | focus    | 78 | 69 |
|5| pretrained | random | - |  33 | 33  |
|6| pretrained | random | both | 97 | 93 |
|7| pretrained | random | classify | 95 | 90 |
|8| pretrained | random | focus    | 92 | 87 |
|9| random     | pretrained | -    | 38 | 39 |
|10| random    | pretrained | both | 94 | 60 |
|11| random    | pretrained | classify |  68 | 39 |
|12| random    | pretrained | focus   | 94  |  74 |
|13| pretrained | pretrained | - | 36 | 35 |
|14| pretrained | pretrained | both |  99 | 96 |
|15| pretrained | pretrained | classify | 99 | 96  |
|16| pretrained | pretrained | focus    | 94 | 73 |


