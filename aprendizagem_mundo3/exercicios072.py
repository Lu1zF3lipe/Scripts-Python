numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('digite um numero de 0 a 20: '))

while True:
  if (numero >= 0 and numero <= 20):
    break
  else:
    numero = int(input('ERRO!!, tente novamente, digite um numero de 0 a 20: '))
  
print('voce digitou o numero {}'.format(numeros[numero]))
