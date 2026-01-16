import os
from cryptography.fernet import Fernet

# Generate a unique encryption key (dummy, akan diganti dari main.py)
encryption_key = Fernet.generate_key()

def encrypt_file(file_path):
    """Encrypts a file using the global encryption_key"""
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(encryption_key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path):
    """Decrypts a file using the global encryption_key"""
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(encryption_key)
    decrypted_data = fernet.decrypt(data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)
