#!/usr/local/bin/python

import paho.mqtt.client as paho
import ssl
import time
broker="<exact_broker_FQDN_from_cert>"
port=8883

def on_connect(client, userdata, flags, rc):
  client.subscribe('#', qos = 1)        # Subscribe to all topics
  client.subscribe('$SYS/#')            # Broker Status (Mosquitto)
  client.subscribe('$SYS/broker/bytes/received')
  client.subscribe('$SYS/broker/bytes/sent')
  client.subscribe('$SYS/broker/clients/active')
  client.subscribe('$SYS/broker/clients/connected')
  client.subscribe('$SYS/broker/clients/disconnected')
  client.subscribe('$SYS/broker/clients/expired')
  client.subscribe('$SYS/broker/clients/inactive')
  client.subscribe('$SYS/broker/clients/maximum')
  client.subscribe('$SYS/broker/clients/total')
  client.subscribe('$SYS/broker/connection/')
  client.subscribe('$SYS/broker/connection/#')
  client.subscribe('$SYS/broker/heap/current')
  client.subscribe('$SYS/broker/heap/current')
  client.subscribe('$SYS/broker/heap/maximum')
  client.subscribe('$SYS/broker/heap/maximum')
  client.subscribe('$SYS/broker/heap/maximum992')
  client.subscribe('$SYS/broker/load/bytes/received/+')
  client.subscribe('$SYS/broker/load/bytes/received/15min')
  client.subscribe('$SYS/broker/load/bytes/received/1min')
  client.subscribe('$SYS/broker/load/bytes/received/5min')
  client.subscribe('$SYS/broker/load/bytes/sent/+')
  client.subscribe('$SYS/broker/load/bytes/sent/15min')
  client.subscribe('$SYS/broker/load/bytes/sent/1min')
  client.subscribe('$SYS/broker/load/bytes/sent/5min')
  client.subscribe('$SYS/broker/load/connections/+')
  client.subscribe('$SYS/broker/load/connections/15min')
  client.subscribe('$SYS/broker/load/connections/1min')
  client.subscribe('$SYS/broker/load/connections/5min')
  client.subscribe('$SYS/broker/load/messages/received/+')
  client.subscribe('$SYS/broker/load/messages/received/15min')
  client.subscribe('$SYS/broker/load/messages/received/1min')
  client.subscribe('$SYS/broker/load/messages/received/5min')
  client.subscribe('$SYS/broker/load/messages/sent/+')
  client.subscribe('$SYS/broker/load/messages/sent/15min')
  client.subscribe('$SYS/broker/load/messages/sent/1min')
  client.subscribe('$SYS/broker/load/messages/sent/5min')
  client.subscribe('$SYS/broker/load/publish/dropped/+')
  client.subscribe('$SYS/broker/load/publish/received/+')
  client.subscribe('$SYS/broker/load/publish/received/15min')
  client.subscribe('$SYS/broker/load/publish/received/1min')
  client.subscribe('$SYS/broker/load/publish/received/5min')
  client.subscribe('$SYS/broker/load/publish/sent/+')
  client.subscribe('$SYS/broker/load/publish/sent/15min')
  client.subscribe('$SYS/broker/load/publish/sent/1min')
  client.subscribe('$SYS/broker/load/publish/sent/5min')
  client.subscribe('$SYS/broker/load/sockets/+')
  client.subscribe('$SYS/broker/load/sockets/15min')
  client.subscribe('$SYS/broker/load/sockets/1min')
  client.subscribe('$SYS/broker/load/sockets/5min')
  client.subscribe('$SYS/broker/messages/inflight')
  client.subscribe('$SYS/broker/messages/received')
  client.subscribe('$SYS/broker/messages/sent')
  client.subscribe('$SYS/broker/messages/stored')
  client.subscribe('$SYS/broker/publish/bytes/received')
  client.subscribe('$SYS/broker/publish/bytes/sent')
  client.subscribe('$SYS/broker/publish/messages/dropped')
  client.subscribe('$SYS/broker/publish/messages/received')
  client.subscribe('$SYS/broker/publish/messages/sent')
  client.subscribe('$SYS/broker/retained')
  client.subscribe('$SYS/broker/store/messages/bytes')
  client.subscribe('$SYS/broker/subscriptions/count')
  client.subscribe('$SYS/broker/timestamp')
  client.subscribe('$SYS/broker/uptime')
  client.subscribe('$SYS/broker/version')
  client.subscribe('+/+/+')
  client.subscribe('+/+/+/+')
  client.subscribe('+/b/c/#')
  client.subscribe('+/b/c/d')
  client.subscribe('a/#')
  client.subscribe('a/+/+/d')
  client.subscribe('a/+/c/d')
  client.subscribe('a/b/#')
  client.subscribe('a/b/c')
  client.subscribe('a/b/c/#')
  client.subscribe('a/b/c/d')
  client.subscribe('b/+/c/d')     

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
