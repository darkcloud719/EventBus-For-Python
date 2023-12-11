from aqeventbus import AQEventBusConfiguration, AQEventBusSender, AQEventBusReceiver
import json
from threading import Thread 
from json import loads, JSONEncoder

key = "495dcbb7303c4b2abc918be15df7d52e74c02f94e891409a9f4c0e181ca264a4"
account_encrypted = "5iXEGFi3Z/3Ny5nDEAibYq8HkYdNSsi+"
password_encrypted = "9QeFicfS12AJpzha+m/ZZJ9i6pjKJFQH"


RABBITMQ_USERNAME = account_encrypted
RABBITMQ_PASSWORD = password_encrypted
RABBITMQ_HOST = 'nebula-res.ccasd.com'
RABBITMQ_PORT = '33134'
RABBITMQ_VIRTUAL_HOST = "Net9_Development"
KEY = key
configuration = AQEventBusConfiguration(RABBITMQ_USERNAME, RABBITMQ_PASSWORD, RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_VIRTUAL_HOST, KEY)

class SampleMessage:
    def __init__(self,name):
        self.name = name

def handler(ch, method, properties, body):
    msg = loads(body.decode())
    print("Received message: %s" % msg["message"])

    # t = Thread(target=send_message(msg))
    # t.start()
    # threads.append(t)


# with AQEventBusSender(configuration) as sender:
#     message = json.dumps({'user_email':'test'})
#     sender.send_message_to_queue(message,"Net7C2")

# receiver = AQEventBusReceiver(configuration,"test")

if __name__ == "__main__":
    threads = []

    receiver = AQEventBusReceiver(configuration, "test")
    receiver.add_on_message_callback(handler)
    receiver.start_consuming()
