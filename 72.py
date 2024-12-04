#creating filter directly from array

#we can directly substitute the array instead
#of the iterable variable in our condition and
# it will work just as we expect it to.

#create a filter array that will return only values higher than 42 ?

import numpy as np

arr = np.array([1,2,3,4,5,6,7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
