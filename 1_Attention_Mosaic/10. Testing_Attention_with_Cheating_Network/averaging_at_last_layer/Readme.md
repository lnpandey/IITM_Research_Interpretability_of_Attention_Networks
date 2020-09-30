### averaging at last layer

Base Models - 6 layer CNN Network

#### Fg vs Bg Classification

Train Accuracy - 99

Test Accuarcy  - 90
#### Fg1 vs FG2 vs Fg3 classification
Train Accuracy - 99

Test Accuracy - 82

| | Focus init | Classification init | trained | train accuracy | test accuracy |
| - | ---------  | ------------------- | ------- | -------------  | ------------  |
|1| random | random | - | 33 |  32 |
|2| random | random | both | 99 | 95 |
|3| random | random | classify | 93 | 41 |
|4| random | random | focus    | 33 | 32 |
|5| pretrained | random | - | 33 | 33 |
|6| pretrained | random | both | 99 | 97|
|7| pretrained | random | classify | 99 | 97 |
|8| pretrained | random | focus    | 33 | 33 |
|9| random     | pretrained | -    | 32 | 31 |
|10| random    | pretrained | both | 99 | 94 |
|11| random    | pretrained | classify |  |  |
|12| random    | pretrained | focus   |  | |
|13| pretrained | pretrained | - | 55 | 55 |
|14| pretrained | pretrained | both | 99 | 97 |
|15| pretrained | pretrained | classify |98 | 96 |
|16| pretrained | pretrained | focus    | 34 | 34 |

