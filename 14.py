#access 2-D arrays
#to access elements from 2-D arrays we can use
# coma separated integers representing the dimension
# and the index of the element.

#think of 2-0 arrays like a table with rows and colums,
#where the dimension represents the row and the index represents the column.

#access the elements on the first row, second column?

import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print('2nd element on 1st row:', arr[0,1])
#row index number, elements  index number
