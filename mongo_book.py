from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["libary"]
collection=db["book"]
print("create successfully")
#insert books
documents=[
           {"title":"biology","auther":"jhon","year":2000},
           {"title":"chem","auther":"bob","year":2002},
           {"title":"math","autehr":"achu","year":2020}
           ]
re=collection.insert_many(documents)
print("insert successfully")
result=collection.update_one({'auther':'jhon'},{'$set':{'year':2020}})
print("update successfully")

for col in collection.find():
    print(col)
    
res=collection.delete_one({"name":"bob"})
print("delete successfully")


