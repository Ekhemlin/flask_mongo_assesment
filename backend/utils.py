import flask
from flask import jsonify, make_response
import datetime

def formatReturnPayload(status, body):
    ret = {"Status": status, "Body": body}
    json_ret = jsonify(ret)
    resp = flask.make_response(json_ret)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print(resp)
    return resp

    # return(json_ret)

def get_rental_period(date1, date2):
    if(not date1 or not date2):
        return({"days": None, "hours" : None})
    date1 = date1.split('.')[0]
    date2 = date2.split('.')[0]
    start_rental = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    end_rental = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    duration = end_rental - start_rental
    duration_days = duration.days
    duration_hours = divmod(duration.total_seconds(), 3600)[0]%24
    return({"days": duration_days, "hours" : duration_hours})