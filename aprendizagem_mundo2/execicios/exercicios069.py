cont_idade = 0
cont_homens = 0
cont_mulheres = 0

while True:
  print(10 * '{}======'.format('\033[34m'))
  print('                      CADASTRO DE PESSOAS')
  print(10 * '======')

  idade = int(input(('idade: ')))
  sexo = ' '
  flag = ' '

  while sexo not in 'MmFf':
    sexo = str(input('sexo: ')).strip()[0]
  
  while flag not in 'sSnN':
    flag = str(input('quer continuar? ')).strip()[0]

  if (idade >= 18):
    cont_idade += 1
  
  if (sexo in 'mM'):
    cont_homens += 1
  
  if (sexo in 'Ff' and idade >= 20):
    cont_mulheres += 1

  if (flag in 'nN'):
    break

print('\n\n\033[32mtotal de pessoas cadatradas com mais de 18 anos: {}'.format(cont_idade))
print('ao todo temos {} homens '.format(cont_homens))
print('e temos {} mulheres com menos de 20 anos\033[32m'.format(cont_mulheres))
  