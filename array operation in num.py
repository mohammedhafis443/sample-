# array operations in numpy
import numpy as np

arr1=np.array([1,2,3,4])
arr2=np.array([10,20,30,40])

print(arr1+arr2)# addition
print(arr1-arr2) # subtraction
print(arr1*arr2)# multiplication 
print(arr1/arr2)# division
print(arr1**arr2)
print(np.sqrt(arr1))

print(arr1+5)
print(arr1*2)

# mathamatical function

print(np.sum(arr1)) # find sum
print(np.mean(arr1)) # find mean
print(np.median(arr1)) # find median
print(np.var(arr1)) # find variance 
print(np.min(arr1))# find min value 
print(np.argmin(arr1)) # index min
print(np.max(arr1))  # find max value 
print(np.argmax(arr1)) # find max index value 

print(np.exp(arr1))
print(np.log(arr1))

#  linear algebra 
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
# matrix product

print(np.dot(a,b))

# determinant

print(np.linalg.det(a))

# inverse
print(np.linalg.inv(a))

x=np.array([[3,2],[4,1]])
y=np.array([[6,8],[5,7]])

# copying in numpy
# assignment 
a1=np.array([1,2,3])
b1=a1
b1[0]=100
print(a1)
print(b1) 
# shallow copy 
a=np.array([1,2,3,4])
b=a.view()
b[1]=100
print(a)
print(b)
# deep copy 
x=np.array([1,2,3,4,5])
y=x.copy()
y[2]=100
print(x)
print(y)


