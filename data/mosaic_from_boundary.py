import numpy as np
def boundary_mosaic_points(boundary_points,y_boundary):
  x_b = []
  y_b = []
  f_index = []
  for i in range(3):
    'pos'
    for j in range(8):
      for k in range(8,12,1):
        for l in range(8,12,1):
          a = []
          if i ==0:
            a.append(boundary_points[j])
            a.append(boundary_points[k])
            a.append(boundary_points[l])
            f_index.append(i)
          elif i==1:
            a.append(boundary_points[k])
            a.append(boundary_points[j])
            a.append(boundary_points[l])
            f_index.append(i)
          elif i==2:
            a.append(boundary_points[k])
            a.append(boundary_points[l])
            a.append(boundary_points[j])
            f_index.append(i)
          y_b.append(y_boundary[j])
          a = np.concatenate(a,axis=0)
          x_b.append(list(np.reshape(a,6)))
          
  x_b = np.array(x_b) 
  y_b = np.array(y_b)
  return x_b,y_b,f_index