from flask import jsonify

def formatReturnPayload(status, body):
    ret = {"Status": status, "Body": body}
    json_ret = jsonify(ret)
    return(json_ret)
