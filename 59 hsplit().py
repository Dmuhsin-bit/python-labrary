#use the hsplit() method to split the 2-d array
# into three 2-d arrays along rows?

import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])

newarr = np.hsplit(arr,3)
print(newarr)

#vspli() -- along coloums
#dsplit()-- depth(height)
