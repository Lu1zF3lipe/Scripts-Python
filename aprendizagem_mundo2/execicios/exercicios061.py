termo1 = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao da sua PA: '))

cont = 0
print(termo1, end=' - ')

while cont != 9:
    cont += 1
    termo1 += razao
    print('{}'.format(termo1), end=' - ') 

print('FIM\n\n')