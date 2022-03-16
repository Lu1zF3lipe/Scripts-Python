casa = float(input('informe o valor da casa: '))
salario = float(input('informe o seu salario: '))
anos = int(input('em quantos anos voce quer finançiar?: '))

preco_parcela = casa/(anos*12)

if(preco_parcela < (salario * 0.3)):
    print('\033[32mo finaciamento foi aprovado!!\033[m')
    print('o tempo para pagar o finaçiamento é de {} anos, dividos em {} parcelas!'.format(anos, anos*12))
    print('o valor de cada parcela sera de R${:.2f}'.format(preco_parcela))

else:
    print('\033[31mo finaciamento foi negado!!\033[m')
    print('o valor de cada parcela nao pode exceder 30%, cada parcela sera sera de R${:.2f}'.format(preco_parcela))



