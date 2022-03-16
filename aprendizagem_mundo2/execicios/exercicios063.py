print(10 * '\033[36m=======')
print('                       SEQUENCIA DE FIBONACHI')
print(10 * '=======')

termos = int(input('\033[32mquantos termos vc deseja na sua sequencia?: '))

t1 = 0
t2 = 1
cont = 1

print('{} - {}'.format(t1, t2), end=' - ')

while cont <= termos - 2:
    cont += 1
    t3 = t1 + t2
    print('{}'.format(t3), end=' - ')
    t1 = t2
    t2 = t3 
print('FIM\033[m')
