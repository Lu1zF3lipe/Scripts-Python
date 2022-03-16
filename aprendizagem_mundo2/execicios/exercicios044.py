print(10 * '{}======='.format('\033[36m'))
print('                         SIMULADOR DE LOJA')
print(10 * '{}======='.format('\033[36m'))

valor = float(input('preço das compras?: '))

print('FORMA DE PAGAMENTO')
print('[1] -- à vista dinheiro')
print('[2] -- à vista cartao')
print('[3] -- 2x no cartao ')
print('[4] -- 3x ou mais no cartao ')
pagamento = int(input('escolha: '))

if (pagamento == 1):
    print('\033[33mo valor da sua compra foi de R${:.2f}, e com 10% de desconto saira por R${:.2f}\033[m'.format(valor,(valor - (valor * 0.1))))

elif (pagamento == 2):
    print('\033[33mo valor da sua compra foi de R${:.2f}, e com 5% de desconto saira por R${:.2f}\033[m'.format(valor,(valor - (valor * 0.05))))

elif (pagamento == 3):
    print('\033[33msua compra sera parcelada em 2x de R$ {}'.format(valor/2))
    print('o valor da sua compra foi de R${:.2f}\033[m'.format(valor))

elif (pagamento == 4):
    parcelas = float(input('\033[1;36mquantas parcelas?:'))
    valorcomjuros = (valor + (valor * 0.2))
    valordasparcelas = (valorcomjuros / parcelas)
    print('\033[33msua compra sera parcelada em {:.0f}x de R${:.2f} com 20% de juros'.format(parcelas, valordasparcelas))
    print('o valor da sua compra foi de R${:.2f}, e com 20% de juros saira por R${:.2f}\033[m'.format(valor,(valorcomjuros)))

else:
    print('\033[31mescolha uma opçao valida!!\033[m')