lista_num = []
option = ''

while option in 'Ss':
    num = 0
    num = int(input('digite um numero pra grava-lo: '))
    
    if(num not in lista_num):
        lista_num.append(num)

    else:
        while True:
            num = int(input('ERRO! numero ja cadastrado tente novamente: '))

            if(num not in lista_num):
                lista_num.append(num)
                break

    option = str(input('voce deseja digita mais algum numero?: '))

lista_num.sort()   
print(lista_num)
