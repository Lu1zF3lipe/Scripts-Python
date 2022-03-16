speed = float(input('qual a velocidade?: '))
multa = (speed - 80) * 7

if (speed > 80):
    print('\033[31mMULTADO!!! voce excedeu o lmite de velocidade de 80km/h\nvoce deve pagar uma multa de R${}\033[m'.format(multa))
else:

    print('\033[32mtenha um bom dia! dirija com cuidado!!\033[m')
