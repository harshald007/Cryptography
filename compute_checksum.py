import hashlib
 
# Read the sensitive file
sensitive_file = open("sensitive.txt","rb").read()

# Open the file for writing the hash
file_hash = open("sensitive_checksum.txt", "w")

# Create a SHA-256 hash of the sensitive file
sha_256_hash = hashlib.sha256(sensitive_file).hexdigest() 

# Write the hash to the file
file_hash.write(sha_256_hash)
