for p in range (1, 6):
    peso = int(input('digite o peso da {}° pessoa: '.format(p)))

    if (p == 1 ):
        maior = peso

    elif(peso > maior):
        maior = peso

    if (p == 1 ):
        menor = peso

    elif(peso < menor):
        menor = peso

print('o maior peso é {}Kg'.format(maior))
print('o menor peso é {}Kg'.format(menor))