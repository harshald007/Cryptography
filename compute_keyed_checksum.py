import hmac
import hashlib
import base64

# Read the binary key file
bin_key = open("key.bin","rb").read()

# Read the sensitive file
sensitive_file = open("sensitive.txt","rb").read()

# Open the file for writing the keyed hash
file_hash = open('sensitive_keyed_checksum.txt','w+')

# Create a keyed hash of the sensitive file using the binary key and SHA-256
keyed_hash = hmac.new(bin_key, sensitive_file, digestmod=hashlib.sha256).digest()

# Encode the keyed hash in base64 and decode it to a string for writing to file
keyed_hash = base64.b64encode(keyed_hash).decode()

# Write the keyed hash to the file
file_hash.write(keyed_hash)
