termo1 = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao da sua PA: '))
decimo = (termo1 +((10-1) * razao))

print()

for c in range(termo1, decimo +1, razao):
    print('{}'.format(c), end=' - ') 
print('FIM\n\n')