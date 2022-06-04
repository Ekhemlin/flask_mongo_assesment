import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://eitan:eitan@cluster0.auufom8.mongodb.net/?retryWrites=true&w=majority")
mydb = client["imperva_db"]
movies_collection = mydb["rentals"]
movies = movies_collection.find()
retList = []
for m in movies:
    m_obj = {"Title" : m["Title"], "Category" : m["Category"], "id" : m["_id"],
             "Rating" : m["Rating"], "Description" : m["Description"], "Rental Duration": m["Rental Duration"]}
    retList.append(m_obj)
print(retList)

