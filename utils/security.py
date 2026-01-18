import os
import base64
from cryptography.fernet import Fernet

def salt(length):
    return base64.b64encode(os.urandom(length)).decode('utf-8')[:length]

def generate_key():
    key = Fernet.generate_key()
    
    with open('secret.key', 'w') as keyfile:
        keyfile.write(key)
    return key


def load_key():
    pass


def encrypt_string(text):
    key = Fernet.generate_key()
    f = Fernet(key)
    enc = f.encrypt(text)
    return enc
