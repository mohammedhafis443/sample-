
#  boolean masking

import numpy as np

arr=np.array([1,2,3,4,5,6])
mask=arr>3
print(arr[mask])
# modifing value using boolean indexing
arr[arr>3]=0
print(arr)

#indexing

arr1=np.array([[1,2,3,4],[6,7,8,9]])
row=[0,1]
cols=[1,2]
print(arr1[row,cols])




#  reshaping

arr=np.arange(12)
print(arr.reshape(3,4)) # reshape 
print(arr.reshape(2,6))

# flatening

arr2=np.array([[1,2,3],[4,5,6]])
print(arr2.flatten())

# transpose
print(arr2.T)



# vertical horizontel 
arr1=np.array([[1,2],[4,5]])

arr2=np.array([[6,7],[8,9]])

print(np.concatenate([arr1,arr2],axis=1))

# vertical stacking & horizontal stacking 

arr3=np.array([[4,5],[6,8]])
arr4=np.array([[9,3],[5,7]])

print(np.vstack([arr3,arr4]))
print(np.hstack([arr3,arr4]))
# spliting
arr=np.arange(9)
print(np.split(arr,3))# spliting to 3 equal parts
