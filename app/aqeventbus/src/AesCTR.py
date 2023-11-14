from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import a2b_hex
import binascii
import os

class AesCTR:

    
    def int_of_string(self,s):
        # Convert a string to its hexadecimal representation and then to an integer
        return int(binascii.hexlify(s),16)
    
    def decrypt_message(self, key, cipherText):
        # Extract the counter value from the ciphertext
        count = cipherText[:16]
        # Initialze the counter for AES decryption
        ctr = Counter.new(128, initial_value=self.int_of_string(count))
        # Create an AES object for decryption
        aes = AES.new(a2b_hex(key), AES.MODE_CTR, counter=ctr)
        # Decrypt the cipherText excluding the counter part
        return aes.decrypt(cipherText[16:])
    
    def encrypt_message(self, key, plainText):
        # Generate a random counter value
        count = os.urandom(16)
        # Initialize the counter for AES encryption
        ctr = Counter.new(128,initial_value=self.int_of_string(count))
        # Create an AES object for encryption
        aes = AES.new(a2b_hex(key), AES.MODE_CTR, counter=ctr)
        # Combine the counter value and the encrypted plaintext
        return count + aes.encrypt(plainText)