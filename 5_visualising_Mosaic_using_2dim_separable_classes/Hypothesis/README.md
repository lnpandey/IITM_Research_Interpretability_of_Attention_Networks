  ### Attention is required only when data is not linearly separable D_1  K_2 NF_2 NB_1
  
  # Mosaic Data is not linearly separable
    - data distribution
    
    
  ![](./plots/data_distr.PNG)
    
   - Mosaic Data
    
   ![](./plots/mosaic_data.PNG)
    
  - Learning attention weights 
  
     # Not good attention weights
     - At epoch zero
    
    ![](./plots/At_epoch_zero_not_Sep.PNG)
    
    
    - At epoch hundred
    
    ![](./plots/At__epoch_100_non_sep.PNG)
    
    
    -  Accuracy 58.7%
     
     
     # good attention weights
     - At epoch zero
    
    ![](./plots/gaw_at_epoch_zero_non_sep.PNG)
    


     - At epoch hundred 
    
    ![](./plots/gaw_at_epoch_hun_non_sep.PNG)
    
    


    - Accuracy 99.1%
    
    
    
    
    # Mosaic Data is linearly separable
    - data distribution
    
    
  ![](./plots/data_distr_ls.PNG)
    
   - Mosaic Data
    
   ![](./plots/mosaic_data_ls.PNG)
    
  - Learning attention weights 

     - At epoch zero
    
    ![](./plots/At_epoch_zero_Sep.PNG)
     
     - At epoch hundred
    
    ![](./plots/At_epoch_100_Sep.PNG)
    
    -  Accuracy 100%
    
  
### D_2 K_3 NF_2 NB_1  
  # When Data is not linearly Separable



|Data Distribution   | Linear SVM Accuracy on Mosaic Data |  Deep Network Accuracy on Mosaic Data | Linear Attention network Accuracy | Deep Attention Newtork Accuracy | Analysis Linear Attention Network | Analysis Deep Attention Network |
| ------------------ | ----------------------------------- | ------------------------------------ | ------------------- | ------------------------------------------------- | ----------------------- | ------------------------------ |
| <img src= ./plots/distribution1.png width="150">  | 75 |  80 |  100 | 100 |<img src= ./plots/trends1.png width="150">   |  <img src= ./plots/trends2.png width="150">  |
| <img src= ./plots/distribution2.png width="150">  | 82 |  90.1 |  100 | 100 |<img src= ./plots/trends3.png width="150">   |  <img src= ./plots/trends4.png width="150">  | 
| <img src= ./plots/distribution3.png width="150">  | 63.03  |  99.23 | 74.46  | 91.1 |<img src= ./plots/trends5.png width="150">   |  <img src= ./plots/trends6.png width="150">  | 






|   Focus Map epoch 1 | Classification  Map epoch 1 |  Focus Map epoch last | Classification  Map epoch last | 
|  ------------------ | --------------------------- |  ----------- | --------------------------- | 
|<img src= ./plots/f_map11.png width="150">  | <img src= ./plots/c_map11.png width="150">  | <img src= ./plots/f_map1l.png width="150">  | <img src= ./plots/c_map1l.png width="150">  |
|<img src= ./plots/f_map21.png width="150">  | <img src= ./plots/c_map21.png width="150">  | <img src= ./plots/f_map2l.png width="150">  | <img src= ./plots/c_map2l.png width="150">  |
|<img src= ./plots/f_map31.png width="150">  | <img src= ./plots/c_map31.png width="150">  | <img src= ./plots/f_map3l.png width="150">  | <img src= ./plots/c_map3l.png width="150">  |
|<img src= ./plots/f_map41.png width="150">  | <img src= ./plots/c_map41.png width="150">  | <img src= ./plots/f_map4l.png width="150">  | <img src= ./plots/c_map4l.png width="150">  |
|<img src= ./plots/f_map51.png width="150">  | <img src= ./plots/c_map51.png width="150">  | <img src= ./plots/f_map5l.png width="150">  | <img src= ./plots/c_map5l.png width="150">  |
|<img src= ./plots/f_map61.png width="150">  | <img src= ./plots/c_map61.png width="150">  | <img src= ./plots/f_map6l.png width="150">  | <img src= ./plots/c_map6l.png width="150">  |





| Data    | Fg vs Bg Score(Linear) | fg1 vs fg2 score(Linear) | Linear SVM score(Mosaic) | Linear Attention Network Score | Deep Attention Network Score| Deep Network Score  |
| --------| ---------------------- | ------------------------ | ------------------------ | ----------------------------- | ---------------------------- | ------------------  |   
| D_3_K_5 |    91                  |       93.1               |     63.8                 |     91.6                      |    96.1                      |                     |
| D_3_K_5 |    80                  |       87.43              |     62                   |     76.73                     |    86.9                      |                     |
| D_4_K_5 |    80.4                |       89.89              |     68                   |     80                        |     88.93                    |                     |
| D_4_K_10|    80.4                |       89.39              |     62.56                |     73.86                     |     87.06                    |     98.8            |
| D_5_K_5 |    86.2                |       83.33              |     62.9                 |     80.33                     |     96.36                    |                     |
| D_5_K_10|    86.4                |       83.83              |     60.1                 |     78.4                      |     95.93                    |                     |


| Data     |  Linear Attention Trends                    |    Deep Attention Trends                    |
| ------   |  ---------------------------------------    |    --------------------------------------   |
| D_3_K_5  | <img src= ./plots/trends_Linear_D_3.png width="150">  |  <img src= ./plots/trends_Deep_D_3.png width="150"> |
| D_3_K_5  | <img src= ./plots/trends_Linear_D_3_K_5.png width="150">  |  <img src= ./plots/trends_Deep_D_3_K_5.png width="150"> |
| D_4_K_5  | <img src= ./plots/trends_Linear_D_4_K_5.png width="150">  |  <img src= ./plots/trends_Deep_D_4_K_5.png width="150"> |
| D_4_K_10 | <img src= ./plots/trends_Linear_D_4_K_10.png width="150"> |  <img src= ./plots/trends_Deep_D_4_K_10.png width="150"> |
| D_5_K_5  | <img src= ./plots/trends_Linear_D_5_K_5.png width="150">  |  <img src= ./plots/trends_Deep_D_5_K_5.png width="150"> |
| D_5_K_10 | <img src= ./plots/trends_Linear_D_5_K_10.png width="150"> |  <img src= ./plots/trends_Deep_D_5_K_10.png width="150"> |

### Deep Attention Model
```python
class Focus_deep(nn.Module):
    '''
       deep focus network averaged at zeroth layer
       input : elemental data
    '''
    def __init__(self,inputs,output,K,d):
        super(Focus_deep,self).__init__()
        self.inputs = inputs
        self.output = output
        self.K = K
        self.d  = d
        self.linear1 = nn.Linear(self.inputs,50)  #,self.output)
        self.linear2 = nn.Linear(50,self.output) 
    def forward(self,z):
        batch = z.shape[0]
        x = torch.zeros([batch,self.K],dtype=torch.float64)
        y = torch.zeros([batch,self.d], dtype=torch.float64)
        #x,y = x.to("cuda"),y.to("cuda")
        for i in range(self.K):
            x[:,i] = self.helper(z[:,self.d*i:self.d*i+self.d])[:,0]
        x = F.softmax(x,dim=1)   # alphas
        x1 = x[:,0]
        for i in range(self.K):
            x1 = x[:,i]          
            y = y+torch.mul(x1[:,None],z[:,self.d*i:self.d*i+self.d])
        return y , x 
    def helper(self,x):
      x = F.relu(self.linear1(x))
      x = self.linear2(x)
      return x

class Classification_deep(nn.Module):
    '''
       input : elemental data
       deep classification module data averaged at zeroth layer
    '''
    def __init__(self,inputs,output):
        super(Classification_deep,self).__init__()
        self.inputs = inputs
        self.output = output
        self.linear1 = nn.Linear(self.inputs,50)
        self.linear2 = nn.Linear(50,self.output)

    def forward(self,x):
      x = F.relu(self.linear1(x))
      x = self.linear2(x)
      return x    
```
### Synthetic Data Pretrained Models(Cheating)
D_4 K_10 (Linear Model)
| Focus Init      | Classification Init             | Training Module          | Training Acuracy  | Analysis                                                     |
| --------------- | --------------------------      | ------------------------ | ----------- ----- | ---------------------------------------------------          |
| Random          | Random                          |   -                      |    51.20      | NA                                                               |
| Random          | Random                          |   Both                   |    73.73      | img src= ./plots/both_randomb_trends_D_4_K_10.png width="150">   |               
| Random          | Random                          |   Focus                  |    62.7       | img src= ./plots/focus_randomb_trends_D_4_K_10.png width="150"> |
| Random          | Random                          |   classify               |    59.96      | img src= ./plots/classify_randomb_trends_D_4_K_10.png width="150">|
| Random          | Pretrained                      |   -                      |    56.56      | NA                                                         |
| Random          | Pretrained                      |   Both                   |    73.8       | img src= ./plots/both_randomf_trends_D_4_K_10.png width="150"> |               
| Random          | Pretrained                      |   Focus                  |    71.9       | img src= ./plots/focus_randomf_trends_D_4_K_10.png width="150">      |
| Random          | Pretrained                      |   classify               |    54.5       | img src= ./plots/classify_randomf_trends_D_4_K_10.png width="150">      |    
| Pretrained      | Random                          |   -                      |    49.86      | NA                                                         |
| Pretrained      | Random                          |   Both                   |    74.76      | img src= ./plots/both_randomc_trends_D_4_K_10.png width="150"> |               
| Pretrained      | Random                          |   Focus                  |    50.06      | img src= ./plots/focus_randomc_trends_D_4_K_10.png width="150">       |
| Pretrained      | Random                          |   classify               |  73.63        | img src= ./plots/classify_randomc_trends_D_4_K_10.pngwidth="150">      | 
| Pretrained      | Pretrained                      |   -                      | 73.46         | NA                                                         |
| Pretrained      | Pretrained                      |   Both                   | 74.6          | img src= ./plots/both_norandom_trends_D_4_K_10 width="150">|               
| Pretrained      | Pretrained                      |   Focus                  | 73.63         | img src= ./plots/focus_norandom_trends_D_4_K_10.png width="150">      |
| Pretrained      | Pretrained                      |   classify               |   73.3        | img src= ./plots/classify_norandom_trends_D_4_K_10.pngwidth="150">      | 





D_4 K_10 (Deep Model)
| Focus Init      | Classification Init             | Training Module          | Training Acuracy         | Analysis                                              |
| --------------- | --------------------------      | ------------------------ | ------------------------ | ---------------------------------------------------   |
| Random          | Random                          |   -                      |        54.4              | NA                                                    |
| Random          | Random                          |   Both                   |        88.06             | img src= ./plots/ch_trends_D_4_K_10.png width="150">  |               
| Random          | Random                          |   Focus                  |        72.03             | img src= ./plots/chf_trends_D_4_K_10.png width="150"> |
| Random          | Random                          |   classify               |        63.36             | img src= ./plots/chc_trends_D_4_K_10.png width="150"> |
| Random          | Pretrained                      |   -                      |                      | NA                                                    |
| Random          | Pretrained                      |   Both                   |                   | img src= ./plots/ch_trends_D_4_K_10.png width="150">  |               
| Random          | Pretrained                      |   Focus                  |                     | img src= ./plots/chf_trends_D_4_K_10.png width="150"> |
| Random          | Pretrained                      |   classify               |                     | img src= ./plots/chc_trends_D_4_K_10.png width="150"> |        



<!--- | Data_distribution  | Linear SVM score |Deep NN Score| Accuracy | Analysis  |
| ------------------ | ---------------- | ----------- |-------- | --------  |
|<img src= ./plots/distribution1.png width="150">  | 66.4 | 67.1875 | 79.7 | <img src= ./plots/trends1.png width="150">  |
|<img src= ./plots/distribution2.png width="150">  |  62.2 | 69.2 | 69.1 | <img src= ./plots/trends2.png width="150">  |
|<img src= ./plots/distribution3.png width="150">  | 59.375 | 80.9 | 100.0 | <img src= ./plots/trends3.png width="150">  |
|<img src= ./plots/distribution4.png width="150">  |  77.60 | 81.28 |92.2| <img src= ./plots/trends4.png width="150">  |
|<img src= ./plots/distribution5.png width="150">  | 66.97  | 78.32 |87.1| <img src= ./plots/trends5.png width="150">  |
|<img src= ./plots/distribution5.png width="150">  | 68.2  | 88.150 | 96.4 | <img src= ./plots/trends6.png width="150">  |---!>


     
 









   <!--- # When Data is linearly Separable
   - Data Distribution
     
      ![](./plots/ls_distr.png)
   
   - SVM with Linear Kernel with C value 1000
      - Score 1  (Suggesting Mosaic data is linearly separable)
    
      
    
   - At epoch zero
              
      
   - Focus Map 

      ![](./plots/s_plot_1.png)
      
      
      
      ![](./plots/s_fm_1.png)


   
   - Classification Map
       

      ![](./plots/s_cm_1.png)
      
            
      

   - At epoch hundred
    
   

   - Focus Map 

      ![](./plots/s_plot_100.png)
      
      
      
      ![](./plots/s_fm100_1.png)


   
   - Classification Map
       

      ![](./plots/s_cm100_1.png)

     

      
      
      
      
     
   - Accuracy 100% -->
    
# Observations 
  - When mosaic data is not linearly separable 
     - The models needs attention to learn a good classifier.
     - For higher dimension once it learns some good attention weights, the attention weight learning stops.
  - When mosaic data is linearly separable
     - The model does not need attention to learn a good classifier.
     - For higher dimension model need not require to learn the attention weights, but is sometimes learning good attention weights.
