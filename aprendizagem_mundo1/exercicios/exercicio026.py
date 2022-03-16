frase = str(input('digite uma frase: ')).strip().upper()

print('a letra A apareceu {} vezes'.format(frase.count('A')))
print('a letra A apareceu pela primeira vez em {}'.format(frase.find('A')+1))
print('a letra A apareceu pela ultima vez em {}'.format(frase.rfind('A')+1))

