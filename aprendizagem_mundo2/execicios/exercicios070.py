soma = 0
cont_expansive = 0
cont = 0

while True:
  flag = ' '
  print(10 * '{}======'.format('\033[35m'))
  print('                      LOJA BARATAO')
  print(10 * '======')

  name = str(input(('\033[36mnome do produto: ')))
  price = float(input('preço do produto: R$ '))

  while flag not in 'SsNn':
    flag = str(input('quer continuar as compras?')).strip()[0]
  
  soma += price
  cont += 1

  if (price > 1000):
    cont_expansive += 1
  
  
  if(cont == 1 or price < low):
    low = price
    lowname = name
  
  if(flag in 'Nn'):
    break

print(10 * '{}======'.format('\033[32m'))
print('valor total: R$ {:.2f}'.format(soma))
print('total de itens mais caro que R$ 1000,00: {:.2f}'.format(cont_expansive))
print('item mais barato: {}\033[m'.format(lowname))
