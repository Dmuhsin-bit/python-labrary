#find the indexes where the values are even ?

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])

x = np.where(arr%2 == 0) #for even
y = np.where(arr%2 == 1)  #for odd
print(x)
print(y)

