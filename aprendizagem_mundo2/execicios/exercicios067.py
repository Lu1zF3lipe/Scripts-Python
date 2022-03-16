while True:
  print()
  print(10 * '{}======'.format('\033[36m'))
  print('                        TABUADA')
  print(10 * '======')

  tabuada = int(input('tabuada: '))
  print()

  if (tabuada <= 0):
    break

  for resutados in range(1, 11):
    print('\033[1;32m{} X {} = {}'.format(tabuada, resutados, (resutados * tabuada)))

print('\033[31mfim do programa\033[m')
