boletim = []
lista = []
media = 0
nota1 = 0
nota2 = 0
nome = ''

print(10 * '\033[32m====')
print(f'{"Boletim escolar":^40}')
print(10 * '\033[32m====\033[m')

for c in range(0, 3):
    nome = str(input('nome: '))
    nota1 = int(input('nota 1: '))
    nota2 = int(input('nota 2: '))
    print()

    media = nota1 + nota2/2

    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    lista.append(media)
    boletim.append(lista[:])
    lista.clear()

print(10 * '\033[32m====')
print(f'{"No.":<10}{"nome":^15}{"media":>15}')
print(10 * '\033[32m====\033[m')

for i in range(0 ,3):
    print(f'{i:<10}{boletim[i][0]:^15}{boletim[i][3]:>15}')

print(10 * '\033[32m====\033[m')

flag = 0

while True:
    flag = int(input('\ndeseja ver as notas de qual aluno? (999 para encerrar): '))

    if (flag == 999):
        break

    print('as notas do aluno {} sao {} e {}'.format(boletim[flag][0], boletim[flag][1], boletim[flag][2]))

print('programa encerrado!!')