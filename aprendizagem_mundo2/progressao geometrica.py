termo1 = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao da sua PG: '))
resultado = termo1

print()

print('{}'.format(resultado), end=' - ')
resultado = resultado * razao

print('{}'.format(resultado), end=' - ')

for c in range(termo1, 8 + termo1):
    resultado = resultado * razao
    print('{}'.format(resultado), end=' - ') 

print('FIM\n\n')