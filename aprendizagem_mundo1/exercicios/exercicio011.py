a=float(input('digite a largura: '))
b=float(input('digite o comprimento: '))

area=a*b
litros_tinta=area/2

print('sua parede tem a dimensao de {}m x {}m e a area mede {:.2f}m²'.format(a, b, area))
print('para pintar essa parede, voce precisara de {:.2f} litros de tinta'.format(litros_tinta))
