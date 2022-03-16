termo1 = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao da sua PA: '))

cont = 1
opcao = 1
conttotal = 1

print(termo1, end=' - ')

while opcao != 0:
    cont = cont - opcao
    while cont != 9:
        cont += 1
        conttotal += 1
        termo1 += razao
        print('{}'.format(termo1), end=' - ') 

    print('FIM')

    opcao = int(input('\nquantos termos vc quer mostrar a mais?: '))
    
print('progressao finalizada com {} termos mostrados\n\n'.format(conttotal))
