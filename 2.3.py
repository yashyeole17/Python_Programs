#3. An ABC company wants to perform the following tasks .
#A. Copy the contents of ‘FILE1.txt’ to ‘FILE2.txt’
#B. Count the number of lines, characters, special symbols for a given file.
"""
Write a python program using multithreading concept to perform above operations
simultaneously. Accept the filenames from user.
Also handle necessry exceptions.

( HINT : Thread_obj=Thread(target=Func_A , args=(FILE1, FILE2)) where Thread_obj
is thread object , Func_A is function to perform the specific task, FILE1, FILE2 are the
file names passed in the form of tuple as parameter to function.
"""

"""
# A

with open('file1.txt','r') as f:
    f1 = open('file2.txt','w')
    f1.writelines(f)
    print("DATA is copied")
    f1.close()





# B

from string import punctuation
special_symbol = set(punctuation)
with open('file1.txt','r') as f:
    char_len=0
    symbol=0
    file = f.read()
    line_len = len(file.split('\n'))
    for line in file:
        if '\n' in line:
            symbol+=1
        char_len+=len(line)
        for char in line:
            if char in special_symbol:
                symbol+=1

    print("Length:  ",line_len)
    print("Characters:  ",char_len)
    print("Symbols: ",symbol)

"""




# 3
from threading import *
from string import punctuation
def copy():
    try:
        with open('file1.txt', 'r') as f:
            f1 = open('file2.txt', 'w')
            f1.writelines(f)
            f1.close()
    except:
        print("Something Went Wrong")


def count():
    special_symbol = set(punctuation)
    try:
        with open('file1.txt', 'r') as f:
            char_len = 0
            symbol = 0
            file = f.read()
            line_len = len(file.split('\n'))
            for line in file:
                if '\n' in line:
                    symbol += 1
                char_len += len(line)
                for char in line:
                    if char in special_symbol:
                        symbol += 1
        print("Length of  file data :  ", line_len)
        print("Characters in file data:  ", char_len)
        print("Symbols in file data: ", symbol)
    except:
        print("Something Went Wrong")


t1 = Thread(target=copy)
t2 = Thread(target=count)
t1.start()
t2.start()
""""""