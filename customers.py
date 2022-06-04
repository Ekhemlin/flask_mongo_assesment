import pymongo
import datetime
import utils

def getAllCustomers(customers_collection):
    customers = customers_collection.find()
    retList = []
    for c in customers:
        c_obj = {"First Name" : c["First Name"], "Last Name" : c["Last Name"], "id" : c["_id"]}
        retList.append(c_obj)
    print(retList)
    return(retList)


def getCustomerWithId(client, customerId):
    customers_collection = client["customers"]
    movies_collection = client["rentals"]
    myquery = { "_id": customerId }
    try:
        myquery = { "_id":  int(customerId) }
        customer = customers_collection.find_one(myquery)
        if customer is None:
            return("customer not found", 400)
        print(customer)
        info = {"First Name" : customer["First Name"], "Last Name" : customer["Last Name"], 
            "Address" : customer["Address"], "City" : customer["City"], "Country" : customer["Country"], 
            "District" : customer["District"], "Phone" : customer["Phone"]}
        rentals_json = customer["Rentals"]
        rentals_list = []
        for i in range(len(rentals_json)):
            rental = rentals_json[i]
            payments = rentals_json[i]["Payments"]
            sum_paid = 0.0
            for p in range(len(payments)):
                payment = payments[p]
                sum_paid += payment["Amount"]
            rental_length = utils.get_rental_period(rental["Rental Date"], rental["Return Date"])
            newObj = {"Film Title" : rental["Film Title"], "Rental Date" : rental["Rental Date"],
                      "Cost" : sum_paid, "Rented For" : rental_length}
            rentals_list.append(newObj)
        ret = {"info" : info, "rentals" : rentals_list}
        return(ret, 200)
    except Exception as e:
        print(e)
        return("Customer could not be retrieved", 500) #return status code from here
