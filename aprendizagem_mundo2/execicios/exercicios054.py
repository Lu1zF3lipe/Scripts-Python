from datetime import date

anoAtual = date.today().year
cont = 0

for c in range(1 , 8):
    nascimento = int(input('em que ano a {}° pessoa nasceu?: '.format(c)))
    idade = anoAtual - nascimento

    if (idade >= 21):
        cont = cont + 1

print('\nao todo tivemos {} pessoas maiores de idade'.format(cont))
print('e tmb tivemos {} pessoas menores de idade\n\n'.format(7 - cont))