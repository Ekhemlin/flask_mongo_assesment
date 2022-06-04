import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://eitan:eitan@cluster0.auufom8.mongodb.net/?retryWrites=true&w=majority")
mydb = client["imperva_db"]
customers_collection = mydb["customers"]
customers = customers_collection.find()
retList = []
for c in customers:
    c_obj = {"First Name" : c["First Name"], "Last Name" : c["Last Name"], "id" : c["_id"]}
    retList.append(c_obj)
print(retList)

