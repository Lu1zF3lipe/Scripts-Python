lista_num = []
option = ''

while option in 'sS':
    lista_num.append(int(input('digite um numero: ')))
    option = str(input('deseja continuar?: ')).strip()

print('a quantidade de numeros digitados foram: {}'.format(len(lista_num)))
lista_num.sort(reverse=True)
print('os valores digitados em ordem decrescente sao: {}'.format(lista_num))

if (5 in lista_num):
    print('o 5 faz parte dessa lista!')

else:
    print('o 5 nao faz parte dessa lista!')