soma = 0

for c in range(1, 7):
    num =int(input('digite {}° valor: '.format(c)))

    if (num%2 == 0):
        soma += num 

print('a soma desse valores é igual á: {}'.format(soma))