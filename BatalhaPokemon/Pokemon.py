import os
import pokemons
import random

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def player(vida, ataque, agilidade):
    vida = vida
    ataque = ataque
    agilidade = agilidade
    return vida, ataque, agilidade

def enemy(vida, ataque, agilidade):
    vida = enemy.vida
    ataque = enemy.ataque
    agilidade = enemy.agilidade
    return vida, ataque, agilidade

def miss():
    rate = random.randint(1, 6)
    agilidade = player.agilidade
    miss = agilidade / rate
    if miss > 12:
        return 1
    else:
        return 0

print("Bem-vindo ao mundo Pokémon!")
nome = input("Qual seu nome, treinador? ")

print(f"""Olá {nome}, você pode escolher um dos pokémons a seguir:
1 - Bulbasaur
2 - Charmander
3 - Squirtle""")
pokemon = input("Qual pokemon você deseja? ")

while pokemon != "1" and pokemon != "2" and pokemon != "3":
    pokemon = input("Você só pode escolher entre 1, 2 e 3. Qual pokemon você deseja? ")

if pokemon == "1":
    player.vida, player.ataque, player.agilidade = pokemons.bulbasaur()
    print("Você escolheu o Bulbasaur!")
elif pokemon == "2":
    player.vida, player.ataque, player.agilidade = pokemons.charmander()
    print("Você escolheu o Charmander!")
elif pokemon == "3":
    player.vida, player.ataque, player.agilidade = pokemons.squirtle()
    print("Você escolheu o Squirtle!")

input("Pressione ENTER para continuar...")
clear()


if pokemon == "1":
    escolha = input("Você encontrou um Charmander selvagem! O que deseja fazer? \n1 - Atacar \n2 - Fugir\nEscolha: ")
    clear()
    if escolha == "1":
        print("Vamos batalhar!")
        enemy.vida, enemy.ataque, enemy.agilidade = pokemons.charmander_selvagem()
        while player.vida > 0 and enemy.vida > 0:
            escolha = input("Você deseja atacar ou curar? \n1 - Atacar \n2 - Curar\nEscolha: ")
            if escolha == "1":
                print(f"Você ataca o Charmander selvagem e causa {player.ataque} de dano!")
                enemy.vida -= player.ataque
                print(f"O Charmander selvagem tem {enemy.vida} de vida!")
                if miss() == 1:
                    print("O Charmander selvagem errou o ataque!")
                else:
                    print(f"O Charmander selvagem ataca você e causa {enemy.ataque} de dano!")
                    player.vida -= enemy.ataque
                print(f"Você tem {player.vida} de vida!")
                print("Pressione Enter para continuar...")
            elif escolha == "2":
                print("Você cura seu pokemon!")
                player.vida += 20
                print(f"Você tem {player.vida} de vida!")
                print("Pressione Enter para continuar...")
            if enemy.vida <= 0:
                print("Você venceu o Charmander selvagem!")
            elif player.vida <= 0:
                print("Você perdeu!")
    else:
        print("Você fugiu do Charmander selvagem!")