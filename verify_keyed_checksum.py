import hmac
import hashlib
import base64

# Read the binary key file
bin_key = open("key.bin","rb").read()

# Read the sensitive file
sensitive_file = open("sensitive.txt","rb").read()

# Read the keyed hash of the file from the file
sensitive_checksum = open("sensitive_keyed_checksum.txt","r+").read()

# Create a keyed hash of the sensitive file using the binary key and SHA-256
keyed_hash = hmac.new(bin_key, sensitive_file, digestmod=hashlib.sha256).digest()

# Encode the keyed hash in base64 and decode it to a string
keyed_hash = base64.b64encode(keyed_hash).decode()

# Compare the keyed hash of the file with the keyed hash stored in the file
if keyed_hash == sensitive_checksum:
    print("Accept!")
else:
    print("Reject!")
