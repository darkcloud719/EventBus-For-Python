from pika import BlockingConnection
from pika import ConnectionParameters
from json import dumps
import logging
import pika

class AQEventBusSender(object):
    __slots__ = ["_configuration","_connection","_channel","_queue","_routing_key","_exchange"]

    def __init__(self, configuration):
        """
        Create RabbitMQ Sender
        :param configurtion: EventBusConfiguration object
        """
        credentials = pika.PlainCredentials(configuration.username,configuration.password)
        self._configuration = configuration
        self._connection = BlockingConnection(ConnectionParameters(host=self._configuration.host,
                                                                   port=self._configuration.port,
                                                                   virtual_host=self._configuration.virtual_host,
                                                                   credentials=credentials))
        
        self._channel = self._connection.channel()

# public async Task<(bool isSuccess, string message)> SendMessage(string data, string queueId, Dictionary<string, string> userHeaderDictionary = null)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()
    
    def send_message_to_queue(self,message,queueId):

        finalmessage = {
            "data":message
        }

        msg = {
            "messageType":['urn:message:'+'SaaS.NetCore.AQ.EventBus:IntegrationEvent'],
            "destinationAddress": f"amqp://{self._configuration.virtual_host}:{self._configuration.port}/{queueId}?bind=true&queue={queueId}",
            "message":finalmessage,
        }

        self._channel.basic_publish(
            exchange=queueId,
            routing_key='',
            body=dumps(msg)
        )
        
    


