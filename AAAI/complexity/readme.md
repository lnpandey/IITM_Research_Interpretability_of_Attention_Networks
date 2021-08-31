### Table 1: Complexity effect on 5D elliptical blob data (Zeroth Layer averaging)
- Focus is functionally zero with no bias and 1 hidden layer initialised to xavier norm.
- Classify has 1 hidden layer with bias initialised to zero and weights initialised to xavier norm.
- Entry in the table is average over 10 runs and is of the form (avg Accuracy/ avg FTPT).
- Adam optimizer is used with LR = 0.001

| Focus \\ Classify ->  | 50 | 100 | 200 |
|-------------------------|----|-----|------|
| 50  | 99.99 / 89.13 | 99.99 / 96.13 | 99.99 / 99.99 |
| 100 | 99.96 / 92.17 | 99.99 / 92.66 | 99.99 / 93.59 |
| 200 | 99.98 / 88.89 | 99.97 / 94.64 | 99.98 / 86.50 |

### Table 2: Complexity effect on 5D elliptical blob data (First Layer averaging)
- Focus is functionally zero with no bias and 1 hidden layer initialised to xavier norm.
- Classify has 1 hidden layer with bias initialised to zero and weights initialised to xavier norm.
- Entry in the table is average over 10 runs and is of the form (avg Accuracy/ avg FTPT).
- Adam optimizer is used with LR = 0.001

| Focus \\ Classify ->  | 50 | 100 | 200 |
|-------------------------|----|-----|------|
| 50  | 99.99 / 93.52 | 99.99 / 99.94 | 99.99 / 99.99 |
| 100 | 99.96 / 96.76 | 99.99 / 100 | 99.99 / 100 |
| 200 | 99.99 / 99.99 | 99.97 / 99.99 | 99.98 / 100 |







