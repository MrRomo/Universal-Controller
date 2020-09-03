import paho.mqtt.client as mqtt

class MQTTEngine():
    def __init__(self, broker_addres = '', console = 'none'):
        self.client = mqtt.Client('PC', clean_session=False)
        self.broker_addres = broker_addres
        self.console = console
        self.topic = 'testPepper'
    
    def send_message(self, msg):
        self.console(f"send message {msg}\n")
        self.client.publish(self.topic, msg, qos=0)

    def connect(self):
        self.console(f"Client Connect to {self.broker_addres}\n")
        self.client.connect(self.broker_addres, keepalive=10000)

    def disconnect(self):
        self.client.disconnect()
