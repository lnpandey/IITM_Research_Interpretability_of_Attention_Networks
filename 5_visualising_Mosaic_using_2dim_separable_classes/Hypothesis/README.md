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
| Data_distribution  | Linear SVM score | Accuracy | Analysis  |
| ------------------ | ---------------- | -------- | --------  |
|<img src= ./plots/distribution1.png width="150">  | 54.16  | 89.1 | <img src= ./plots/trends1.png width="150">  |
|<img src= ./plots/distribution2.png width="150">  |  54.16 | 66.4 | <img src= ./plots/trends2.png width="150">  |
|<img src= ./plots/distribution3.png width="150">  | 72.2  | 96.0 | <img src= ./plots/trends3.png width="150">  |
|<img src= ./plots/distribution4.png width="150">  |  70.15 | | <img src= ./plots/trends4.png width="150">  |
|<img src= ./plots/data_distribution_ns5.png width="150">  | 70.9  | 98.2 | <img src= ./plots/trends5.png width="150">  |
|<img src= ./plots/data_distribution_ns6.png width="150">  | 83.5  | 94.2 | <img src= ./plots/trends6.png width="150">  |

     
 

|   Focus Map epoch 1 | Classification  Map epoch 1 |  Focus Map epoch last | Classification  Map epoch last | 
|  ------------------ | --------------------------- |  ----------- | --------------------------- | 
|<img src= ./plots/f_map11.png width="150">  | <img src= ./plots/c_map11.png width="150">  | <img src= ./plots/f_map1l.png width="150">  | <img src= ./plots/c_map1l.png width="150">  |
|<img src= ./plots/f_map21.png width="150">  | <img src= ./plots/c_map21.png width="150">  | <img src= ./plots/f_map2l.png width="150">  | <img src= ./plots/c_map2l.png width="150">  |
|<img src= ./plots/f_map31.png width="150">  | <img src= ./plots/c_map31.png width="150">  | <img src= ./plots/f_map3l.png width="150">  | <img src= ./plots/c_map3l.png width="150">  |
|<img src= ./plots/f_map41.png width="150">  | <img src= ./plots/c_map41.png width="150">  | <img src= ./plots/f_map4l.png width="150">  | <img src= ./plots/c_map4l.png width="150">  |






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
