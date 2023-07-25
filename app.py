from flask import Flask, jsonify, request
from decouple import config
from pymongo import MongoClient
import uuid
import time
import bcrypt
app = Flask(__name__)
app.config["MONGO_URI"] = config("DATABASE_URI")
mongo_client = MongoClient(app.config["MONGO_URI"])

mongo = mongo_client["coRider"] 
users_collection = mongo['users_collection']

@app.route('/users', methods=['GET'])
def get_all_users():
    users = list(users_collection.find({}, { 'password': 0, '_id':0}))  # Excluding passwords from the response
    return users

@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = users_collection.find_one({'user_id': user_id}, {'password': 0, '_id':0})
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    password = data["password"].encode()
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(12))
    data["user_id"] = str(uuid.uuid4().hex)[:10] + str(round(time.time()))
    data["password"] = hashed_password
    users_collection.insert_one(data)
    return jsonify({'message': 'User created', 'user_id': data["user_id"]}), 201

@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    result = users_collection.update_one({'user_id': user_id}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': 'User updated'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = users_collection.delete_one({'user_id': user_id})
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404


@app.route('/', methods=['GET'])
def ping():
    return jsonify({'Ping Hello !': 'World!'})


if __name__ == '__main__':
    app.run( host="0.0.0.0" , port = int("3000") , debug=True)
