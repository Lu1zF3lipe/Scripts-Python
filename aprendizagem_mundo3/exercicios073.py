tabela = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Internacional', 'Corinthians', 'Fluminense', 'Atlético-GO','América-MG', 'Cuiabá', 'Athletico-PR', 'São Paulo', 'Ceará', 'Bahia', 'Santos', 'Juventude', 'Sport', 'Grêmio', 'Chapecoense')

print('clasifiçao do brasileirao:')
for c in range(0, 20):
  if c >= 0 and c <= 5:
    print('\033[32m{}°: {}'.format(c + 1, tabela[c]))
  elif c >= 5 and c <= 15:
    print('\033[33m{}°: {}'.format(c + 1, tabela[c]))
  else:
    print('\033[31m{}°: {}'.format(c + 1 , tabela[c]))
  
print('\033[34mos cinco primeiros colocados sao: {}'.format(', '.join(tabela[0:6])))
print('os quatro ultimos colocados sao: {}'.format(', '.join(tabela[16:])))
print('os times em ordem alfabetica: \n{}\033[m'.format('\n'.join(sorted(tabela))))