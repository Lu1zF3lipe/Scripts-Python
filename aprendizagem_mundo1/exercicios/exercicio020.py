from random import shuffle

n1=input('primeiro nome: ')
n2=input('segundo nome: ')
n3=input('terceiro nome: ')
n4=input('quarto nome: ')

lista=[n1, n2, n3, n4]

shuffle(lista)
print('a ordem de apresentaçao sera:')
print('\n'.join(lista))
