import pymongo
import datetime
import customers

def getAllFilms(client):
    try:
        movies_collection = client["rentals"]
        movies = movies_collection.find()
        retList = []
        for m in movies:
            m_obj = {"Title" : m["Title"], "Category" : m["Category"], "id" : m["_id"],
                    "Rating" : m["Rating"], "Description" : m["Description"], "Rental Duration": m["Rental Duration"]}
            retList.append(m_obj)
        return(retList, 200)
    except Exception as e:
        print(e)
        return("Films could not be retrieved", 500)

def getFilmWithID(client, filmID):
    movies_collection = client["rentals"]
    try:
        movie = movies_collection.find_one({"_id": int(filmID)})
        if(movie is None):
            return("Movie not found", 400)
        renters = customers._getRentersForFilmTitle(client, movie["Title"])
        m_obj = {"Title" : movie["Title"], "Category" : movie["Category"], "id" : movie["_id"],
            "Rating" : movie["Rating"], "Description" : movie["Description"], "Renters" : renters,
            "Rental Duration" : movie["Rental Duration"]}
        return(m_obj, 200)
    except Exception as e:
        print(e)
        return("Could not retrieve movie", 500)


