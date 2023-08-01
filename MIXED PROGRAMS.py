import re
"""

def validate_pass(password):
    if len(password)>8 or len(password)<20:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[$#@*]", password):
        return False
    return True

password = "Welcome@123"
if validate_pass(password):
    print("Yes")
else:
    print("No")
"""

import numpy as np
array = np.array([
    [1,2,3,4],
    [11,12,13,14],
    [21,22,23,24],
    [51,42,53,43],
    [41,52,43,55]
])
mean = np.mean(array,axis=0)
max1 = np.max(array,axis=0)
min2 = np.min(array,axis=0)
sum3 = np.sum(array,axis=0)
print("mean: ",mean)
print("max: ",max1)
print("min: ",min2)
print("sum: ",sum3)

"""

import numpy as np
a1 = np.array([ [1,2,3],[4,5,6] ])
a2 = np.array([ [11,12,13],[ 14,15,16] ])

print("Addition:")
print(a1+a2)

print("multiplication")
print(a1*a2)

scalar = 2
print("Scalar mul A")
print(a1*scalar)

print("Scalar mul B")
print(a2*scalar)

print("Transpose A")
print(a1.T)
print("Transpose B")
print(a2.T)




#overloading
class Student:
    def __init__(self,m1,m2,m3):
        self.a = m1
        self.b = m2
        self.c = m3

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a!= None and b != None and c != None:
            s=a+b+c
        elif a != None and b != None :
            s = a + b
        else:
            s=a
        return s
s1 = Student(0,0,0)
print(s1.sum(1,2,3))
print(s1.sum(1,2))
print(s1.sum(1))


from time import sleep
from threading import Thread

class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(0.1)
class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(0.1)
t1 = Hello()
t2 = Hi()
t1.start()
t2.start()
t1.join()
t2.join()
print("BYE")
"""


"""
from threading import Thread
from time import sleep, time
def run():
    for i in range(10):
        print("HII")
        sleep(0.2)
s= time()
t1 = Thread(target=run)
t1.start()
sleep(4)
print("BYE")
e =time()
print("Time: ",e-s)



from threading import Thread, Lock
from time import time,sleep
mylock = Lock()
def fun(mylock, msg):
    mylock.acquire()
    for i in range(8):
        print(msg)
    sleep(2)
    mylock.release()
t1 = Thread(target=fun, args=(mylock, "Hello"))
t2 = Thread(target=fun, args=(mylock, "HIII"))
t1.start()
t2.start()
t1.join()
t2.join()
print("BYE")



from threading import Thread, RLock
from time import sleep
rlock= RLock()
def first():
    rlock.acquire()
    for i in range(5):
        print("Yash")
    sleep(4)
    rlock.release()
def second():
    rlock.acquire()
    for i in range(5):
        print("Yeole")
    sleep(2)
    rlock.release()
def main():
    rlock.acquire()
    first()
    second()
    rlock.release()

t1 = Thread(target=main)
t1.start()
sleep(3)
print("BYE")



from threading import Thread, Semaphore
from time import sleep
ob  = Semaphore(2)

def display(name):
    ob.acquire()
    for i in range(5):
        print("Hello")
        print(name)
    ob.release()

t1 = Thread(target=display, args=("Thread-1",))
t2 = Thread(target=display, args=("Thread-2",))
t3 = Thread(target=display, args=("Thread-3",))
t4 = Thread(target=display, args=("Thread-4",))

t1.start()
t2.start()
t3.start()
t4.start()

"""