from math import hypot

cat1=float(input('medida do cateto: '))
cat2=float(input('medida do outro cateto: '))

print('a medida da hipotenusa vale {:.2f}'.format(hypot(cat1, cat2)))
