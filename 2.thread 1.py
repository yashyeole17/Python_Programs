#Write A program to demonstrate:
#A. Creating a Thread without using any class
# B. Creating a Thread by extending Thread class
# C. Creating a Thread without extending Thread class
# D. Use of getname(), setname(),isalive(), Join(),enumerate() etc.
# E. Deamon Thread.

'''
# thread without using a class

from threading import *
def display():
    for i in range(0,3):
        print("Child Thread")

t = Thread(target=display)    #Creating Thread Object
t.start()
for _ in range(0,10):
    print("Main Thread")
'''

"""
#thread by extending the thread class
from threading import *
class Test(Thread):
     def run(self):
         for _ in range(0,3):
             print("Child Thread")

t= Test()
t.start()
for _ in range(0,10):
    print("Main Thread")
"""


"""
# Thread without extending the thread class
from threading import *
class Temp:
     def display(self):
        for i in range(1,5):
            print(i)
t1=Temp()
t=Thread(target=t1.display)
t.start()
for _ in range(0,10):
     print("Child Thread")
print(current_thread().getName())
current_thread().setName("YY")

""""""
from threading import *
def fun():
     for i in range(1,5):
        print(i)

t = Thread(target=fun)      # Creating Thread Object
print(t.is_alive())
th = current_thread().name
 print(th)
""""""

"""
"""
import gc
gc.isenabled()
for x in enumerate():
    print(x.name)

"""


import time
from threading import *
def thread_1():
    for i in range(5):
        print('this is thread T')
        time.sleep(1)

T = Thread(target = thread_1)
T.setDaemon(True)
T.start()
time.sleep(5)
print('this is Main Thread')

