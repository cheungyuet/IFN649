import paho.mqtt.publish as publish


try:
    publish.single("ifn649", "Hello World", hostname="test.mosquitto.org", port=1883)
    print("Done")

except Exception as e:
    print(f"Failed to publish: {e}")