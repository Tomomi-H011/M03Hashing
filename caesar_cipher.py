# caesar_cipher.py
# This app uses the Caesar cipher to encrypt and decrypt an input text.
# Reference: Python Beginner Project: Build a Caesar Cipher Encryption App 
#            (https://www.youtube.com/watch?v=x71kJyNvB5o)


# Define variables.
FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

# Encrypt or decrypt an input message using the Caesar cipher.
def caesar_shift(message, shift):
    result = ""
    # Go through each of the letters in the message.
    for char in message.upper():
        if char.isalpha():
            # Convert the letter to ASCII code, shift the letter, and convert back to a character.
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE
            
            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char

        else:
            result += char
        
    return result


# Get user input.
user_message = input("Enter a message to encrypt: ")
user_shift_key = int(input("Enter a shift key (integer):"))


# Test the function.
if __name__ == "__main__":
    print("\nCaesar Cipher Test:")
    print("Original message:", user_message)
    encrypted_message = caesar_shift(user_message, user_shift_key)
    print("Encrypted message:", encrypted_message)
    decrypted_message = caesar_shift(encrypted_message, -user_shift_key)
    print("Decrypted message:", decrypted_message, "\n")

