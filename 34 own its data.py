#check if array owns its data

#copies owns the data,
# and views does not own the data,
# but how can we check this?---using base
#base that returns none if the array owns the data.
#otherwise, the base attribute refers to the original object.

#print the value of the base attribute to
#check if an array owns its data or not ?

import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

#the copy returns none.
#the view returns the original array
