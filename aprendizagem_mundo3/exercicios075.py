a = int(input('digite um numero: '))
b = int(input('digite um numero: '))
c = int(input('digite um numero: '))
d = int(input('digite um numero: '))
cont = 0

numeros =(a, b, c, d)

print('voce digitou os valores: {}'.format(numeros))
print('o valor 9 apareceu {} vezes'.format(numeros.count(9)))
if 3 in numeros: 
  print('o numero 3 apareceu na {}ª posiçao'.format(numeros.index(3) + 1))

else:
  print('o valor 3 nao foi digitado!')
  
print('os valores pares digitados foram: ', end= '')
for n in numeros:
  resto = n % 2
  
  if resto == 0:
    print(n, end=' ')
    