import os
import sqlite3
from sqlite3 import Error

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("system.db")
    except Error as err:
        print(err)
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

def register(user, password, acess):
    query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, password TEXT, acess NUMERIC)"
    execute(query)
    query = "INSERT INTO users (user, password, acess) VALUES('{}', '{}', '{}')".format(user, password, acess)
    execute(query)

def login(user, password):
    query = "SELECT * FROM users WHERE user = '{}' AND password = '{}'".format(user, password)
    return select(query)

def group(user):
    query = "SELECT acess FROM users WHERE user = '{}'".format(user)
    return select(query)

def main():
    while True:
        os.system("cls")
        print("Seja bem-vindo a academia")
        print("1 - Para fazer login")
        print("2 - Para Sair")
        option = input("Digite a opção desejada: ")
        if option == "1":
            user = input("Digite seu usuário: ")
            password = input("Digite sua senha: ")
            if login(user, password):
                os.system("cls")
                if group(user) == [(6,)]:
                    print("Login efetuado com sucesso!")
                    print("1 - Cadastrar novo usuário")
                    print("2 - Treino do dia")
                    print("3 - Sair")
                    option = input("Digite a opção desejada: ")
                    if option == "1":
                        user = input("Digite o usuário: ")
                        password = input("Digite a senha: ")
                        acess = input("Digite o grupo: ")
                        register(user, password, acess)
                        print("Usuário cadastrado com sucesso")
                        input("Aperte ENTER para continuar ")
                    elif option == "2":
                        print("Em andamento")
                        input("Aperte ENTER para continuar ")
                    elif option == "3":
                        break
                    else:
                        input("Opção inválida, aperte ENTER para continuar ")
                elif group(user) == [(1,)]:
                    print("Login efetuado com sucesso!")
                    print("1 - Treino do dia")
                    print("2 - Sair")
                    option = input("Digite a opção desejada: ")
                    if option == "1":
                        print("Em andamento")
                        input("Aperte ENTER para continuar ")
                    elif option == "2":
                        break
                    else:
                        input("Opção inválida, aperte ENTER para continuar ")
                else:
                    print("Usuário com erro no cadastro, contate um administrador")
                    input("aperte ENTER para continuar ")
            else:
                print("Usuário ou senha incorreto")
                input("Aperte ENTER para continuar ")
        elif option == "2":
            break
        else:
            input("Opção inválida, aperte ENTER para continuar ")


if __name__ == "__main__":
    main()
