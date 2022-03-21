Full EM here


For em step in 1 to 20:
  1. gamma values from E-step
  2. for epoch in range(10):
        3. for batch in train data
                4. update f
                5. update g
  
  
  | m\size | 10k | 30k |
  | --    | ---  | --  |
  | 5     | 60.21/72.54 (ftpt/acc) | 76.54/85.39 |
  | 20    | 76.14/85.39  | 63.9/ 84.91 |
