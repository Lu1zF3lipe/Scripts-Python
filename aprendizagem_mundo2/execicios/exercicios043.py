peso = float(input('qual o seu peso?: '))
altura = float(input('qual a sua altura?: '))
imc = (peso/(altura **2))

print('seu imc é {:.1f}'.format(imc))

if (imc < 18.5):
    print('voce esta abaixo do peso')

elif (imc >= 18.5 and imc < 25):
    print('voce esta no peso ideal')

elif (imc >= 25 and imc < 30):
    print('voce esta com sobre peso')

elif (imc >= 30 and imc < 40):
    print('voce esta com obsidade')

elif (imc >= 40):
    print('voce esta com obsidade morbida')