soma = 0
values = 0
cont = 0

while True:
    values = int(input('digite algum valor:'))

    if values == 999:
      break

    soma += values        
    cont += 1

print('foram digitados {} numeros'.format(cont))
print('a soma dos valores digitados é {}'.format(soma))