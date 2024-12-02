#numpy joining array
#joining numpy arrays
#joining means putting contents of two or more arrays in asingle array
#concatenate() function

import numpy as np

arr=np.array([1,2,3])
arr1=np.array([4,5,6])

arr2=np.concatenate((arr,arr1))
print(arr2)