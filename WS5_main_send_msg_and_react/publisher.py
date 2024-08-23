import paho.mqtt.publish as publish

publish.single("ifn649", "Hello World", hostname="test.mosquitto.org")
print("Done")