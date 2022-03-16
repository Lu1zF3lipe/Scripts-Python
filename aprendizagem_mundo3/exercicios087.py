matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
soma_col3 = 0
maior_col2 = 0
cont = 0

for i in range(0 ,3):
    for c in range(0, 3):
        matriz[i][c] = int(input('digite um valor pra posiçao [{}][{}]: '.format(i, c)))

for i in range(0 ,3):
    for c in range(0, 3):
        print('[{}]'.format(matriz[i][c]),end= ' ')

    print()

for i in range(0 ,3):
    for c in range(0, 3):
        cont += 1

        if (matriz[i][c] % 2 == 0):
            soma_par += matriz[i][c]
        
        if (c == 2):
            soma_col3 += matriz[i][2]
        
        if (c == 1 ):
            if (cont == 1):
                maior_col2 = matriz[i][1]

            elif (matriz[i][1] > maior_col2):
                maior_col2 = matriz[i][1]

print('a soma dos valores pares é: {}'.format(soma_par))
print('a soma dos valores da terceira coluna é: {}'.format(soma_col3))
print('o maior valor da segunda coluna é: {}'.format(maior_col2))
