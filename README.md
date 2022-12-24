# Cryptography

Welcome to the Cryptography project! In this project, you will implement programs to perform public-key encryption, compute cryptographic checksums (keyless and keyed), and verify the integrity of files using these checksums.

## Section 1: Public-key encryption
1. Create a file called `sensitive.txt` in the current directory.

2. Write a program called `generate_keys` that generates a pair of 3072-bit RSA keys and saves the public key to a file called `pub_key` and the private key to a file called `priv_key`. 

To run the program, open a terminal window and type `generate_keys`. Then, display the contents of pub_key and priv_key using the hexdump command.

3. Write a program called `encrypt_file` that encrypts the contents of ``sensitive.txt`` using the public key in pub_key. The encrypted file will overwrite the original `sensitive.txt`. Make sure that the original (unencrypted) `sensitive.txt` is in the same directory as the program. 

> To run the program, open a terminal window and type `encrypt_file`. Then, display the first 100 bytes of the encrypted `sensitive.txt` using the hexdump command.

4. Write a program called `decrypt_file` that decrypts the contents of `sensitive.txt` using the private key in `priv_key`. The decrypted file will overwrite the encrypted `sensitive.txt`. Make sure that the encrypted `sensitive.txt` is in the same directory as the program. 

> To run the program, open a terminal window and type `decrypt_file`. Then, display the first 100 bytes of the decrypted `sensitive.txt` using the head command.

## Section 2: Cryptographic checksums
5. Write a program called `compute_checksum` that computes a keyless cryptographic checksum of sensitive.txt using the SHA256 hash function. The checksum should be written to a file called `sensitive_checksum.txt` in text format.

> Display the checksum of `sensitive_checksum.txt` using the `cat` command.

6. Write a program called `verify_checksum` that computes a checksum of sensitive.txt using SHA256 and compares it with the contents of `sensitive_checksum.txt`. If the resulting hash values are the same, the program should output "Accept!" and otherwise it should output "Reject!".

7. Write a program called `compute_keyed_checksum` that works similarly to `compute_checksum`, but instead of `SHA256`, it should use the keyed hash function `HMAC-SHA256`. A 256-bit key should be read from a file called `key.bin`. The checksum should be written to a file called `sensitive_keyed_checksum.txt` in text format.

> The file `key.bin` can be created using the command `head -c 256 /dev/urandom > key.bin`

> Display the checksum of `sensitive_keyed_checksum.txt` using the `cat` command.


8. Write a program called `verify_keyed_checksum` that works similarly to `verify_checksum`, but it should compute a keyed checksum of `sensitive.txt` using HMAC-SHA256 and compare it with the contents of `sensitive_keyed_checksum.txt`. If the resulting values are the same, the program should output "Accept!" and otherwise it should output "Reject!".