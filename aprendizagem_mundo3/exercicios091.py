from random import randint
from time import sleep
from operator import itemgetter

players = {'player 1':[], 'player 2':[], 'player 3':[], 'player 4':[], }
rank = dict()
cont = 1

input()

for c, i in players.items():
    players[c] = randint(1, 6)

for c, i in players.items():
    print('o jogador {} tirou {}'.format(c, i))
    sleep(0.8)

rank  = sorted(players.items(), key= itemgetter(1), reverse=True)

print(f'\033[35m{"======" * 10}')
print(f'{"RANKING DOS JOGADORES":^60}')
print(f'{"======" * 10}\033[m')

for c, i in enumerate(rank):
    print('{}°: {} tirou {}'.format(c + 1, i[0], i[1]))