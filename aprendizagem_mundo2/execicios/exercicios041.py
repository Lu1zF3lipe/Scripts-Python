from datetime import date

ano = int(input('qual o ano de nascimento do atleta do atleta?: '))
anoAtual = date.today().year
idade = anoAtual - ano

print('o atleta tem {} anos'.format(idade))

if (idade <= 9):
    print('classificaçao: MIRIN')

elif (idade > 9 and idade <= 14):
    print('classificaçao: INFANTIL')

elif (idade > 14 and idade <= 19):
    print('classificaçao: JUNIOR')

elif (idade > 19 and idade <= 25):
    print('classificaçao: SÊNIOR')

elif (idade > 25):
    print('classificaçao: MASTER')