"""

n=int(input("Enter no"))
i=1
sum=0
while(i<=n):
    if(i%2==0):
        sum=sum+i
        print(sum)
    i=i+1





a = 8.6
b=2
print(a//b)


dict1 = {1 : "yash", 2 : "Yeole", 3 : "pune"}
print(dict1.values())
"""
'''
d1 = {"john": 40, "peter": 45}
d2 = {"yash": 444, "yeole": 45}
print(list(set(list(d1.keys())+list(d2.keys()))))


string1 = "YYttgYY"
if(string1==string1[::-1]):
    print("yes")
else:
    print("No")


def display(name,age):
    print("name: ",name)
    print("age: ",age)
    return
display(name="yash", age=45)

'''
"""
x=10
c = lambda x:x**2
print(c(x))


list1 =[10,20,30,40,50]
listIt = list1.__iter__()
list1 = listIt.__next__()
list2 = listIt.__next__()
list3 = listIt.__next__()
list4 = listIt.__next__()
print(list1)
print(list2)
print(list3)
print(list4)
print()

listA = [11,12,13,14,15]
listIt = iter(listA)
print(next(listIt))
print(next(listIt))
print(next(listIt))
print(next(listIt))
print(next(listIt))
print(next(listIt))

""" '''
class PowTwo:
    def __init__(self, max = 0):
        self.max= max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 3 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

n = PowTwo(5)
i = iter(n)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))



def no():
    yield 1
    yield 2
    yield 3
    yield 5
    yield 5
    yield 53
    yield 5
value = no()
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))

print()
print()
print()


def odd(n):
    for i in range(n):
        if i% 2 ==1:
            yield i
k = odd(10)
print(next(k))
print(next(k))
print(next(k))

'''
"""
def fibo(n):
    a,b=0,1
    if n==a:
        return a
    elif n==b:
        return b
    else:
        ans = []
        for i in range(n):
            ans.append(a)
            a,b = b, a+b
        return ans
no = 1
a = fibo(no)
print(a) 


# pipelining generator

def fibo (nums):
    x,y = 0,1
    for i in range(nums):
        x, y = y, x+y
        yield x
def square (nums):
    for n in nums:
        yield n**2
print(sum(square(fibo(4))))

"""

def smart_div(fun):
    def inner(a,b):
        print("Divide: ",a, " and ", b)
        if b == 0:
            a,b=b,a
        return fun(a,b)
    return inner
@smart_div
def div(a,b):
    print( a/b)
div(0,1)