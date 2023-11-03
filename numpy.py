import numpy
from numpy import random

# ----- BASIC ----- #

# CREATE ARRAY
array = numpy.array(55)
arrays = numpy.arange(1, 16)
singleArray1, singleArray2 = numpy.array(numpy.arange(1, 11)), numpy.array(('a', 'b', 'c', 'd', 'e'))
twoDArray = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
threeDArray = numpy.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
fourDArray = numpy.array([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]])

# GET ITEM
# print(singleArray1[-1] + singleArray1[0])
# print(twoDArray[0, 1])
# print(threeDArray[0, 1, 2])

# CHECK DIMENSION LENGTH
# print(fourDArray.ndim) # check array dimension

# CREATE DIMENSION ARRAY
# createDimension = numpy.array([2, 3], ndmin=5) # create dimension
# print(f"Result: {createDimension}\nDimension: {createDimension.ndim}")

# SLICING
# print(singleArray1[1:3]) # slicing
# print(singleArray1[-4:-1]) # slicing backward
# print(singleArray1[0:len(singleArray1):2], singleArray1[::2]) # slicing step
# print(threeDArray[0, 2, 1:3]) # slicing in dimension array
# print(twoDArray[0:2, 1]) # slicing in dimension array in reverse

# DATA TYPE
# print(singleArray2.dtype) # check data type
# newInt = singleArray1.astype('f') # change data type to 'Float'
# newBool = singleArray1.astype(bool) # change data type 'Bool'
# newInt = numpy.array([2.5, 5.8], dtype=int) # change data type 'Int'
# print(newInt.dtype, newBool, newInt)

# COPY = change copy | original not
# copy = singleArray2.copy() # copy array
# copy[0] = 'fyqq' # change the copy array
# print(f"Original: {singleArray2}\nCopy: {copy}")
# print(copy.base) # check if own data | None

# VIEW = change original and copy 
# view = singleArray1.view() # view array
# view[0] = 9 # change the view array
# print(f"Original: {singleArray1}\nView: {view}")
# print(copy.base) # check if own data | singleArray1

# SHAPE
# print(numpy.array([1, 2, 3], ndmin=4).shape) # (1, 1, 1, 3)
# print(twoDArray.shape) # (3, 4)
# print(numpy.array(['a', 'b', 'c', 'd', 'e', 'f']).reshape(3, 2)) # change dimension
# [['a', 'b'], ['c', 'd'], ['e', 'f']]

# RESHAPE
# print(singleArray1.reshape(2, 4)) # change dimension [[x, x, x, x], [x, x, x, x]]
# print(singleArray1.reshape(2, 2, 2)) # change dimension [[[X, X], [x, x]], [[x, x], [x, x]]]
# print(twoDArray.reshape(-1)) # dimension array to normal array
# print(singleArray1.reshape(2, len(singleArray1) // 2))

# ITERATING
# [print(arr) for arrays in twoDArray for arr in arrays] # loop shorthand
# for arrays in twoDArray: # looping
#     for arr in arrays:
#         print(arr)
# [print(arr) for arr in numpy.nditer(threeDArray)] # looping through normal array
# [print(arr) for arr in numpy.nditer(singleArray1, flags=['buffered'], op_dtypes=float)] # looping & change data type
# [print(arr) for arr in numpy.nditer(singleArray1[4:])] # looping & slicing
# [print(index, array) for index, array in numpy.ndenumerate(singleArray1)] # looping & enumerate

# JOIN
# print(f"{singleArray1}\n{singleArray2}")
# print(numpy.concatenate((arrays, singleArray1))) # concat only single array 
# print(numpy.concatenate((numpy.array([[1, 2]]), numpy.array([[3, 4]])), axis=1)) # concate 2D Array
# print(numpy.concatenate((numpy.array([[[1, 2]]]), numpy.array([[[3, 4]]])), axis=2)) # concate 3D Array
# print(numpy.hstack((numpy.array([1, 2]), numpy.array(([3, 4]))))) # normal concate
# print(numpy.vstack((numpy.array([1, 2]), numpy.array(([3, 4]))))) # concate 2D array
# print(numpy.dstack((numpy.array([1, 2]), numpy.array(([3, 4]))))) # concate 3D array

# SPLIT
# print(numpy.array_split(arrays, 4)) # split item on single array
# print(numpy.array_split(arrays, 4)[1]) # get item after split item
# print(numpy.array_split(twoDArray, 2)) # split item on 2D array
# print(numpy.hsplit(twoDArray, 2)) # split item with 2 item into 2 array 

# SEARCHING
# print(numpy.where(singleArray1 == 4)) # find every single item on index
# print(numpy.searchsorted(singleArray1, 2)) # find item on index
# print(numpy.searchsorted(numpy.array([1, 2, 3, 4, 5, 6]), 5, side='right')) # find item on index start with right
# print(numpy.argmin(singleArray1)) # find min number on index (any dimension)
# print(numpy.argmax(singleArray1)) # find max number on index (any dimension)
# print(numpy.nonzero([0, 5, 1, 2, 0, 4, 0])) # remove '0'
# print(numpy.extract(singleArray1 > 5, singleArray1)) # filter array (any dimension)

# SORTED
# print(numpy.sort([5, 4, 3, 2, 1])) # sort list number
# print(numpy.sort(['d', 'c', 'a', 'b'])) # sort list string
# print(numpy.sort([[5, 7, 2], [1, 3, 0]])) # sort in each list

# FILTER
# print(singleArray1[[False, True, False, True, False, True, False, True, False, True]]) # show item on true


# ----- RANDOM ----- #

# lists = numpy.arange(5)

# print(random.randint(5)) # random number 0 to 5
# print(random.randint(10, size=5)) # 5 random number 0 to 10
# print(random.randint(10, size=(2, 5))) # 5 random number in 2 list

# print(random.rand()) # random float 
# print(random.rand(5)) # 5 random float 
# print(random.rand(2, 5)) # 5 random float in 2 list

# print(random.choice(lists)) # 1 random number in list
# print(random.choice(lists, size=3)) # 3 random number in list
# print(random.choice(lists, size=(2, 4))) # 4 random in 2 list

# print(random.choice([2, 4, 6, 8], p=[0.1, 0.3, 0.6, 0.0], size=(10))) # 10 random int in list
# print(random.choice(['a', 'd', 'b', 'c'], p=[0.1, 0.3, 0.6, 0.0], size=(10))) # 10 random str in list
# print(random.choice([2, 4], p=[0.5, 0.5], size=(2))) # probabilty must sum result 1
# print(random.choice([1, 3, 5], p=[0.35, 0.35, 0.3], size=(2, 3))) # 3 random int int 2 list

# random.shuffle(lists) # shuffle random all int in list
# print(random.permutation(lists)) # shuffle too  


# ----- UFUNC ----- #

# x = [1, 2, 3, 4]
# y = [5, 6, 7, 8]
# z = [2, 4, 6, 8]

# result = [i + j for i, j in zip(x, y)] # looping more than 1 list
# print(numpy.add(x, y)) # sum 2 list | int

# print(numpy.subtract(y, x)) # minus list | int

# print(numpy.multiply(x, y)) # multiply list | int

# print(numpy.divide(2, 2)) # divide list | int

# print(numpy.power(2, 3)) # 2 ** 3 list | int

# print(numpy.mod(2, 5)) # modulo % list | int 
# print(numpy.remainder(2, 5)) # modulo % list | int 

# print(numpy.divmod([2, 4, 6, 8], [2, 2, 2, 2])) # divide each item on index

# print(numpy.absolute([-1, -2, -3, -4])) # remove - in list

# myFunc = lambda a, b: numpy.add(a, b)
# result = numpy.frompyfunc(myFunc, 2, 1) # create own function
# print(result(x, y))

# print(type(numpy.add)) # check type function

# print(numpy.trunc([-2.5550, 3.211])) # remove dot in item | float
# print(numpy.fix(-1.0001)) # remove dot in item | float

# print(numpy.around(2.6)) # round list | float
# print(numpy.floor([2.5, 1.2])) # floor list | float
# print(numpy.ceil([2.1, 3.5])) # ceil list | float

# print(numpy.log(x))
# print(numpy.log2(x))
# print(numpy.log10(x))

