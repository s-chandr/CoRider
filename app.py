from flask import Flask, jsonify
from flask_restful import Api
from decouple import config
from pymongo import MongoClient
app = Flask(__name__)
app.config["MONGO_URI"] = config("DATABASE_URI")
api = Api(app)
mongo_client = MongoClient(app.config["MONGO_URI"])

mongo = mongo_client["coRider"] 


@app.route('/', methods=['GET'])
def ping():
    return jsonify({'Ping Hello !': 'World!'})

