#numpy array copy vs view

#the difference between copy vs view

#the main difference between a copy and a view of an array is that:
#the copy is a new array,
#and the view is a view of the original array.

#the copy owns the data
# any changes made to the copy will not affect original array,
#and any changes made to the original array will not affect the copy.

#the view does not own the data and
#any changes made to the view will affect the orginal array,
# and any changes made to the original array will affect the view.
