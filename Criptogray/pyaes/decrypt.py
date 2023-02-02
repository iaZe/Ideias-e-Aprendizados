import os
import pyaes

KEY = b"0123456789123456"

def decrypt(file_path):
    with open(file_path, "rb") as file:
        content = file.read()

        aes = pyaes.AESModeOfOperationCTR(KEY)
        decrypted_data = aes.decrypt(content)

        new_file = file_path[:-4]

    with open(new_file, "wb") as file:
        file.write(decrypted_data)
        os.remove(file_path)

system = os.walk("C:/Users/Kali/Desktop/ransomware/testes")
for root, dirs, files in system:
    for file in files:
        file_path = os.path.join(root, file)
        decrypt(file_path)
        print(f"[+] Decrypting {file_path}")