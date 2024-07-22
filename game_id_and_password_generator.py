import random
import string
import hashlib
import secrets
import bcrypt
import pyperclip
from cryptography.fernet import Fernet

def password_maker(password_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(password_length))
    return password

def game_id_generator():
    game_id = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return game_id

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
    return encrypted_password.decode('utf-8')

def decrypt_password(encrypted_password, key):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password.encode('utf-8'))
    return decrypted_password.decode('utf-8')

def main():
    key = Fernet.generate_key()
    user_input = input("1. Generate game ID\n2. Generate password\nEnter your choice: ")
    
    if user_input == "1":
        game_id = game_id_generator()
        print("Generated game ID:", game_id)
    elif user_input == "2":
        password_length = int(input("Enter the length of the password: "))
        if password_length < 8:
            print("Password length should be at least 8 characters.")
            return
        password = password_maker(password_length)
        hashed_password = hash_password(password)
        encrypted_password = encrypt_password(password, key)
        print("Generated password:", password)
        print("Hashed password:", hashed_password)
        print("Encrypted password:", encrypted_password)
        pyperclip.copy(encrypt_password(password, key))
        decrypted_password = decrypt_password(encrypted_password, key)
        print("Decrypted password:", decrypted_password)
        print("Copied encrypted password to clipboard.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
