from application import api, mongo
from flask import Blueprint , jsonify, make_response , request
from flask_restful import Resource
import uuid
import time
import bcrypt

User = Blueprint("user", __name__)  # create Blueprint
users_collection = mongo['users_collection']

#Add user and get all user
class Register(Resource):
    def get(self):
        all_users_data = list(users_collection.find({}, {"_id": 0, "password": 0}))
        if all_users_data:
                    return all_users_data
    def post(self):
        try:
            data = request.json
            password = data["password"].encode()
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(12))
            data["user_id"] = str(uuid.uuid4().hex)[:10] + str(round(time.time()))
            data["password"] = hashed_password
            users_collection.insert_one(data)
            return jsonify({'message': 'User created', 'user_id': data["user_id"]}), 201
        except Exception as e:
            return make_response(
                jsonify(
                    {
                        "message": "Something went wrong",
                        "Exception": str(e),
                    }
                ),
                500,
            )
class Update(Resource):
    def get(self , user_id = None):
        try:
            
            if user_id:
                user_data = users_collection.find_one({"user_id": user_id}, {"_id": 0, "password": 0})

                if user_data:
                    return jsonify(user_data), 200
                else:
                    return make_response(jsonify({"message": "User not found"}), 404)
            
        except Exception as e:
            return make_response(jsonify({"message": "Something went wrong", "Exception": str(e)}), 500)
        
    
        
    def put(self, user_id=None):
        if user_id is None:
            return make_response(jsonify({"message": "User_id can not empty"}), 403)            
        data = request.json
        result = users_collection.update_one({'user_id': user_id}, {'$set': data})
        if result.modified_count > 0:
            return jsonify({'message': 'User updated'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    def delete(self , user_id = None):
        result = users_collection.delete_one({'user_id': user_id})
        if result.deleted_count > 0:
            return jsonify({'message': 'User deleted'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404


api.add_resource(Update, "/users/<string:user_id>")
api.add_resource(Register , "/users")