import pika
from pymongo.mongo_client import MongoClient
import json
from datetime import datetime, timezone


RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = 'status_queue'
# mongodb url
MONGODB_URI = 'mongodb+srv://krishnasu:<password>@cluster0.m9dio8j.mongodb.net/'
MONGODB_DB = 'status_db'
MONGODB_COLLECTION = 'status_collection'

mongo_client = MongoClient(MONGODB_URI)
collection = mongo_client[MONGODB_DB][MONGODB_COLLECTION]

connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel =connection.channel()

channel.queue_declare(queue=RABBITMQ_QUEUE)

def callback(ch, method, properties, body):
    message = json.loads(body.decode('utf-8'))
    message['timestamp']= datetime.now(timezone.utc)
    collection.insert_one(message)
    print(f"Message saved to collection: {message}")
    
channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)
print("Waiting for new messages. To exit press CTRL+C")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    connection.close()
   
    