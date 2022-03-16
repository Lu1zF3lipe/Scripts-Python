nome=str(input('digite seu nome completo: ')).strip()

print('seu nome em maiusculas é: {}'.format(nome.upper()))
print('seu nome em minusculas é: {}'.format(nome.lower()))
print('seu nome tem {} letras'.format((len(nome)-nome.count(' '))))

separa=nome.split()

print('seu primeiro nome é {} e tem {} letras'. format(separa[0], len(separa[0])))