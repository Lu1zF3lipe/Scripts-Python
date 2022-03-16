from time import sleep

num1 = float(input('\033[33mdigite o primeiro valor: \033[m'))
num2 = float(input('\033[33mdigite o segundo valor: \033[m'))

option = 0
cont = 0

print('\033[34mescolha uma opçao:')

while not option == 5:
    cont += 1

    if(cont != 1):
        print('\033[34mo que mais voce dejesa fazer?: ')

    print('''\033[34m
    [1] --> somar
    [2] --> multiplicar
    [3] --> maior
    [4] --> novos numeros
    [5] --> encerrar o programa
    \033[m''')

    option = int(input('\033[1;36mqual a sua opçao?: \033[m'))

    if(option == 1):
        print('\033[32mo resultado de {:.0f} + {:.0f} é {:.0f}\033[m\n'.format(num1, num2, (num1 + num2)))
    
    elif(option == 2):
        print('\033[32mo resultado de {} x {} é {}\033[m\n'.format(num1, num2, (num1 * num2)))
    
    elif(option == 3):
        if(num1 > num2):
            maior = num1

        else:
            maior = num2

        print('\033[32mo maior numero entre {:.0f} e {:.0f} é {:.0f}\033[m\n'.format(num1, num2, maior))
    
    elif(option == 4):
        num1 = float(input('\033[33mdigite o primeiro valor: \033[m'))
        num2 = float(input('\033[33mdigite o segundo valor: \033[m'))
    
    elif(option > 5):
        print('\033[31mopçao invalida!! tente novamente!\033[m')
    print(10 * '{}======='.format('\033[1;33m'))

print('\033[31mFINALIZANDO...\033[m')

for c in range(3, 0, -1):
    print('\033[31m{}...\033[m'.format(c))
    sleep(0.66)

print('\033[31mprograma encerrado!!\033[m')
