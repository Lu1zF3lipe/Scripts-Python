distancia = float(input('qual a distancia da sua viagem?: '))

if (distancia <= 200):
    print('sua viagem vai custar R${:.2f}'.format(distancia * 0.5))
else:

    print('sua viagem vai custar R${:.2f}'.format(distancia * 0.45))

