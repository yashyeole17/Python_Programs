'''
def greet():
    print("Hello")
    print("Good Morning")
greet()
'''


'''
def add(x,y):
    print(x+y)
add(4,5)
'''

'''
def add_sub(x1,x2):
    add=x1+x2
    sub=x1-x2
    return add, sub
result1, result2 = add_sub(5,4)
print("addition: ",result1)
print("Subtraction: ",result2)
'''

'''
def update(x):
    x=8
    print("X: ",x)
    print(id(x)," :X")
a=19
update(a)
print("a: ",a)
print(id(a)," :A")


#factorial of No.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
answer=factorial(4)
print(answer)


#keyword variable length argument
def person(name,**data):
    print(name)
    print(data)
person('navin',age=28,city='mumbai', mob=14223243)



def person(name,**data):
    print(name)
    for i j in data.items():
        print(i,j)
person('navin',age=28,city='mumbai', mob=14223243)


a=10
def something(a):
    a=15
    print("in function: ",a)
something(14)
print("Outside: ",a)

'''
def even_odd(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
lst=[10,11,12,13,14,15,16]
ans1, ans2=even_odd(lst)
print(ans1," even")
print(ans2," odd")
