import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
from datetime import datetime
import pytz
from urllib.parse import quote_plus

# Configuration
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'Status_topic'
IST = pytz.timezone('Asia/Kolkata')

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

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    if msg:
        message = msg.payload.decode('utf-8')
        print(f"Message received: {message}")
        message = json.loads(message)
        timestamp = datetime.now(pytz.utc).astimezone(IST).isoformat()
        message['timestamp'] = timestamp
        collection.insert_one(message)
        print(f"Message saved to collection: {message}")

try:
    while True:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_forever()
        print("Press CTRL+C to stop/exit the server")
except KeyboardInterrupt:
    print("Stopping Server......!")
    client.disconnect()
