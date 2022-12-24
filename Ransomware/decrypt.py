import os
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES

# This function returns an iterator that yields all the files in the given directory
# and its subdirectories.
def scan(top_dir):
    for object in os.scandir(top_dir):
        if object.is_file():
            yield object
        else:
            yield from scan(object.path)

# This function decrypts the given file using the RSA private key in the given file.
def decrypt(file_to_dec, privateKeyFile):
    '''
    use EAX mode to allow detection of unauthorized modifications
    '''

    # Read the private key from the file
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()

    # Create a private key object
    key = RSA.import_key(privateKey)

    # Read the encrypted data from the file
    with open(file_to_dec, 'rb') as file:
        # Get the encrypted session key, nonce, tag, and ciphertext from the file
        encrypted_Session_Key, nonce, tag, ciphertext = [ file.read(x) for x in (key.size_in_bytes(), 16, 16, -1) ]

    # Decrypt the session key using the private key
    cipher_text = PKCS1_OAEP.new(key)
    session_key = cipher_text.decrypt(encrypted_Session_Key)

    # Decrypt the data using the session key
    cipher_text = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_text.decrypt_and_verify(ciphertext, tag)

    # Overwrite the encrypted file with the decrypted data
    with open(file_to_dec,'wb') as file:
        file.write(data)
        print("Decrypted successfully")

if __name__ == "__main__":
    # The directory to start decryption
    directory = 'secret'
    for item in scan(directory): 
        # Decrypt all files
        decrypt(Path(item), 'private.pem')
