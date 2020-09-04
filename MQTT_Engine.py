import paho.mqtt.client as mqtt

class MQTTEngine():
    def __init__(self, broker_addres, console, ui):
        self.client = mqtt.Client('PC', clean_session=False)
        self.console = console
        self.ui = ui
        self.broker_addres = broker_addres
        self.init_mqtt()

    def init_mqtt(self):
        self.broker_addres_ui = self.ui.broker_addres
        self.broker_addres_ui.setText(self.broker_addres)
        self.connect_button = self.ui.connect_button
        self.connect_button.clicked.connect(self.connection)
        self.connect_button.setStyleSheet(f"background-color: red")
        self.is_connect = False
        self.topic = 'testPepper'
    
    def send_message(self, msg):
        self.console(f"send message {msg}\n")
        self.client.publish(self.topic, msg, qos=0)

    def connection(self):
        self.broker_addres = self.broker_addres_ui.text()
        try:
            self.client.disconnect() if (self.is_connect) else self.client.connect(self.broker_addres, keepalive=10000)
            self.connect_button.setStyleSheet(f"background-color: {'red' if (self.is_connect) else 'green'}")
            self.connect_button.setText(f"{'Disconnect' if not self.is_connect else 'Connect'}")
            self.console(f"{'Client has disconnect' if (self.is_connect) else f'Client Connect to {self.broker_addres}'}\n")

            self.is_connect = not self.is_connect
        except:
            self.console(f'Could\'n connect to {self.broker_addres}\n')
            
        

