frase = input('escreva seu nome:')
tipo= input('seu nome é composto?')
frase = frase.title().split()
if tipo==('sim'):
    print('primeiro nome:',' '.join(frase[0:2]))
    print('segundo nome:', frase[2])
    print('terceiro nome:',' '.join(frase[3:]))
else:
    print('primeiro nome:',frase[0])
    print('segundo nome:', frase[1])
    print('terceiro nome:',' '.join(frase[2:]))








