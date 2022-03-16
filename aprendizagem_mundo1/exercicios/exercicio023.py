num=int(input('digite um numero:'))

u=num // 1 % 10
d=num // 10 % 10
c=num // 100 % 10
m=num // 1000 % 10

print('analisando esse numero sua:')
print('unidade é: {}'.format(u))
print('dezena é: {}'.format(d))
print('centena é: {}'.format(c))
print('milhar é: {}'.format(m))