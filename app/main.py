from flask import Flask, jsonify
from flask_sqlalchemy import sqlalchemy
from flask_marshmallow import Marshmallow
import json



app = Flask(__name__)

@app.route('/')
def hello_world():
    jsonString = """ "firstName": "Eric", 
                      "lastName": "Weitzman" """
    jsonVar1 = jsonify("hello", "world")
    jsonVar2 = jsonify(jsonString)
    return jsonString


@app.route('/test', methods=['get', 'post'])
def test():
    jsonVar3  = 'hello world'

    jsonVar4 = '''
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            },
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": null,
                "has_license": true
            }
        ]
    }
    '''
    #  loads: string -> json
    data = json.loads(jsonVar4)
    # to go back to string, dump : json -> string
    jsonData = json.dumps(data)

    # print(data)

    return data
