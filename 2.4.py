import time
from threading import *

I=RLock()
def factorial(n):
    I.acquire()
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    I.release()
    return result
def results(n):
    print("The factorial of ",n," is: ",factorial(n))
n1=int(input("Enter number 1 "))
n2=int(input("Enter number 2 "))
t1=Thread(target=results,args=(n1,))
t2=Thread(target=results,args=(n2,))
t1.start()
t2.start()