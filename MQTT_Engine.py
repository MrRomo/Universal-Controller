import paho.mqtt.client as mqtt

class MQTTEngine():
    def __init__(self, broker_addres = ''):
        self.client = mqtt.Client('PC', clean_session=False)
        self.broker_addres = broker_addres
        
    def send_message(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

if __name__ == "__main__":
    test = MQTTEngine('NUevasss')