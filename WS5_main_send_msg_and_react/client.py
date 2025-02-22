import paho.mqtt.client as mqtt
import serial

def on_connect(client, userdata, flags, rc): # Function for making connection
  print("Connected to MQTT")
  print("Connection returned result: " + str(rc) )

  client.subscribe("ifn649")

def on_message(client, userdata, msg): # Function for Sending msg
  print(msg.topic+" "+str(msg.payload))
  ser = serial.Serial("/dev/rfcomm0", 9600)
  ser.write(str.encode(str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()