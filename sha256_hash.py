# sha256_hash.py
# This app generates a SHA-256 hash for an input string or file.
# Reference: hashlib — Secure hashes and message digests (https://docs.python.org/3/library/hashlib.html)

import hashlib

# Generate a SHA-256 hash for an input string.
def generate_hash_for_text(message):

    m = hashlib.sha256()
    m.update(message.encode("utf-8"))

    return m.hexdigest()

# Generate a SHA-256 hash for a file.
def generate_hash_for_file(file_path):

    m = hashlib.sha256()

    with open(file_path, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")

    return digest.hexdigest()


# Test the functions.
if __name__ == "__main__":
    # Get user's choice for hashing a string or a file.
    user_choice = input("Do you want to hash a text (1) or a file (2)? Enter 1 or 2: ")
    
    if user_choice == "1":
        # Get user input for text to hash.
        user_message = input("Enter a message to hash: ")
  
        print("\nSHA-256 Text Hash Test:")
        print("   Original text:", user_message)
        hash_result = generate_hash_for_text(user_message)
        print("   SHA-256 hash for the text:", hash_result, "\n")
    
    elif user_choice == "2":
        # Get user input for file path.
        user_file_path = input("Enter the file path to hash: ")
  
        print("\nSHA-256 File Hash Test:")
        print("   Hashed file:", user_file_path)
        try:
            hash_result = generate_hash_for_file(user_file_path)
            print("   SHA-256 hash for the file:", hash_result, "\n")
        except FileNotFoundError:
            print("   Error: File not found. Exiting the program.\n")
            exit(1)
        
    else:
        print("Invalid choice. Exiting the program.\n")
        exit(1)
