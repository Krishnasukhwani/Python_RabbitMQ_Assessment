import paho.mqtt.client as paho
import random
import time

MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
TOPIC = 'Status_topic'

client = paho.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)
try:
    while True:
        status = random.randint(0,6)
        message = {"status": status}
        client.publish(TOPIC, str(message))
        time.sleep(1)
        print("Press ctrl+c to stop client......!")
except KeyboardInterrupt:
    print("Stopping client......!")
    client.disconnect()
    
    
    


    