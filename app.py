from flask import Flask, jsonify, request
from decouple import config
from pymongo import MongoClient


app = Flask(__name__)
app.config["MONGO_URI"] = config("DATABASE_URI")
mongo_client = MongoClient(app.config["MONGO_URI"])

mongo = mongo_client["project"] 
likes = mongo['likes']

# Placeholder function for sending push notification
def send_push_notification(user_id):
    # Placeholder code for sending a push notification
    print(f"Sending push notification to user {user_id}: You have reached 100 likes!")

@app.route('/like', methods=['POST'])
def store_like_event():
    data = request.get_json()
    user_id = data.get('user_id')
    content_id = data.get('content_id')

    if user_id and content_id:
        likes.insert_one({'user_id': user_id, 'content_id': content_id})
        # Check if user has reached 100 likes
        like_count = len(list(likes.find({'user_id': user_id})))
        print(like_count)
        if like_count == 11:
            send_push_notification(user_id)
        return jsonify({'message': 'Like event stored successfully'})
    else:
        return jsonify({'error': 'Invalid data provided'})

@app.route('/like/check', methods=['POST'])
def check_like():
    data = request.get_json()
    user_id = data.get('user_id')
    content_id = data.get('content_id')

    if user_id and content_id:
        like = likes.find_one({'user_id': user_id, 'content_id': content_id})
        
        if like:
            return jsonify({'liked': True})
        else:
            return jsonify({'liked': False})
    else:
        return jsonify({'error': 'Invalid data provided'})

# Total likes for a content
@app.route('/like/total', methods=['POST'])
def total_likes():
    data = request.get_json()
    content_id = data.get('content_id')

    if content_id:
        count = likes.count_documents({'content_id': content_id})
        return jsonify({'total_likes': count})
    else:
        return jsonify({'error': 'Invalid data provided'})


@app.route('/', methods=['GET'])
def ping():
    return jsonify({'Ping Hello !': 'World!'})


if __name__ == '__main__':
    app.run( host="0.0.0.0" , port = int("3000") , debug=True)
