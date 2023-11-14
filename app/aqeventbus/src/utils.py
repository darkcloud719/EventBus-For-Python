from .AesCTR import AesCTR
import base64

def decrypt(_ctr_key, _cypherText):
    # Create an instance of the AesCTR class for decryption
    decryptor = AesCTR()
    # Convert the Base64-encoded cipherText to binarydata
    binary_cipherText = _cypherText.encode()
    # Decode the binary cipherText using Base64
    base64_decoded_str= base64.b64decode(binary_cipherText)
    # Decrypt the binary ciphertext and decode the result to string
    decrypt_message = decryptor.decrypt_message(_ctr_key, base64_decoded_str).decode()
    # Return the decrypted message
    return decrypt_message

def encrypt(_ctr_key, plainText):
    # Convert the plainText to binary data
    byte_plainText = plainText.encode()
    # Create an instance of the AesCTR class for encryption
    encryptor = AesCTR()
    # Encrypt the binary plainText using the aesCTR class
    byte_plainText_encrypted = encryptor.encrypt_message(_ctr_key, byte_plainText)
    # Encode the result in Base64 for better representation
    base64_encoded_str = base64.b64encode(byte_plainText_encrypted)
    # Decode the Base64 result to obtain the final encrypted message
    encrypt_message = base64_encoded_str.decode()
    # Return the encrypted message
    return encrypt_message
