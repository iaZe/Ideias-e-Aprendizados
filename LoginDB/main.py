import os
import sqlite3
from sqlite3 import Error

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("database.db")
    except Error as error:
        print(error)
    return connection

def select(query):
    with create_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

def execute(query):
    with create_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

def login(user, password):
    query = "SELECT * FROM users WHERE user = '{}' AND password = '{}'".format(user, password)
    return select(query)

def register(user, password):
    query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, password TEXT)"
    execute(query)
    query = "INSERT INTO users(user, password) VALUES('{}', '{}')".format(user, password)
    execute(query)

def main():
    while True:
        os.system("cls")
        print("Olá, seja bem-vindo ao sistema")
        print("1 - Login")
        print("2 - Registrar")
        print("3 - Sair")
        option = input("Digite a opção desejada: ")
        if option == "1":
            user = input("Digite o usuário: ")
            password = input("Digite a senha: ")
            if login(user, password):
                print("Login efetuado com sucesso")
                input("Aperte ENTER para continuar")
            else:
                print("Usuário ou senha inválidos")
                input("Aperte ENTER para continuar")
        elif option == "2":
            user = input("Digite o usuário: ")
            password = input("Digite a senha: ")
            register(user, password)
            print("Usuário cadastrado com sucesso")
            input("Aperte ENTER para continuar")
        elif option == "3":
            break
        else:
            print("Opção inválida")
            input("Aperte ENTER para continuar")

if __name__ == "__main__":
    main()

