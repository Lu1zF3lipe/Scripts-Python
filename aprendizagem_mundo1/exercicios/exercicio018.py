from math import sin, cos, tan, radians

angulo=float(input('informe o angulo: '))
sen=sin(radians(angulo))
coss=cos(radians(angulo))
tang=tan(radians(angulo))

if angulo == 90:
    print('o seno vale: {:.2f}\no casseno vale {:.2f}\na tangente de 90° nao existe '.format(sen, coss))

else:
    print('o seno vale: {:.2f}\no casseno vale {:.2f}\na tangente vale {:.2f} '.format(sen, coss, tang)) 
