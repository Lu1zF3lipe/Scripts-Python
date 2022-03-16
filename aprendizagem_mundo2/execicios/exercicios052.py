num = int(input('digite um numero: '))
cont = 0

for c in range(1, num +1):
    resto = (num % c)
    
    if(resto == 0):
        cont = cont +1

if(cont == 2):
    print('o numero {} é PRIMO\n'.format(num))
    print('pois é divisivel por: ')

else:
    print('o numero {} nao é primo\n'.format(num))
    print('pois é somente divisivel por: ')

for c in range(1, num +1):
    resto = (num % c)
    
    if(resto == 0):
        print('\033[32m{}'.format(c),end=' ')

    else:
        print('\033[31m{}'.format(c),end=' ')

print('\n\033[m')