import numpy as np
arr1=np.array([1,2,3,4])

print(arr1)

arr2=np.array([[1,22,3,4,5],[2,4,8,9,7]])
print(arr2)

# array of zeros
arr3=np.zeros((3,4))
print(arr3)

# array of ones
arr4=np.ones((2,3))
print(arr4)

# array with range of value
arr5=np.arange(0,10,3) 
print(arr5)
# array with evenly spaced value
arr6=np.linspace(0,1,5) # five value from zero to one
print(arr6)

# identity matrix
arr7=np.eye(3)


print(arr7)
# random arrays
arr8=np.random.rand(3,3)
print(arr8)
arr9=np.random.randint(0,10,(3,3))
print(arr9)
# array atributes 
import numpy as np

arr=np.array([[1,2,3],[6,7,8]])

print(arr.shape)# define array dimension 
 
print(arr.ndim) # dimension

print(arr.size)# totl number of element

print(arr.dtype)# int data type

print(arr.itemsize)# size of each element in bites


arr1=np.array([10,20,30,40])
print(arr1[0])
print(arr1[-1])
print(arr1[1:4])

print(arr1[:3])
print(arr1[2:])

#boolean indexing
print(arr1[arr1<20])
print(arr1[arr1>20])
