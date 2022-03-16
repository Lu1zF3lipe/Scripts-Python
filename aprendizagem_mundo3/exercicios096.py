
def calc_area(a, b):
   area = a * b
   print('a area do terreno é {}m²'.format(area))

def title(msg):
    print(f'\033[35m{"======" * 10}')
    print(f'{msg:^60}')
    print(f'{"======" * 10}\033[m')

title('calculadora de area')

b = float(input('largura(M): '))
a = float(input('comprimento(M): '))

calc_area(a, b)