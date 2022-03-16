print(10 * '{}======='.format('\033[36m'))
print('                                TABUADA')
print(10 * '{}======='.format('\033[36m'))

tabuada = int(input('tabuada: '))
print('')

for resutados in range(0, 11):
    print('\033[1;36m{} X {} = {}'.format(tabuada, resutados, (resutados * tabuada)))
print('FIM\033[m\n\n')