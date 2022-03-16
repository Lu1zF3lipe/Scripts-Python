soma = 0
values = 0

while values != 999:
    values = int(input('digite algum valor:'))

    if (values != 999):
        soma += values
print('a soma dos valores digitados é {}'.format(soma))