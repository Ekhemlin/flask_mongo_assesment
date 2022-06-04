import pymongo
import datetime


def get_rental_period(date1, date2):
    date1 = date1.split('.')[0]
    date2 = date2.split('.')[0]
    start_rental = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    end_rental = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    duration = end_rental - start_rental
    duration_days = duration.days
    duration_hours = divmod(duration.total_seconds(), 3600)[0]%24
    return({"days": duration_days, "hours" : duration_hours})

client = pymongo.MongoClient("mongodb+srv://eitan:eitan@cluster0.auufom8.mongodb.net/?retryWrites=true&w=majority")
mydb = client["imperva_db"]
customers = mydb["customers"]
myquery = { "_id": 1 }
customer = customers.find_one(myquery)
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
    rental_length = get_rental_period(rental["Rental Date"], rental["Return Date"])
    newObj = {"Film Title" : rental["Film Title"], "Rental Date" : rental["Rental Date"],
              "Cost" : sum_paid, "Rented For" : rental_length}
    rentals_list.append(newObj)

ret = {"info" : info, "rentals" : rentals_list}

print(ret)
# print(customer)
