# 9. Write Python Program to Save Dictionary in Python Pickle.
import pickle
f = open('file1.txt','wb')
dict = { 1 : "AAA", 2 : "BBB", 3 : "CCC", 4 : "DDD"}
pickle.dump(dict,f)
print("Successful")