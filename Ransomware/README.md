# Sample Ransomware Project

This project includes three Python scripts `generate_keys.py`, `ransomware.py` and `decrypt.py`, as well as a testing folder called `secret`.

## Instructions

1. Generate the public and private key files using `generate_keys.py`.
   - Run the script with `python generate_keys.py`.
   - This will create the `public.pem` and `private.pem` files in the current directory.
   - These key files are required for the encryption and decryption.

2. Practice the encryption using `ransomware.py`.
   - Run the script with `python ransomware.py`.
   - This will encrypt all the files in the `secret` folder and its subdirectories.

3. Confirm success of encryption.
   - Check that the files in the `secret` folder are no longer readable.

4. Practice the decryption using `decrypt.py`.
   - Run the script with `python decrypt.py`.
   - This will decrypt all the files in the `secret` folder and its subdirectories.

5. Confirm success of decryption.
   - Check that the files in the `secret` folder are readable again.

## Thank you

Thank you for visiting this project.

Proof of Concept can be found on my blog: (Ransomware)[https://medium.com/@ianpeter/ransomware-project-195ec1a078eb]
