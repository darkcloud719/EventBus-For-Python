from pika import BlockingConnection
from pika import ConnectionParameters
import pika

class MetaClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        """ Singleton Pattern """
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args,**kwargs)
            return cls._instance[cls]
        
class AQEventBusReceiver(metaclass=MetaClass):
    __slots__ = ["_configuration","_connection","_channel","_queue","_exchange","_on_message_callback"]

    def __init__(self, configuration, queue):
        """
        Create RabbitMQ Receiver
        :param configuration: EventBusConfiguration object
        """
        credentials = pika.PlainCredentials(configuration.username,configuration.password)
        self._configuration = configuration
        self._queue = queue
        self._exchange = "SaaS.NetCore.AQ.EventBus:IntegrationEvent"
        self._connection = BlockingConnection(ConnectionParameters(host=self._configuration.host,
                                                                   port=self._configuration.port,
                                                                   virtual_host=self._configuration.virtual_host,
                                                                   credentials=credentials))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self._queue,
                                    durable=True)
        self._channel.exchange_declare(exchange=self._exchange,
                                       exchange_type='fanout',
                                       durable=True)
        self._channel.queue_bind(queue=self._queue,
                                 exchange=self._exchange,
                                 routing_key='')
        self._on_message_callback = None

    def add_on_message_callback(self, on_message_callback):
        """
        Add function callback
        :param self:
        :param on_message_callback: function where the message is consumed
        :return: None
        """
        self._on_message_callback = on_message_callback

    def start_consuming(self):
        """ Start Consumer with earlier definded callback """
        self._channel.basic_consume(queue=self._queue,
                                    on_message_callback=self._on_message_callback,
                                    auto_ack=True)
        self._channel.start_consuming()

