lista = []
maior = 0
menor = 0
cont = 0

for i in range(0, 5):
    lista.append(int(input("digite um valor {}º: ".format(i+1))))

for c in range(len(lista)):
    cont += 1
    if(cont == 1):
        menor = lista[c]
        maior = lista[c]

    if(lista[c] > maior):
        maior = lista[c]

    elif(lista[c] < menor):
        menor = lista[c]

print('voce digitou os valores: {}'.format(lista))
print('o maior numero é {} na posiçao:'.format(maior),end= '')
for i, c in enumerate(lista):
    if (c == maior):
        print(f'{i} ', end= '')
print()

print('o menor numero é {} na posiçao:'.format(menor),end= '')
for i, c in enumerate(lista):
    if (c == menor):
        print(f'{i} ', end= '')
print()

