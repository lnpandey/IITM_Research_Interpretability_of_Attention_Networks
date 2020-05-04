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
   - Data Distribution
     
      ![](./plots/d2_data_distr.png)
   
   - SVM with Linear Kernel with C value 1000
      - Score 0.984  (Suggesting Mosaic data is not linearly separable)
    
      
    
   - At epoch zero
      
      ![](./plots/D_2_at_e0.png)
      
        - Focus output map
    
    ![](./plots/f2_l_1.png)
    
    
    ![](./plots/f2_l_2.png)

    ![](./plots/f2_l_3.png)
    
   - Classification output map    
     
     ![](./plots/c2_l_3.png)    
      
      
 
   - At epoch fifty
      
      ![](./plots/D2_at_e50.png)
      
          
       
    
    
   - Focus output map
    
    ![](./plots/f2_l5_1.png)
    
    
    ![](./plots/f2_l5_2.png)

    ![](./plots/f2_l5_3.png)
    
   - Classification output map    
     
     ![](./plots/c2_l5_3.png)   
   
   
   - At epoch hundred
    
      ![](./plots/D_2_at_e100.png) 
     

    
   - Focus output map
    
    ![](./plots/f2_l10_1.png)
    
    
    ![](./plots/f2_l10_2.png)

    ![](./plots/f2_l10_3.png)
    
   - Classification output map    
     
     ![](./plots/c2_l10_3.png)  
     
     
   - Accuracy 100%
   
   
   
   # When Data is linearly Separable
   - Data Distribution
     
      ![](./plots/ls_distr.png)
   
   - SVM with Linear Kernel with C value 1000
      - Score 1  (Suggesting Mosaic data is linearly separable)
    
      
    
   - At epoch zero
      
      ![](./plots/ls_e0.png)
        
      
      
      ![](./plots/ls2_e0.png)
      
      
      
        - Focus output map
    
    ![](./plots/f2_nl_1.png)
    
    
    ![](./plots/f2_nl_2.png)

    ![](./plots/f2_nl_3.png)
    
    
    
    
     - Classification output map    
     
     ![](./plots/c2_nl_3.png)  
      
      
 
     
     
     
   - At epoch fifty
  
  
  
  - Focus output map
    
    ![](./plots/f2_nl5_1.png)
    
    
    ![](./plots/f2_nl5_2.png)

    ![](./plots/f2_nl5_3.png)
    
    
    
    
     - Classification output map    
     
     ![](./plots/c2_nl5_3.png)   
     
     
     

   - At epoch hundred
    
      ![](./plots/ls_e100.png) 
      
      
      
      ![](./plots/ls2_e100.png)
      
      
      
      
   - Focus output map
    
    ![](./plots/f2_nl10_1.png)
    
    
    ![](./plots/f2_nl10_2.png)

    ![](./plots/f2_nl10_3.png)
    
    
    
    
   - Classification output map    
     
     ![](./plots/c2_nl10_3.png)   
     
   - Accuracy 100% , 2nd Case Accuracy is 100% at 5th epoch only
    
# Observations 
  - When mosaic data is not linearly separable 
     - The models needs attention to learn a good classifier.
     - For higher dimension once it learns some good attention weights, the attention weight learning stops.
  - When mosaic data is linearly separable
     - The model does not need attention to learn a good classifier.
     - For higher dimension model need not require to learn the attention weights, but is sometimes learning good attention weights.
