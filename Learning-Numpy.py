import numpy as np

a = np.array([2, 3, 4, 5])
b = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])

print(a)
print(b.ndim)  # Number of nested arrays/dimensions
print(b.shape)  # Vector 2 by 3 shape
print(b.dtype)  # type in bits
print(b.itemsize)  # showing type as 4 bytes / 32 bits
print("")

# Changed to 16 bits / 2 bytes
b = np.array([[1, 2, 3, 4], [1, 2, 3, 4]], dtype="int8")
print(b)
print("")

# When you know the data is not going to be big, you can change
# the type of bytes / bits, however if you have a big number
# such as '4222' and only assigned 8 bits, i will only store
# the maximum value of 126 in a 8 bit type
b = np.array([[1, 2, 3, 4222], [1, 2, 3, 4]], dtype="int8")
print(b)
print("")

# Need to change the type to a higher byte type
b = np.array([[1, 2, 3, 4222], [1, 2, 3, 4]], dtype="int16")
print(b)
print("")

print(b[0, 3])
# Printing a specific item in a nested array

print(b[0, -1])
# Also can go backwards

print(b[1, :])
# Prints everything in the row

print(b[:, 3])
# Prints all rows 3rd item.

# Syntax = [startindex:endindex:stepsize]
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a[0:-1:2])

# Starting at 0, ending at 10, Step by 2 = 1,3,5,7,9
print(b[0, 0:-1:2])

# Same as above however specifying which nested array to be used.
print("")

# Replacing a index in a array
a[2] = 20
print(a)

# Create an array matrix with all zeros
print(np.zeros((3, 4), "int16"))

# Matrix with all ones
print(np.ones((3, 4)))

# Matrix with any number
print(np.full((1, 2), 30))  # 30 being the number inside.

# Take a shape already built and change all the values
print(np.full_like(a, 30))

# Initialise a array of random float numbers
print(np.random.rand(4, 2, 3))

# Change random float values to a existing array
print(np.random.random_sample(a.shape))

# Random integer values
print(np.random.randint(7, size=(2, 3)))

# 0-7 rand range, shape of array 2 by 3.
print(np.random.randint(4, 7, size=(2, 3)))

# 4-7 rand range, shape of array 2 by 3.
print("")

# Repeat an array
arr = np.array([1, 2, 3])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

arr = np.array([[1, 2, 3]])  # Nested
r1 = np.repeat(arr, 3, axis=0)
print(r1)
print("")

output = np.ones([5, 5])
print(output)
zeros = np.zeros([3, 3])
print(zeros)
zeros[1:-1, 1:-1] = 9
print(zeros)
output[1:-1, 1:-1] = zeros
print(output)

# How to copy an array
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100

print(b)
print(a)

# Vertically stacking arrays
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

print(np.vstack([v1, v2]))
# Combines vertically both variables containing arrays

# Loading data from file
# filedata = np.genfromtxt('test.txt', delimiter=',')
# Input text file data into an array delimiter = separator
# filedata = filedata.astype('int32')
# Changes type to integer instead of float

# Boolean masking
print(a > 100)
print(a < 100)

# Advanced indexing
# Grabbing only values greater or less than a value
print(a[a < 50])
print(a[a < 2])

# Grabbing specific values in an array
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2, 8]])