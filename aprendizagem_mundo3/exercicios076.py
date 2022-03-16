produtos =('lapis', 1.75,
           'boracha', 2,
           'caderno', 15,
           'estojo', 25,
           'transferidor', 4,
           'regua', 5)

print(f'\033[35m{"======" * 10}')
print(f'{"PREÇOS DAS COMPRAS":^60}')
print(f'{"======" * 10}')

for c in range(0, len(produtos), 2):
  print('\033[32m{:.<52}'.format(produtos[c]), end= ' ')
  print('R${:>5.2f}'.format(produtos[c + 1]))

print(f'\033[35m{"======" * 10}\033[m')