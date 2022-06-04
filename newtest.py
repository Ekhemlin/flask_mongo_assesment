from flask import Flask, jsonify, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://eitan:eitan@cluster0.auufom8.mongodb.net/?retryWrites=true&w=majority")
mydb = client["imperva_db"]
customers = mydb["customers"]


def foramtResponse(status, body):
    ret = {"status" : status, "body" : body}
    return(jsonify(ret))


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    # return foramtResponse(200, {"data" : "response"})


# @app.route("/customer")
# def getCustomerWithID():
#     id = request.args.get("id") 
#     myquery = { "_id": int(id) }
#     customer = customers.find_one(myquery)
#     if(customer):
#         name = customer["First Name"]
#         return(foramtResponse(200, name))


if __name__ == "__main__":
    app.run(debug=True)

    

