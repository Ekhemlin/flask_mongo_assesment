import pymongo
import datetime

def getAllFilms(movies_collection):
    movies = movies_collection.find()
    retList = []
    for m in movies:
        m_obj = {"Title" : m["Title"], "Category" : m["Category"], "id" : m["_id"],
                "Rating" : m["Rating"], "Description" : m["Description"], "Rental Duration": m["Rental Duration"]}
        retList.append(m_obj)
    return(retList)
