num = int(input('Digite um numero [DE 0 A 9999]: '))
par = 0
impar = 0

n1 = num // 1 % 10
n2 = num // 10 % 10
n3 = num // 100 % 10
n4 = num // 1000 % 10

if n1 % 2 == 0:
    print(f'O número {n1} é PAR')
    par += 1
else:
    print(f'O número {n1} é IMPAR')
    impar += 1

if n2 % 2 == 0:
    print(f'O número {n2} é PAR')
    par += 1
else:
    print(f'O número {n2} é IMPAR')
    impar += 1

if n3 % 2 == 0:
    print(f'O número {n3} é PAR')
    par += 1
else:
    print(f'O número {n3} é IMPAR')
    impar += 1

if n4 % 2 == 0:
    print(f'O número {n4} é PAR')
    par += 1
else:
    print(f'O número {n4} é IMPAR')
    impar += 1

print(f'Você obteve {par} números pares e {impar} números impares')
