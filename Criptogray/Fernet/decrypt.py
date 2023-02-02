import os
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

with open("key.key", "rb") as key_file:
    key = key_file.read()

for file in os.listdir():
    if file == "key.key" or file == "decrypt.py" or file == "encrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(file, "wb") as f:
        f.write(decrypted)