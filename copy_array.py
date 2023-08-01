from numpy import *
arr1=array([1,2,3,4,5,6])
arr2=array([5,8,9,7,1,4])

#print(arr1)
#print(arr2)
arr3=arr1+5
#print("modify arr1",arr3)

arr4=arr1+arr2
#print("addition",arr4)

#print("concatination: ",concatenate((arr1,arr2)))


arr4=array([1,8,2,3,3,4,9,4,5])
#print(sin(arr4))
#print(log(arr4))
#print(sqrt(arr4))
#print(square(arr4))
#print(pow(arr4,3))
#print(pow(arr4,4))
#print(sum(arr4))
#print(min(arr4))
#print(max(arr4))
#print(sort(arr4))
#print(unique(arr4))


a1=array([1,2,3,4,5,6])
a2=a1
print("1",a1)
print("2",a2)
print("1",id(a1))
print("2",id(a2))
print()
a3=a1.copy()   #location id will be change
a1[1]=7
print("1",a1)
print("3",a3)
print("1",id(a1))
print("3",id(a3))




