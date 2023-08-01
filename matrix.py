from numpy import *
arr1=array([
            [1,2,3],
            [6,5,7]
            ])
#print(arr1)
#print(arr1.dtype)
#print(arr1.ndim)
#print(arr1.shape)
#print(arr1.size)

arr2=arr1.reshape(3,2)
#print(arr2)

arr5=array([
            [1,2,3,4,5,6],
            [7,8,9,10,11,12]
        ])
#print(arr5)
#print()
arr7=arr5.reshape(3,2,2)
#print(arr7

a1=matrix('1, 2, 3, 4 ; 5, 6, 7, 8')
#print(a1)
print()
a2=matrix('1,2; 3,4; 5,6; 7,8')
#print(a2)


a11=matrix('1,2,3; 4,5,6')
a22=matrix('6,5,4; 3,2,1')
a33=a11+a22
print(a33)
