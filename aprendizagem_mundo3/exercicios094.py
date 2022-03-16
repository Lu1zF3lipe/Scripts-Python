lista = []
flag = ''
cont = 0
soma = media = 0
listaMulehres = []

while flag  in 'Ss':
    dic = dict()
    dic['nome'] = str(input('nome: '))
    dic['idade'] = int(input('idade: '))
    soma += dic['idade']
    
    while True:
        dic['sexo'] = str(input('sexo [M/F]: ')).upper()
       
        if dic['sexo'] in 'MmFf':
            break
        
        else:
            print('ERRO!! digite apenas M ou F!')
            
    while True:
        flag = str(input('deseja continuar? [S/N]: '))
        
        if flag in 'NnSs':
            break
        
        else:
            print('ERRO!! digite apenas S ou N!')
    
    lista.append(dic.copy())
    del dic
    cont += 1
    
media = soma/cont

print('\nao todo foram cadastradas {} pessoas!'.format(cont))
print('a média de idade é {} anos'.format(media))
print('as mulheres cadastradas foram', end= ' ')
for c in lista:
    if c['sexo'] in 'Ff':
        print(f'{c["nome"]}', end= ' ')
 
print('\nlista das pessoas que estao acima da media: ')
for c in lista:
    if c['idade'] >= media:
        print(' --nome: {}, idade: {}, sexo: {}\n'.format(c['nome'], c['idade'], c['sexo']))
        