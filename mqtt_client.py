import paho.mqtt.client as paho
import ssl
import time
broker="<exact_broker_FQDN_from_cert>"
port=8883

def on_connect(client, userdata, flags, rc):
  # Subscribe to all topics
  client.subscribe('#', qos = 1)     
  # Broker Status (Mosquitto)
  client.subscribe('$SYS/#')            

def on_log(client, userdata, level, buf):
  print("buffer ",buf)

def on_disconnect(client, userdata, rc):
  print("client disconnected ok")

def on_message(client, userdata, msg):
  print(msg.topic+" "+str(msg.payload))

#create client object
client1=paho.Client("control1") 
client1.on_log=on_log
client1.tls_set(ca_certs='rootCA.pem',certfile='certificate.crt',keyfile='private.pem')

client1.on_connect = on_connect
client1.on_disconnect = on_disconnect
client1.on_message = on_message

#establish connection
client1.connect(broker,port) 
client1.loop_forever()
