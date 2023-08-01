#Function without name is k/n Lambda Function

f=lambda a: a*a*a
result=f(5)
print("Lambda Function: ",result)

"""
f=lambda a:a**2
result=f(10)
print(result)
"""
from functools import reduce

# filter function using lambda
num=[0,1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,num))
print("Filter function: ",evens)

double=list(map(lambda n:n*2,evens))
print("Map Function: ",double)

answer=reduce(lambda a,b:a+b, evens)
print("Rduce Function: ",answer)

