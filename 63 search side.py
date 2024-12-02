#search from the  sides

#find the indexes where the value 7 should be inserted,
#starting from the right ?


import numpy as np

arr = np.array([6,7,8,9])

x = np.searchsorted(arr,7,side='right')
y = np.searchsorted(arr,6,side='left')
print(x)
print(y)

