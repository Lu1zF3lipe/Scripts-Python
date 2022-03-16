from random import randint
from time import sleep

jogos = []
option = ''
cont = 0

print(10 * '\033[32m======')
print(f"{'PALPITES PARA MEGA SENA':^60}")
print(10 * '\033[32m======\033[m')

while option in 'sS':
    quant = int(input('quantos jogos voce quer?: '))

    for c in range(0, quant):
        jogos.clear()
        cont = 0

        while cont != 6:
            num = randint(1, 60)
            
            if (num not in jogos ):
                jogos.append(num)
                cont += 1

        jogos.sort()
        sleep(1)
        print('palpite {}: {}'.format(c + 1, jogos))
    
    option = str(input('quer jogar mais jogos?: '))

print('BOA SORTE!!!')
