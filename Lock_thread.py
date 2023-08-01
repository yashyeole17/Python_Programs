
from threading import *
from time import *

mylock =Lock()
def task(mylock, msg):
    mylock.acquire()
    for i in range(5):
        print(msg)
    sleep(3)
    mylock.release()

t1 = Thread(target = task, args =(mylock, "Hello"))
t2 = Thread(target = task, args =(mylock, "Welcome"))
t1.start()
t2.start()


