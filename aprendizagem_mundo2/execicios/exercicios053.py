nome = str(input('digite uma frase: ')).strip().upper().split()
nome =''.join(nome)

inverso = ''

for cont in range (len(nome) - 1, -1, -1):
    inverso += nome[cont]

print('a frase {} invertida fica: {}'.format(nome, inverso), end='')

if(inverso == nome):
    print('\nessa frase é um palindromo')
else:
    print('\nessa frase nao é um palindromo')
