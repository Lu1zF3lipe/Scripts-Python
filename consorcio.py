valor = int(input("qual o valor mensal do consorcio?: "))
posiçao = int(input("qual a sua posiçao no consorcio?: "))
acressimo = int(input("qual o acressimo mensal do consorcio: "))

valor_total = 0
valor_acressido = valor

for i in range(12):
    valor_total += valor_acressido

    if (i + 1 == posiçao):
        valor_a_receber = valor_acressido*12

    valor_acressido += 3

juros = ((valor_total - valor_a_receber)*100)/valor_total

print("o valor que vc ira receber é: R${:.2f}".format(valor_a_receber))
print("o valor dos juros para a posiçao {}° é {:.1f}%".format(posiçao, juros))
