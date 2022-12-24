import codecs
import shutil
import os
import ast
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Func to split encrypted file into 384-byte chunks and decrypt it
def split(file):
    # Open file to be decrypted
    temp_file = open(file,"rb")
    
    # Read 384 bytes from the file
    byte = temp_file.read(384)
    
    # Loop until there are no more bytes to read
    while byte:
        # Create decryptor using the private key
        decryptor  = PKCS1_OAEP.new(priv_key)
        
        # Decrypt the 384-byte chunk
        message_decoded = decryptor.decrypt(ast.literal_eval(str(byte)))
        
        # Write the decrypted chunk to the output file
        sensitive_file.write(message_decoded)
        
        # Read the next 384 bytes
        byte = temp_file.read(384)
        
    # Close the file
    temp_file.close()


# Main function
if __name__ == "__main__":
    # Open the private key file and import it
    priv_key = open('priv_key','rb')
    priv_key = RSA.importKey(priv_key.read())
    
    # Open the output file for writing, and truncate any existing content
    sensitive_file= open("decrypted.txt","ab")
    sensitive_file.truncate(0)
    
    # Split and decrypt the file
    split("sensitive.txt")
    
    # Close the output file
    sensitive_file.close()

    # Copy the content of the new file to the old file and delete the new file
    shutil.copyfile('decrypted.txt','sensitive.txt')
    os.remove("decrypted.txt")
