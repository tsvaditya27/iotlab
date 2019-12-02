import paho.mqtt.client as mqtt
def on_connect(client,userdata,flags,rc):
    print("connected with mqtt server"+str(rc))
    client.subscribe("TOPIC/581163")
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload=="HELLO":
        print("command received to do something")
client = mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect("test.mosquitto.org", 1883,60)
client.loop_forever()
