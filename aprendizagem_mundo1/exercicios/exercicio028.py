from random import randint
from time import sleep

print(10 * '{}======='.format('\033[35m'))
print('                        JOGO DA ADIVINHAÇAO')
print(10 * '=======')

num = int(input('\033[1;36mDigite um numero: '))
rand = randint(0,5)

print('\n\033[1;34mPROCESSANDO...\n\n')
sleep(3)

if(num == rand):
    print('\033[1;32mdroga! vc ganhou!!\033[m\n\n\n\n')
    
else:
    print('\033[1;31mhahaha! eu ganhei!!\033[m\n\n\n\n')
