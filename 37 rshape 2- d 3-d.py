#rshape from 1-d to 3-d
#convert the following 1-d array with 12 elements into a 3-d array.

#the outermost dimension will have 2 arrays that contains 3 arrays,
#each with 2 elements:

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr.reshape(2,3,2)

print(newarr)
