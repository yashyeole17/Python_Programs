from time import sleep
from threading import Thread , RLock
I = RLock()

def factorial(n):
    I.acquire()
    if n == 1:
        return 1
    else:
        fact = n * factorial(n - 1)
    return fact
    sleep(4)
    I.release()

def square(n):
    I.acquire()
    square = n ** 2
    return square
    sleep(4)
    I.release()

def answer(n):
    print("Factorial: ", factorial(n))
    print("Square: ", square(n))

n = int(input("Enter No: "))
t1 = Thread(target = answer, args=(n,))
t1.start()