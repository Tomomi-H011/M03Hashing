# App name: digital_signature.py
# Description: This app applies digital signatures and verifies files using 
#   Python’s cryptography library (RSA, SHA-256) to simulate OpenSSL functionality.
# References: 
#   Hashing & Digital Signature Functions with Python to Digitally Sign Data (Part 3) - Paul Mahon 
#       (https://www.youtube.com/watch?v=8e7MH78PhLU)
#   Python Cryptography Library Documentation - Cryptography 
#       (https://cryptography.io/en/latest/)

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# Generate a private key and a public key.
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    public_key = private_key.public_key()

    # Write the keys to files.
    try:
        with open("private_key.pem", "wb") as private_file:
            private_file.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )

        with open("public_key.pem", "wb") as public_file:
            public_file.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )

        print("    Keys generated and saved to files.")
        return True
    except (OSError, ValueError, TypeError, Exception) as e:
        print(f"    Error during key generation: {e}")
        return False


# Sign a file using the private key and generate a signature file.
def sign_file(file_path, private_key_path, signature_path):
    try:
        # Load the private key.
        with open(private_key_path, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(), password=None
            )

        # Read the file to be signed.
        with open(file_path, "rb") as f:
            data = f.read()

        # Sign the data.
        signature = private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )

        # Write the signature to a file.
        with open(signature_path, "wb") as sig_file:
            sig_file.write(signature)
        print("    File signed with a digital signature.")
        return True

    except (FileNotFoundError, OSError, ValueError, TypeError, Exception) as e:
        print(f"    Error signing the file: {e}")
        return False


# Verify the signature using the public key.
def verify_signature(file_path, signature_path, public_key_path):
    try:
        # Load the public key.
        with open(public_key_path, "rb") as key_file:
            public_key = serialization.load_pem_public_key(key_file.read())

        # Read the file and the signature.
        with open(file_path, "rb") as f:
            data = f.read()

        with open(signature_path, "rb") as sig_file:
            signature = sig_file.read()

        # Verify the signature.
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )
        print("    Signature is valid.")
        return True

    except (FileNotFoundError, OSError, Exception, TypeError, ValueError) as e:
        print(f"    Signature verification failed: {e}")
        return False


# Test for valid signature and file
def test_valid_signature(
    file_to_sign, private_key_path, public_key_path, signature_path
):
    print("Test 1 for valid signature and file:")
    if not generate_keys():
        print("    Exiting.")
        return
    if not sign_file(file_to_sign, private_key_path, signature_path):
        print("    Exiting.")
        return
    if not verify_signature(file_to_sign, signature_path, public_key_path):
        print("    Exiting.")
        return
    print("    <Result> Success. The digital signature and the file are valid.")


# Test for invalid signature or file
def test_invalid_signature(file_to_sign, signature_path, public_key_path):
    print("Test 2 for invalid signature or file:")
    # Change the content of file_to_sign.txt for testing
    with open(file_to_sign, "a") as f:
        f.write("\nAltering the file.")
    # Verify the altered file with the original signature using the public key, which should fail
    if not verify_signature(file_to_sign, signature_path, public_key_path):
        print("    Exiting.")


# Restore the altered file after the second test
def restore_file(file_to_sign):
    try:
        with open(file_to_sign, "r") as f:
            lines = f.readlines()
        if lines and lines[-1].strip() == "Altering the file.":
            lines = lines[:-1]  # Remove the last line
            with open(file_to_sign, "w") as f:
                f.writelines(lines)  # Rewrite the file without the removed line
        print("File restored to original state after testing.")
    except (FileNotFoundError, OSError) as e:
        print(f"Error during file restoration: {e}")


# Perform the tests
if __name__ == "__main__":
    file_to_sign = "file_to_sign.txt"
    private_key_path = "private_key.pem"
    public_key_path = "public_key.pem"
    signature_path = "signature.sig"

    test_valid_signature(file_to_sign, private_key_path, public_key_path, signature_path)
    test_invalid_signature(file_to_sign, signature_path, public_key_path)
    restore_file(file_to_sign)
