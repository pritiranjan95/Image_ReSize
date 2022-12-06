from Repository.database import collection
from bson.json_util import dumps
import json

def add(data):
    a=collection.insert_one(data.dict())
    return "Successfully added"

def show():                       #Not giving parameter as we are finding all the data. 
    a=dumps(collection.find())    #Get the Bson data from database and "dumps" convert it to readable string. And this will show all the data inside the database
    a=json.loads(a)               #Changed the string to json again.
    return a
