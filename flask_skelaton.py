import pymongo
from flask import Flask, request
import utils
import customers
import filmsRequest

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://eitan:eitan@cluster0.auufom8.mongodb.net/?retryWrites=true&w=majority")
mydb = client["imperva_db"]
customers_collection = mydb["customers"]
movies_collection = mydb["rentals"]

@app.route('/')
def hello_world():
   return "Hello World"


@app.route('/customers')
def requestAllCustomer():
    try:
        customersList = customers.getAllCustomers(customers_collection)
        payload = utils.formatReturnPayload(200, customersList)
    except Exception as e:
        print(e)
        payload = utils.formatReturnPayload(500, "Customers could not be retrieved")
    finally:
        return(payload)

@app.route('/customer')
def requestCustomerData():
    if("id" in request.args):
        customerID = request.args.get("id")
        payload = utils.formatReturnPayload(200, "selected a customer " + customerID)
        return(payload) 
    else:
        payload = utils.formatReturnPayload(400, "Customer ID not found")
        return(payload)

@app.route('/films')
def requestFilmsAvailable():
    try:
        filmsList = filmsRequest.getAllFilms(movies_collection)
        payload = utils.formatReturnPayload(200, filmsList)
    except Exception as e:
        print(e)
        payload = utils.formatReturnPayload(500, "Films could not be retrieved")
    finally:
        return(payload)
   
@app.route('/film')
def requestFilmData():
    if("id" in request.args):
        filmId = request.args.get("id")
        payload = utils.formatReturnPayload(200, "selected a film " + filmId)
        return(payload) 
    else:
        payload = utils.formatReturnPayload(400,"Film ID not found")
        return(payload)
   

if __name__ == '__main__':
   app.run()