#3-D arrays
#an array that has 2-D arrays (matrices) as its elements is called 3-D array.
#these are often used to represent a 3rd order tensor.


#create a 3-D array with two 2-D arrays,
# both containing two arrays with the values 1,2,3 and 4,5,6 ?

import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(arr)