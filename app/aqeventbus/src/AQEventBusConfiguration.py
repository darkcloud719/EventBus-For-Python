from .utils import decrypt

class AQEventBusConfiguration(object):
    """
    Create RabbitMQ Configuration
    """

    def __init__(self, username_encrypted, password_encrypted, host, port, virtual_host, key):
        # Check if any of the parameters is None
        if not username_encrypted or not password_encrypted or not host or not port or not virtual_host or not key:
            raise ValueError("All parameters must have a non-empty value.")
        
        # Check if 'key' has 64 length
        if len(key) != 64:
            raise ValueError("Key length must be 32 characters.")

        # Check if the 'key' is a valid hexadecimal string
        try:
            int(key,16)
        except ValueError:
            raise ValueError("Key must be a valid hexadecimal string.")
        
        self.username = decrypt(key,username_encrypted)
        self.password = decrypt(key,password_encrypted)
        self.host = host
        self.port = port
        self.virtual_host = virtual_host
        self.key = key

        print(self.username)
        print(self.password)


