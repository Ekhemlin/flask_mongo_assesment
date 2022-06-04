from flask import jsonify
import datetime

def formatReturnPayload(status, body):
    ret = {"Status": status, "Body": body}
    json_ret = jsonify(ret)
    return(json_ret)

def get_rental_period(date1, date2):
    date1 = date1.split('.')[0]
    date2 = date2.split('.')[0]
    start_rental = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    end_rental = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    duration = end_rental - start_rental
    duration_days = duration.days
    duration_hours = divmod(duration.total_seconds(), 3600)[0]%24
    return({"days": duration_days, "hours" : duration_hours})