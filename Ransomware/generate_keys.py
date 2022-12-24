from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate a private key with 3072 bits
private_key = RSA.generate(3072)

# Generate the public key from the private key
pubkey = private_key.publickey()

# Export the private key in ASCII format and decode it
private_key = private_key.exportKey().decode("ascii")

# Export the public key in ASCII format and decode it
pubkey = pubkey.exportKey().decode("ascii")

# Open pub_key file in write mode
with open('pub_key', 'w') as p:
    p.write(pubkey)
    
# Open priv_key file in write mode
with open('priv_key', 'w') as p:
    p.write(private_key)


