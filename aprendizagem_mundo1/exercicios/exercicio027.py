nome = str(input('escreva seu nome:')).strip().title().split()

print('primeiro nome: {}'.format(nome[0]))
print('ultimo nome: {}'.format(nome[len(nome)-1]))
