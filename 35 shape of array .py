# shape of an array
#the shape of an array is the number of elements in each dimension.

#numpy arrays have an attribute called shape that returns
# a tuple with each index having the number of corresponding elements.

#print the shape of a 2-D array ?
import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

print(arr.shape)

#the example above returns (2,4), which means that
#the array has 2 dimensions,
#where the first dimension has 2 elements  and the second  has 4
