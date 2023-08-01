
from threading import *
from time import *
rlock = RLock()

def get_first():
    rlock.acquire()
    print("Yash")
    rlock.release()

def get_second():
    rlock.acquire()
    print("Yeole")
    rlock.release()

def main():
    rlock.acquire()
    get_first()
    get_second()
    rlock.release()

t1 = Thread(target=main)
t1.start()