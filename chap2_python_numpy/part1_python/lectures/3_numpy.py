import numpy as np

np.array([1,2,3])   # one dimensional array
np.array([[[1,2], [3,4]], [[5,6], [7,8]]])

np.zeros((3,4))
np.zeros((3,4), dtype=int)
np.ones((2,3))

np.full((2,3), fill_value=7) # fill in array with a value

np.empty((2,4))

np.eye(5, dtype=int) # identity matrix of size NxN

np.arange(0,10,2) # array in the range

np.linspace(0, np.pi, 5)  # Evenly spaced range with 5 elements

##############################################################################
# random elements in array
np.random.random((3,4))    # Elements are uniformly distributed from half-open interval [0.0,1.0)

np.random.normal(0, 1, (3,4))    # Elements are normally distributed with mean 0 and standard deviation 1

np.random.randint(-2, 10, (3,4))  # Elements are uniformly distributed integers from the half-open interval [-2,10)

np.random.seed(0) # create random numbers deterministically by use the same starting point


##############################################################################
# types and attributes
a=np.array([[1,2,3], [4,5,6]])
print(f"{a} has dim {a.ndim}, shape {a.shape}, size {a.size}, and dtype {a.dtype}:")


##############################################################################
# slicing
b=np.array([[1,2,3], [4,5,6]])
print(b)
print(b[:,0])
print(b[0,:])
print(b[:,1:])

print(b[:,0])    # First column
print(b[1,:])    # Second row

# reshaping
a=np.arange(9) # a has dim 1, shape (9,), size 9, and dtype int64
anew=a.reshape(3,3) # anew has dim 2, shape (3, 3), size 9, and dtype int64

d=np.arange(4) # dim 1, shape (4,), size 4
print(d[:, np.newaxis]) # dim 2, shape (4, 1)
print(d[np.newaxis, :]) # dim 2, shape (1, 4)
print(d[:, np.newaxis])  # dim 2, shape (4, 1)


##############################################################################
# concat (must have same ndim),split, stack
a=np.arange(2)
b=np.arange(2,5)
print(f"a has shape {a.shape}: {a}")
print(f"b has shape {b.shape}: {b}")
np.concatenate((a,b))  # array([0, 1, 2, 3, 4])

c=np.arange(1,5).reshape(2,2)
print(f"c has shape {c.shape}:", c, sep="\n")
np.concatenate((c,c))   # concatenating 2d arrays

# join arrays horizontally
np.concatenate((c,c), axis=1)

print("New row:")
print(np.concatenate((c,a.reshape(1,2))))
print("New column:")
print(np.concatenate((c,a.reshape(2,1)), axis=1))

# stack: create higher dimensional arrays from lower dimensional arrays
np.stack((b,b)) # stack vertically
np.stack((b,b), axis=1) # stack horizontally


# split": opposite to stack
# Its argument specifies either the number of equal parts the array is divided into
# or it specifies explicitly the break points.


##############################################################################
# aggregations
np.random.seed(0)
a=np.random.randint(-100, 100, (4,5))
print(a)
print(f"Minimum: {a.min()}, maximum: {a.max()}")
print(f"Sum: {a.sum()}")
print(f"Mean: {a.mean()}, standard deviation: {a.std()}")




