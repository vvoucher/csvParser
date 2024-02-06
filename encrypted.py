import base64
from cryptography.fernet import Fernet
from main import main

key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(main)

decrypted_message = encryption_type.decrypt(encrypted_message)

exec(decrypted_message)