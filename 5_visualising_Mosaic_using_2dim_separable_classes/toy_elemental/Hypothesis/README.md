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
    
# Observations 
  - When mosaic data is not linearly separable 
     - The models needs attention to learn a good classifier.
  - When mosaic data is linearly separable
     - The model does not need attention to learn a good classifier.
