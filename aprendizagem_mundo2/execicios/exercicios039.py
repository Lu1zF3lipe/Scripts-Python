from datetime import date

ano = int(input('informe o ano de nascimento: '))
anoAtual = date.today().year
idade = (anoAtual - ano)
alistamento = (ano + 18)

print('quem nasceu em {} tem {} anos em {}'.format(ano, idade, anoAtual))

if (idade > 18):
    print('voce ja deveria ter se alistado ha {} anos!!'.format(anoAtual - alistamento))
    print('seu alistamento foi em {}'.format(alistamento))
elif (idade < 18):
    print('ainda faltam {} anos para seu alistamento!!'.format(alistamento - anoAtual))
    print('seu alistamento sera em {}'.format(alistamento))
elif (idade == 18):
    print('voce deve se alistar imediatamente!!')
