contmedia = 0
contidademulher = 0

for pessoas in range (1, 5):
    print('digite as informaçoes da {}° pessoa'.format(pessoas))
    nome = str(input('nome: ')).strip()
    idade = float(input('idade: '))
    sexo = str(input('sexo: ')).strip().upper()

    contmedia += idade

    if (sexo == 'MASCULINO' or sexo == 'M'):
        if (pessoas == 1):
            maioridadeM = idade
            nomevelho = nome

        elif (idade > maioridadeM):
            maioridadeM = idade
            nomevelho = nome

    else:
        if (idade < 20):
            contidademulher += 1

print('a media das idades do grupo é igual á: {:.1f}'.format(contmedia/4))
print('o homen mais velho tem {:.0f} anos e se chama {}'.format(maioridadeM, nomevelho))

if (contidademulher == 0):
    print('nao tem mulheres menores de 20 anos')

else:
    print('há {} mulheres menor de 20 anos'.format(contidademulher))