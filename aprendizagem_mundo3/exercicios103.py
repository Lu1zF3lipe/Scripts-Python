def title(msg):
    print(f'\033[35m{"======" * 10}')
    print(f'{msg:^60}')
    print(f'{"======" * 10}\033[m')

def ficha(nome= 'desconhecido', gols=0):
    print('o jogador {} fez {} gols\n\n'.format(nome, gols))
    
title('ficha de jogador')    

n = str(input('digite o nome do jogador: '))
g = str(input('quantos gols o jogador fez?: '))
    
if g.isnumeric():
    g = int(g)
    
else:
    g = 0

if n.strip() == '':
    ficha(gols = g)

else:
    ficha(n, g)
   