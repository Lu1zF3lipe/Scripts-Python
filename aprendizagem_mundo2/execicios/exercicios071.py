while True:
  notas = 0
  resto = 0
  cont = 0
  flag = ' '

  print(10 * '{}======'.format('\033[35m'))
  print('                      BANCO DO LUIZ')
  print(10 * '======')

  value = int(input('\033[33mquanto voce quer sacar?: '))
  cedulas = [200, 100, 50, 20, 10, 5, 1]

  for c in range(0, 6):
    if(cont == 0):
      notas = value // cedulas[c]
      resto = value % cedulas[c]
      cont += 1

      if (notas != 0):
        print('\033[34mtotal de {} cedulas de {}'.format(notas, cedulas[c]))

    if(cont != 0 and resto != 0):
      notas = resto // cedulas[c + 1]
      resto = resto % cedulas[c + 1]

      if (notas != 0):
        print('\033[34mtotal de {} cedulas de {}'.format(notas, cedulas[c + 1]))

    if resto == 0:
      break

  print(10 * '{}======'.format('\033[31m'))

  while flag not in 'NnSs':
    flag = str(input('\033[31mvoce dejesa sacar mais dinheiro?: ')).strip()[0]
  
  if (flag in 'Nn'):
    break
  
  print('\033[32mprograma caixa eletronico encerrado com sucesso, volte sempre!!\033[m')
