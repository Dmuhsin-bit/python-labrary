#split the 2-d array into three 2-d arrays.

import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])

newarr = np.array_split(arr,3,axis=1) #0 row wise

print(newarr)
