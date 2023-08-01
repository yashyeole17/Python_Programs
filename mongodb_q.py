"""

Write a pythan program to perform following operations. on MongoDB
Database. [5]
i) Create collection “EMP” with fields:
Emp-name, Emp- mobile, Emp, sal, Age
ii) Insert 5 documents.
iii) Find the employees getting salary between 5000 to 10000.
iv) Update mobile number for the employee named as “Riddhi”
v) Display all employees in the order of “Age”

"""
#i
from pymongo import *
client = MongoClient(host="mongodb://localhost:27017")
collection = client["yash"]["EMP"]

collection.create_index("Age")
"""
query = (
    {"Name":"AAA",     "Mobile":123 ,  "Salary":5000,  "ID":1, "Age":21},
    {"Name":"BBB",     "Mobile":124 ,  "Salary":6000,  "ID":2, "Age":22},
    {"Name":"Siddhi",  "Mobile":125 ,  "Salary":7000,  "ID":3, "Age":23},
    {"Name":"DDD" ,    "Mobile":126 ,  "Salary":8000,  "ID":4, "Age":25},
    {"Name":"EEE",     "Mobile":127 ,  "Salary":11000, "ID":5, "Age":25}
)

insert = collection.insert_many(query)

for record in collection.find():
    print(record)
"""

#ii
query = {"Salary":{"$gte":5000, "$lte":1000}}
for record in collection.find(query):
    print(record)