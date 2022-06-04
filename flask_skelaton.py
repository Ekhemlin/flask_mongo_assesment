import utils
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
   return "Hello World"


@app.route('/customers')
def requestAllCustomer():
   return "All customers"


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
   return "list of avilable films"
   
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