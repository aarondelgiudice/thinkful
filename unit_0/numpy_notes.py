import numpy as np

list_test = ['hello', 'world']

np_test = np.array(list_test)
print(np_test)
print(type(np_test))

x = np.array([0,1,2,3,4,5,6,7])
print(x)
#create an array range 0-7 or range(8)

x_list = list(range(8))
print(x_list)
x_to_array = np.array(x_list)
prrint(x_to_array)
#create the same as above, an array range(8)

x = np.arange(8)
print(x)
#create the same as above, an array range(8)
#arange() is abbreviated for "array range"

x = x.reshape(2,4)
print(x)
#all previous arrays were 1*8, or 1 line by 8 columns
#reshape will convert x to a 2*4 array, 2 rows by 4 columns

#element-wise vs aggregator functions
#numpy math functions can either return results for each element or the aggregate
#element-wise functons will be performed on and return each element of the array
#aggregator functions will be performed on the entire array and return a single value

x = np.arange(8).reshape(2,4)
print(np.square(x))
#square every value of an array
print(np.sqrt(x))
#get the square root of every value of an array
#these are element-wise functions
#the function will transform every value of the array
#and return an array of the same dimensions

x = np.arange(8).reshape(2,4)
print(np.max(x)) #return maximum value of array
print(np.min(x)) #return min value of array
print(np.mean(x)) #return mean value of array
print(np.std(x)) #return the standard deviation of values of array
#these are aggregator functions and only return a singlue value

