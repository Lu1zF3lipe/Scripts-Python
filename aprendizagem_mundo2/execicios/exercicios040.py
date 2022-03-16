nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
nota3 = float(input('terceira nota: '))
media = ((nota1 + nota2 + nota3) / 3)

print('a media do aluno foi: {:.1f}'.format(media))

if (media >= 7):
    print('\033[32mo aluno foi APROVADO\033[m')

elif (media < 6.9 and media >= 5):
    print('\033[36mo aluno ficou de RECUPERAÇAO\033[m')

elif (media < 5):
    print('\033[31mo aluno foi REPROVADO\033[m')
