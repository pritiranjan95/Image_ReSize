import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["Fixed_Dimension"]
collection=db["dimentions"]

# collection.insert_one({"name":"bapi"})