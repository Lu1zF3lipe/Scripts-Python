a = int(input('digite o primeiro numero: '))
b = int(input('digite o segundo numero: '))
c = int(input('digite o terceiro numero: '))

maior = a
if (b > a and b > c):
    maior = b
if (c > a and c > b):
    maior = c
menor = a 
if (b < a and b < c):
    menor = b
if (c < a and c < b):
    menor = c
    
print('o menor numero é {}'.format(menor))
print('o maior numero é {}'.format(maior))