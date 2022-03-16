jogadores = [] 
gols = [] 
flag = ''

while flag in 'Ss':
    jogador = dict()
    jogador['nome'] = str(input('qual é o nome do jogador?: '))
    partidas = int(input('quantas partidas {} jogou?: '.format(jogador['nome'])))

    for c in range(0, partidas):
        gols.append(int(input('quantos gols na partida {}?:'.format(c + 1))))
        
    jogador['gols'] = gols[:]
    jogador['total de gols'] = sum(gols)
    gols.clear()
    
    while True:
        flag = str(input('deseja continuar? [S/N]: '))
        
        if flag in 'NnSs':
            break
        
        else:
            print('ERRO!! digite apenas S ou N!')
            
    jogadores.append(jogador.copy())
    del jogador

print(10 * '\033[32m====')
print(f'{"cod.":<6}{"nome":<}{"gols":>14}{"total":>15}')
print(10 * '\033[32m====\033[m')

for c, i in enumerate(jogadores):
    print(f'{c:<6}', end='')
    for d in i.values():
        print(f'{str(d):<14}', end='')
    print()    
    
print(10 * '\033[32m====\033[m')

while True:
    acum = 0
    resp = int(input('mostra dados de qual jogador? (999 para sair): '))
    
    if resp == 999:
        print('programa encerrado!!!')
        break
    
    if resp >= len(jogadores):
        print('ERROR!! digite um jogador cadastrado!')
    
    else:
        print()
        print(10 * '\033[32m====\033[m')
        print('levantamento do jogador {}:'.format(jogadores[resp]['nome']))
        
        for c, i in enumerate(jogadores[resp]['gols']):
            print('  ==> na partida {} ele fez {} gols'.format(c + 1, i))
            acum += i
        print('e foi um total de {} gols'.format(acum))
        print(10 * '\033[32m====\033[m')
