from math import factorial

num =  int(input('digite um numero: '))
fatorial = factorial(num)

print('{}! = '.format(num),end='')

for c in range (num, 0, -1):
    print(c, end='')
    if(c != 1):
        print(' x ', end='')
print(' = {}\n\n'.format(fatorial))