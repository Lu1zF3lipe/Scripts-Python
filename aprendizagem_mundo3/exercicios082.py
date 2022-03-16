list_main = []
list_odd = []
list_even = []
option = ''

while option in 'Ss':
    list_main.append(int(input('digite um numero: ')))
    option = str(input('quer continuar?: ')).strip()

for c, i in enumerate(list_main):
    if (i % 2 == 0):
        list_even.append(i)
    
    elif (i % 2 == 1):
        list_odd.append(i)

print('os valores digitados foram: {}'.format(list_main))
print('os valores impares sao: {}'.format(list_odd))
print('os valores pares sao: {}'.format(list_even))