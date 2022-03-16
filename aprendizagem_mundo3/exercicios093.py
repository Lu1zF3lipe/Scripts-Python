jogador = {'nome': [], }
gols = []

jogador['nome'] = str(input('qual é o nome do jogador?: '))
partidas = int(input('quantas partidas {} jogou?: '.format(jogador['nome'])))

for c in range(0, partidas):
    gols.append(int(input('quantos gols na partida {}?:'.format(c + 1))))

print()

jogador['gols'] = gols[:]
jogador['total de gols'] = sum(gols)
totaldegols = sum(gols)

print(jogador)
print()

for c, i in jogador.items():
    print('o campo {} tem o valor {}'.format(c, i))
    
print()

print('o jogador {} jogou {} partidads!!'.format(jogador['nome'], partidas))

for c in range(0, partidas):
    print('  ==> na partida {} ele fez {} gols'.format(c + 1, gols[c]))
print('e foi um total de {} gols\n'.format(totaldegols))