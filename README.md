# Python_RabbitMQ_Assessment

# Status Counts API and MQTT Publisher/Subscriber

## Description

The **Status Counts API** is a Flask-based web application that interacts with a MongoDB database to retrieve status counts based on a specified time range. Additionally, the **MQTT Publisher** and **MQTT Subscriber** are simple clients that publish and subscribe to random status messages via MQTT.

## Features

- **Status Counts API**: Retrieve status counts from a MongoDB collection based on a specified time range.
- **MQTT Publisher**: Publish random status messages to an MQTT topic.
- **MQTT Subscriber**: Subscribe to an MQTT topic and save incoming messages to a MongoDB collection.
- Flexible date input in ISO 8601 format for the API.
- Timezone support for accurate date handling.

## Files

1. **app.py**: The main Flask application that defines the API endpoint and handles requests to retrieve status counts from the MongoDB database.
2. **mqtt_publisher.py**: A simple MQTT client that publishes random status messages to a specified topic.
3. **mqtt_subscriber.py**: A simple MQTT client that subscribes to a specified topic and saves received messages to a MongoDB collection.

## Prerequisites

Before running the applications, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## create virtual env
python -m venv "anyname"
## activate virtual env
name\script\activate

## Dependencies

Install the required Python packages using pip:

```bash
pip install Flask pymongo pytz python-dateutil paho-mqtt

## you can install it usng the requirements.txt file
```bash
pip install -r requirements.txt

#Important installations(visit official website)
Make sure to install RabbitMQ and Erlang
# enable important plugins(do this in rabbitmq command prompt)
rabbitmq-plugins enable rabbitmq_mqtt
rabbitmq-plugins enable rabbitmq_management
#Check if it is enabled
rabbitmq-plugins list


# Setup Instructions
# For Status Counts API
Clone the Repository (if applicable):
bash
git clone <repository-url>
cd <repository-directory>

# Configure MongoDB Credentials:
# Update the MongoDB credentials in app.py:
# python
username = 'your_username'
password = 'your_password'
host = 'your_mongodb_host'
db_name = 'your_database_name'
collection_name = 'your_collection_name'

Run the Application:
bash
python app.py
The application will start running on http://localhost:5000.

# RUN the MQTT Client and server script in two different terminals
python mqtt_client.py
python mqtt_server.py