import numpy as np

arr1= np.array([1,2,0,0,4,0])
indices= np.nonzero(arr1)
print(indices)

arr=np.array([1,2,3,4,5,6,7,8,9])
arr[arr%2==1]=3
print(arr)

arr2= np.array([[1,2],[3,4]])
arr3=np.array([[6,7],[8,9]])
print(np.vstack([arr2,arr3]))
print(np.hstack([arr2,arr3]))
 ########

arr1= np.array([10,20,30,40,50])
print(arr1)

arr2= np.arange(9)
print(arr2.reshape(3,3))

arr3= np.eye(5,5)
print(arr3)

arr4= np.random.randint(0,1,(4,4))
print(arr4)

arr5=np.zeros(10)
print(arr5)

arr6=np.ones(10)
print(arr6)

arr7=np.ones(10)
print(arr7*5)
