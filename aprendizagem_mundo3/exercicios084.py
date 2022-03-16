dados = []
pessoas = []
option = ''
cont = 0
maior = []
menor = []

while option in 'Ss':
    cont += 1
    dados.append(str(input('digite nome da pessoa: ')))
    dados.append(float(input('digite o peso da pessoa: ')))
    pessoas.append(dados[:])
    option = (str(input('quer adicionar outra pessoa?: ')))
    dados.clear()

for c, i in enumerate(pessoas):
    if (c == 0):
        maior.append(i)
        maiorpeso = maior[0][1]

    elif (i[1] == maior[0][1]):
        maior.append(i)

    elif (i[1] > maior[0][1]):
        maior.clear()
        maior.append(i)
    
    if (c == 0):
        menor.append(i)
        menorpeso = menor[0][1]

    elif (i[1] == menor[0][1]):
        menor.append(i)

    elif (i[1] < menor[0][1]):
        menor.clear()
        menor.append(i)

print('foram cadastrados {} pessoas'.format(cont))
print('as pessoas mais pesadas pesam {:.2f} KG e foram'.format(maior[0][1]), end= ' ')
for c, i in enumerate(maior):
    print(i[0],end= ' ')
print()

print('as pessoas mais leves pesam {:.2f} KG e foram'.format(menor[0][1]), end= ' ')
for c, i in enumerate(menor):  
    print(i[0],end=' ')
print()
