from pymongo import *
client = MongoClient(host="mongodb://localhost:27017")
collection = client['yash']['yashha']

#INSERT the DATA
"""
first = ({ "Name":"111", "Age":20 })
second = ({ "Name":"112", "Age":21 })
collection.insert_one(first)
collection.insert_one(second)


all = (
    {"Name" : "DDD", "Age":22},
    {"Name" : "EEE", "Age":23},
    {"Name" : "FFF", "Age":24}
)

collection.insert_many(all)
for record in collection.find():
    print(record)


for record in collection.find({}, {"Name":"DDD"}):
    print(record)

"""

'''
# UODATING the DATA
query = { "$set": {"Name":"YYY", "Age":99}}
update = collection.update_one({"Name":"FFF"},query)

for record in collection.find():
    print(record)


'''
"""
#DELETE the data
delete = collection.delete_one({"Name":"ZZZ"})

for record in collection.find():
    print(record)
"""










