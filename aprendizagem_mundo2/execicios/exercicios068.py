from random import randint

print(10 * '{}======'.format('\033[36m'))
print('                        TABUADA')
print(10 * '======')

cont = 0

while True:
  choice_player = ' '
  player = int(input(('\033[33mdigite um valor: ')))
  computer = randint(0,10)

  total= computer + player
  result = total % 2

  while choice_player not in 'PpIi':
    choice_player = str(input('voce quer par ou impar?: ')).strip()[0]

  print('o jogador usou {} e o computador usou {}.'.format(player, computer))

  if (result == 0):
    print('deu PAR...')
    
  else:
    print('deu IMPAR...')
    
  if(choice_player in 'Pp' and result == 0):
    print('o jogador venceu!!\n')
    cont += 1
  
  elif (choice_player in 'Ii' and result == 1):
    print('o jogador venceu!!\n')
    cont += 1

  else:
    break

  print(10 * '{}======'.format('\033[35m'))
  print('\033[35mvamos jogar novamente...')

print()
print(10 * '{}======'.format('\033[31m'))
print('GAMER OVER!!! o computador vencceu!')
print('\033[32mo jogador venceu {}\033[m'.format(cont))
  