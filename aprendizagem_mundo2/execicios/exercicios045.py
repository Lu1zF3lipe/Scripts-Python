from random import randint
from time import sleep

print(10 * '{}======='.format('\033[31m'))
print('                             JO KEN PO')
print(10 * '{}======='.format('\033[31m'))

comp = randint(0, 2)
itens = ('pedra', 'papel', 'tesoura')

print('''\033[1;32mSuas opçoes:
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')
player = int(input('escolha: '))

if (player == 0 or player == 1 or player == 2):
    print('\n\033[1;36mJO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO\033[m\n')
    sleep(0.5)
#casos em que o compotador ganha
    if ((comp == 0 and player == 2) or (comp == 1 and player == 0) or (comp == 2 and player == 1)):
        print(10 * '{}======='.format('\033[35m'))
        print('                              WINNER')
        print('                            computador')
        print(10 * '{}======='.format('\033[35m'))
#caso em que o jogador ganha
    elif ((player == 0 and comp == 2) or (player == 1 and comp == 0) or (player == 2 and player ==1)):
        print(10 * '{}======='.format('\033[35m'))
        print('                              WINNER')
        print('                              player')
        print(10 * '{}======='.format('\033[35m'))

    else:
        print(10 * '{}======='.format('\033[35m'))
        print('                              EMPATE')
        print(10 * '{}======='.format('\033[35m'))

    print('o computador jogou {} e o player jogou {} \n\n'.format(itens[comp], itens[player]))
else:
    print('\033[31mescolha uma opçao valida!\033[m')