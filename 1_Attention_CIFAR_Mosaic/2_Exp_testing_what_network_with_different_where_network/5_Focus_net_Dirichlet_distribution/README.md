### Training Classification network by modelling output of Focus network as Dirichlet distribution with different alpha values
- Diffent alpha values are as following:
   - 1e-2  (sparse samples)
   - 0.5
   - 2
   - 1e5 (samples with equal weights)
  
 ### Observations 
 - With alpha value less than one, occassionaly background images will also get focussed as input to classification network.
 - These results are similar to the experiments done with randomly fixing the Focus network.
