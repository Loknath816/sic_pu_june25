import numpy as np
def f(x, y):
	return 10 * x + y

my_aaray = np.fromfunction(f, (5, 4), dtype = int)

print(my_aaray)
# Slicing the Numpy Arrays:
print("-------------------------------------------------------")
print(my_aaray[2, 3]) # my_array[2][3]
print(my_aaray[0:5, 1]) # From Row-1 to Row-5, print the 2nd element
print(my_aaray[ : , 1]) # From all rows, print 2nd element
print(my_aaray[1:3, : ]) # From Row-2 to Row-3, print all elements
print()
print(my_aaray[1:3])
print()
print(my_aaray[ : , 0])