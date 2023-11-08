class AQEventBusConfiguration(object):
    """
    Create RabbitMQ Configuration
    """

    def __init__(self, username, password, host='localhost', port='5672', virtual_host='/'):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.virtual_host = virtual_host


