from pika import BlockingConnection
from pika import ConnectionParameters
from json import dumps
import logging
import pika

class AQEventBusSender(object):
    __slots__ = ["_configuration","_connection","_channel","_queue","_exchange"]

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
        """
        Send a Json message to queueId

        Args:
            message (str): The JSON string to be sent
            queueId (str): The identifier of the message queue

        Returns:
            None
        """
        # Customize the message object
        message_customized_obj = {
            "data":message
        }

        # Create the MassTransit content object
        masstransit_content_obj = {
            "messageType":['urn:message:'+'SaaS.NetCore.AQ.EventBus:IntegrationEvent'],
            "destinationAddress": f"amqp://{self._configuration.virtual_host}:{self._configuration.port}/{queueId}?bind=true&queue={queueId}",
            "message":message_customized_obj,
        }

        # Publish the MassTransit content to the specified queue
        self._channel.basic_publish(
            exchange=queueId,
            routing_key='',
            body=dumps(masstransit_content_obj)
        )
        
    


