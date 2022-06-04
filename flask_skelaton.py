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
        customerId = request.args.get("id")
        return ("selected a customer " + customerId) 
    else:
        return("Customer ID not found")

@app.route('/films')
def requestFilmsAvailable():
   return "list of avilable films"
   
@app.route('/film')
def requestFilmData():
    if("id" in request.args):
        filmId = request.args.get("id")
        return("selected a film " + filmId) 
    else:
        return("Film ID not found")
   

if __name__ == '__main__':
   app.run()