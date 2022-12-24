import hashlib
 
# Read the sensitive file
sensitive_file = open("sensitive.txt","rb").read()

# Read the hash of the file from the file
file_hash = open("sensitive_checksum.txt", "r").read()


# Create a SHA-256 hash of the sensitive file
sha_256_hash = hashlib.sha256(sensitive_file).hexdigest() 

# Compare the hash of the file with the hash stored in the file
if sha_256_hash == file_hash:
    print("Accept!")
else:
    print("Reject!")
