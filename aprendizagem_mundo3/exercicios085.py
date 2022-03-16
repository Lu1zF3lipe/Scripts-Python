num = [[],[]]
valor = 0

for i in range(0, 7):
    a = int(input('digite um numero: '))

    if (a % 2 == 1):
        num[0].append(a)
    
    elif (a % 2 == 0):
        num[1].append(a)

print('os valores impares digitados sao: {}'.format(num[0]))
print('os valores pares digitados sao: {}'.format(num[1]))
