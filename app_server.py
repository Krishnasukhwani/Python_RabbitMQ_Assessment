from flask import Flask, request, jsonify
from datetime import datetime
import pytz
from pymongo import MongoClient
from urllib.parse import quote_plus

app = Flask(__name__)

# MongoDB credentials
username = 'krishnasu'
password = 'Krishna@1998'
host = 'cluster0.m9dio8j.mongodb.net'
db_name = 'status_db'
collection_name = 'status_collection'
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)
MONGODB_URI = f'mongodb+srv://{encoded_username}:{encoded_password}@{host}/{db_name}?retryWrites=true&w=majority'
mongo_client = MongoClient(MONGODB_URI)
collection = mongo_client[db_name][collection_name]

@app.route('/status_counts', methods=['GET'])
def status_counts():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    if not start_time or not end_time:
        return jsonify({"error": "Please provide both start_time and end_time in ISO 8601 format"}), 400

    try:
        start_time = datetime.fromisoformat(start_time).astimezone(pytz.timezone('Asia/Kolkata'))
        end_time = datetime.fromisoformat(end_time).astimezone(pytz.timezone('Asia/Kolkata'))

        pipeline = [
            {"$match": {"timestamp": {"$gte": start_time, "$lte": end_time}}},
            {"$group": {"_id": "$status", "total": {"$sum": 1}}}
        ]
        results = list(collection.aggregate(pipeline))
        status_counts = {str(item['_id']): item['total'] for item in results}

        return jsonify(status_counts)
    except Exception as e:
        return jsonify({"error": f"Error processing request: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=5000)