#higher dimensional arrays
#an array can have any umber of dimensins.

#when the array is created,
#you can define the number of dimensions by using by *ndim* arguments.
#create an array with 5 dimension and verify that it has  5 dimensions?
import numpy as np
arr = np.array([1,2,3,4],ndmin=5)
print('number of dimensions : ',arr.ndim)
