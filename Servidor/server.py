import socket
from threading import Thread

# Criar um servidor para comunicar com o cliente
def server():
    # Definir o endereço do servidor
    ip_adress = '192.168.100.151'
    port = 5000

    # Criar um socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Vincular o socket ao endereço
        s.bind((ip_adress, port))
        # Escutar por conexões
        s.listen()
        # Aceitar conexões
        conn, addr = s.accept()
        # Receber dados
        data = conn.recv(1024)
        # Imprimir os dados recebidos
        print(data.decode('utf-8'))

# Criar uma thread para o servidor
t = Thread(target=server)
# Iniciar a thread
t.start()

