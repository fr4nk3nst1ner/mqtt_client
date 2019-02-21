import paho.mqtt.client as paho
import ssl
import time
broker="<exact_broker_FQDN>"
port=8883

def on_connect(client, userdata, flags, rc):
  client.subscribe('#', qos = 1)        # Subscribe to all topics
  client.subscribe('$SYS/#')            # Broker Status (Mosquitto)

def on_log(client, userdata, level, buf):
  print("buffer ",buf)

def on_disconnect(client, userdata, rc):
  print("client disconnected ok")

def on_message(client, userdata, msg):
  print(msg.topic+" "+str(msg.payload))

client1=paho.Client("control1") #create client object
client1.on_log=on_log
client1.tls_set(ca_certs='rootCA.pem',certfile='certificate.crt',keyfile='private.pem')

client1.on_connect = on_connect
client1.on_disconnect = on_disconnect
client1.on_message = on_message
client1.connect(broker,port) #establish connection
client1.loop_forever()
