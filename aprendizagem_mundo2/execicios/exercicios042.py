print(10 * '{}======='.format('\033[36m'))
print('                      ANALISADOR DE TRIANGULOS')
print(10 * '=======')

a = float(input('primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))

if (a < c + b and b < a + c and c < b + a):
    print('\033[1;32messes segmentos podem formar um triangulo!!\033[m')

    if (a == b and b == c):
        print('\033[34messe triangulo é equilatero\033[m')

    elif(a != b and b != c and a != c):
        print('\033[34messe triangulo é escaleno\033[m')
    
    else:
        print('\033[34messe triangulo é isoceles\033[m')

else:
    print('\033[1;31messes segmentos nao podem formar um triangulo!!\033[m')
