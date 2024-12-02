#stacking along height(depth)

#numpy provides a helper function: dstack()to stack along height
#which is the same depth

import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

arr=np.dstack((arr1,arr2))
print(arr)