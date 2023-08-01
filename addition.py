"""

list1=[9,6,7,5,4,8,3,2,1]
max1=sorted(list1,reverse=True)
ans=max1[:5]
add=sum(ans)
print(ans)
print(add)

"""
"""
from datetime import time, date
print(date.today())
n = date.today()
print(n.year)
print(n.month)
print(n.day)
print("time",time(11,12,13))



a = "gOOd morNing"
print(a.upper())
print(a.title())

print(a.lower())


class A:
    name = "Yash"
    Age = 20
    def Display(self):
        print(self.name)
        print(self.Age)
class B(A):
    price= 20000
    def RR(self):
        print("$",self.price)
c=B()
c.Display()
c.RR()

"""
class Vehicle:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

class Car(Vehicle):
    def __init__(self,name):
        super().__init__(name)
        self.price = 30000
    def dis(self):
        print("Price: ",self.price)



c1 = Car("Yash")
c1.display()
c1.dis()