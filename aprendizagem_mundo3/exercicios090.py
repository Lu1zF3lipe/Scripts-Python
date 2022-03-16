aluno = {}

aluno['nome'] = str(input('digite o nome do aluno: '))
media = int(input('digite a media do aluno: '))

if (media >= 7):
    situaçao = 'foi aprovado'

elif(7 > media >= 5):
    situaçao = 'ficou de recuperaçao'

elif (media < 5): 
    situaçao = 'foi reprovado'

aluno['media'] = media
aluno['situaçao'] = situaçao

print('o nome do aluno é {}'.format(aluno['nome']))
print('a media do aluno foi: {}'.format(aluno['media']))
print('o aluno {}'.format(aluno['situaçao']))