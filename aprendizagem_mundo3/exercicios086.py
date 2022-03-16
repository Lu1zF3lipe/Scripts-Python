matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0 ,3):
    for c in range(0, 3):
        matriz[i][c] = int(input('digite um valor pra posiçao [{}][{}]: '.format(i, c)))

for i in range(0 ,3):
    for c in range(0, 3):
        print('[{}]'.format(matriz[i][c]),end= ' ')

    print()
