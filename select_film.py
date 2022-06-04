import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://eitan:eitan@cluster0.auufom8.mongodb.net/?retryWrites=true&w=majority")
mydb = client["imperva_db"]
customers_collection = mydb["customers"]
movies_collection = mydb["rentals"]
title = "CHAPLIN LICENSE"
renters = customers_collection.find_one({"Rentals" : {"$elemMatch" : {"Film Title" : title}}}, 
                                        {"First Name" : 1, "Last Name" : 1, "_id" : 1})
movie = movies_collection.find_one({"Title": title})
m_obj = {"Title" : movie["Title"], "Category" : movie["Category"], "id" : movie["_id"],
         "Rating" : movie["Rating"], "Description" : movie["Description"],
         "Rental Duration" : movie["Rental Duration"]}
print(m_obj)

print(renters)


