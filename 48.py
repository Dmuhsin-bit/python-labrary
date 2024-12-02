#enumerated iteration using ndnumerate()

#enumeration means mentioning sequence number of something one by one
#sometimes we require corresponding index of the element while iterating
#the ndenumerate() method ca be used for those usecases

#enumerate on following 1d arrays

import numpy as np
arr=np.array([1,2,3,4,5])

for idx, x in np.ndenumerate(arr):
    print(idx,x)
#enumerate on the following 2-d array

import numpy as np
ar=np.array([[1,2,3],[4,5,6]])

for idx,x in np.ndenumerate(ar):
    print(idx,x)