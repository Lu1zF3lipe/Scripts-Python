termo1 = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao da sua PG: '))
resultado = termo1

print()

opcao = 1
conttotal = 1

for c in range(1, 9):
    print('{}'.format(resultado), end=' - ')
    conttotal += 1
    resultado = resultado * razao
     

while opcao != 0:
    for c in range(1, opcao + 1):
        conttotal += 1
        resultado = resultado * razao
        print('{}'.format(resultado), end=' - ') 

    print('FIM')
    opcao = int(input('\nquantos termos vc quer mostrar a mais?: '))

print('progressao finalizada com {} termos mostrados\n\n'.format(conttotal))
