# Module 3: Secure Hashing and Encryption

## Description and App Logic:
This project contains the following three apps to satisfy assignment requirements:

1. sha256_hash.py: Generates a SHA-256 hash for an input string or file.
    + Ask user to choose hashing an input text or a file.
    + Hash either input text or a file using SHA-256. (User needs to type 'file_to_hash.txt' when testing file hashing.)
    + Display the input text or file name and a hashed value.

    + [Test Results] test1_hash_text.png, test2_hash_file.png

2. caesar_cipher.py: Uses Caesar cipher to encrypt/decrypt an input text.
    + Ask user to input a message to encrypt and a number of characters to shift.
    + Change the input texts to upper case and encrypt (ignoring non-alphabet characters and spaces).
    + Display the original message and encrypted message in the terminal.
    + Use the same function to decrypt the encrypted message.
    + Display the decrypted message in the terminal.

    + [Test Results] test3_encrypt_text.png

3. digital_signature.py: Applies digital signatures and verifies files using Python’s cryptography library (RSA, SHA-256) to simulate OpenSSL functionality.
    + Generate a pair of private and public keys using RSA.
    + Store the keys in files.
    + Sign a file using the private key.
    + Store the digital signature in a file.
    + Test 1: Verify the digital signature and hash of the signed file. Display the result.
    + Modify the content of the signed file.
    + Test 2: Verify the signed file again. Display the result (expecting failed verification.)
    + Restore the modified file for next app run.

    + [Test Results] test4_digital_signature.png

## How to Run the app:
1. Open a terminal in this folder.
2. Create and activate a virtual environment using the following codes.
    + python -m venv .venv
    + .venv\Scripts\activate
3. Install required packages.
    + pip install -r requirements.txt
4. Run each app.
    + python sha256_hash.py
    + python caesar_cipher.py
    + digital_signature.py
5. The apps will run tests for each assignment requirements and display results in the terminal.

