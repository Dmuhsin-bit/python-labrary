#converting data type on existing arrays

#the astype() function creates a copy of the array,
#and allows you to specify the data type as a parameter.

#change data type from float to integer by using 'i' as parameter value ?

import numpy as np

arr = np.array([1.1,2.1,3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)
