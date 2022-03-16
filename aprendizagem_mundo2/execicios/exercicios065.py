soma = 0
cont = 0
Exit = ''

while Exit in 'sS':
    cont += 1
    num = int(input('digite algum valor: '))
    Exit = str(input('quer digitar masi algum valor?: [S/N] '))
    soma += num

    if(cont == 1):
        maior = num
        menor = num
        
    else:
        if(num > maior):
            maior = num

        if(num < menor):
            menor = num

media = soma / cont
print('A media entre os valores é {}'.format(media))
print('o maior dos  valores é {}'.format(maior))
print('o menor dos valores é {}'.format(menor))
