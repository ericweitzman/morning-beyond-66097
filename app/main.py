from flask import Flask
from flask_sqlalchemy import sqlalchemy
from flask_marshmallow import Marshmallow



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world! Eric!'