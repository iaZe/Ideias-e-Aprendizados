def numero(num):
    if num < 0:
        return -1
    
    numero(num - 1)

    par = 0
    impar = 0

    n1 = num

    if n1 % 2 == 0:
        print(f'O número {n1} é PAR')
        par += 1
    else:
        print(f'O número {n1} é IMPAR')
        impar += 1

    print(f'Você obteve {par} números pares e {impar} números impares')
