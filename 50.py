#join two d arrays along rows(axis=1)

import numpy as np

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])

arr=np.concatenate((arr1,arr2),axis=1)
print(arr)


#numpy axis are the directions along the rows and columns
#axis=1 ----column wise
#axis=0---row wise