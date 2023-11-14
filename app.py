from aqeventbus import AQEventBusConfiguration, AQEventBusSender
import json

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

with AQEventBusSender(configuration) as sender:
    message = json.dumps({'user_email':'test'})
    sender.send_message_to_queue(message,"Net7C2")
