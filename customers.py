import pymongo
import datetime

def getAllCustomers(customers_collection):
    customers = customers_collection.find()
    retList = []
    for c in customers:
        c_obj = {"First Name" : c["First Name"], "Last Name" : c["Last Name"], "id" : c["_id"]}
        retList.append(c_obj)
    print(retList)
    return(retList)

