soma = 0
cont = 0

for multiplos in range(0, 501, 3):
   if (multiplos % 2 == 1):
       cont = cont + 1
       soma = soma + multiplos
    
print('a soma dos numeros impares multiplos de 3 entre 1 e 500 é: {}'.format(soma))
print('quantidade de numeros impares multiplos de 3 é: {}'.format(cont))
