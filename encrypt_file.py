import codecs
import shutil
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Func to split file into 128-byte chunks and encrypt each chunk
def split(file):
    temp_file = open(file, "rb")  # Open file in binary read mode
    byte = temp_file.read(128)  # Read 128 bytes from the file
    while byte:
        encryptor = PKCS1_OAEP.new(pub_key)  # Create a new encryptor using the public key
        message_encoded = encryptor.encrypt(byte)  # Encrypt the current chunk of bytes
        sensitive_file.write(message_encoded)  # Write the encrypted chunk to the temp file
        byte = temp_file.read(128)  # Read the next chunk of bytes
    temp_file.close()  # Close the file at the end


if __name__ == "__main__":
    pub_key = open('pub_key', 'rb')  # Open the public key file in binary read mode
    pub_key = RSA.importKey(pub_key.read())  # Import the public key

    sensitive_file = open("encrypted.txt", "ab")  # Open a temp file to store encrypted text in binary append mode
    sensitive_file.truncate(0)  # Clear the contents of the temp file
    split("sensitive.txt")  # Encrypt the sensitive file and write the encrypted data to the temp file

    sensitive_file.close()  # Close the temp file

    # Overwrite the original file with the encrypted data and delete the temp file
    shutil.copyfile('encrypted.txt', 'sensitive.txt')
    os.remove("encrypted.txt")
