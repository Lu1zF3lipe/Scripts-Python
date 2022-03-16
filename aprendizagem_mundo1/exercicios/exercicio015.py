dias=float(input('por quantos dias o carro foi alugado?: '))
km=float(input('quantos km foram rodados?: '))

ppd=dias*60 #ppd=preço por dia
ppk=km*0.15 #ppk=preço por km

print('o aluguel do carro vai custar R${:.2f}'.format(ppd+ppk))
