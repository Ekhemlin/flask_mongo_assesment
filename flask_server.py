import pymongo
from flask import Flask, request
import utils
import customers
import films
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

mongo_url = os.getenv('MONGO_URL')
if(not mongo_url):
    print("Please get the mongo URL from Eitan")

client = pymongo.MongoClient(mongo_url)
mydb = client["imperva_db"]
customers_collection = mydb["customers"]
movies_collection = mydb["rentals"]

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/customers')
def requestAllCustomer():
    try:
        customersList,status = customers.getAllCustomers(mydb)
        payload = utils.formatReturnPayload(status, customersList)
    except Exception as e:
        print(e)
        payload = utils.formatReturnPayload(status, "Customers could not be retrieved")
    finally:
        return(payload)

@app.route('/customer')
def requestCustomerData():
    if("id" in request.args):
        customerID = request.args.get("id")
        customer_body, status = customers.getCustomerWithId(mydb, customerID)
        payload = utils.formatReturnPayload(status, customer_body)
        return(payload) 
    else:
        payload = utils.formatReturnPayload(400, "Customer ID not found")
        return(payload)

@app.route('/films')
def requestFilmsAvailable():
    try:
        filmsList, status = films.getAllFilms(mydb)
        payload = utils.formatReturnPayload(status, filmsList)
    except Exception as e:
        print(e)
        payload = utils.formatReturnPayload(500, "Films could not be retrieved")
    finally:
        return(payload)
   
@app.route('/film')
def requestFilmData():
    if("id" in request.args):
        filmId = request.args.get("id")
        filmBody, status = films.getFilmWithID(mydb, filmId)
        payload = utils.formatReturnPayload(status, filmBody)
        return(payload) 
    else:
        payload = utils.formatReturnPayload(400,"Film ID not found")
        return(payload)
   

if __name__ == '__main__':
   app.run()