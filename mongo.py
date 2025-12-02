from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["company"]
collection=db["mycollection"]
print("connect to mongoDB successfully")
document=({"name":"alice","role":"manager","salery":10000})
collection.insert_one(document)
print("insert successfully")
for col in collection.find():
    print(col)




