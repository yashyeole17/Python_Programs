from threading import *
import time

n=int(input("Enter n "))
obj=Semaphore(n)
def show(the_name):
    obj.acquire()
    for i in range(5):
        print("This is Python practical ")
        time.sleep(1)
        print(the_name)
        obj.release()

t1=Thread(target=show,args=("Thread 1",))
t2=Thread(target=show,args=("Thread 2",))
t3=Thread(target=show,args=("Thread 3",))
t1.start()
t2.start()
t3.start()