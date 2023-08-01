"""
a =10
if (a==10):
    print("I am in if statement")
print("Im not in if statement")
"""

"""
str="yash yeole"
for i in str:
    print(i,end="")


fruits=["apple","mango","grapes","guava"]       #zip() function perfrom two list in  parallal way
color=["red","yellow","green","blue"]
for fruits,color in zip(fruits,color):
    print(f"{fruits} is {color}")


str="GeeksforGeeks"
for letter in str:
    if letter=="e" or letter=="s":
        continue
    print("Current letter: ",letter)


str="geeksforgeeks"
for i in str:
    pass
print("last letter: ",i)

sum=0
for i in range(1,10):
    print(i,end=" ")
    sum=sum+i
print()
print("Sum of first 10 numbers: ",sum)



a = int(input('Enter a number (-1 to quit): '))
while a != -1:
    a = int(input('Enter a number (-1 to quit): '))

def add(num1=0, num2=0):
    return num1+num2
print(add(3,2))     

# Python code to illustrate the cube of a number
# using lambda function
def cube(x): return x**2
cube_v2 = lambda x : x*x*x
print(cube(7))
print(cube_v2(7))


list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = []
for item in list1:
    list2.append(item)

print(list2)

#swap  1st and last element
def swap(list1):
    list1[0],list1[-1]=list1[-1],list1[0]
    return list1
list1=[1,2,3,4,5]
print(swap(list1))

#naive method
count=0
for i in list1:
    count+=1
print(count)

a=[]
a.append(10)
a.append("hfdkaj")
print(a)

"""

#reverssed string
str="yash yeole"
s=str.split()[::-1]
l=[]
for i in s:
    l.append(i)
print(" ".join(l))