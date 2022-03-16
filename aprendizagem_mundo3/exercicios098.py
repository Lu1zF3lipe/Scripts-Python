from time import sleep

def title(msg):
    print(f'\033[35m{"======" * 10}')
    print(f'{msg:^60}')
    print(f'{"======" * 10}\033[m')

def ctg_prog(c, f, p):
    title('contagem de {} a {} de {} em {}: '.format(c, f, p, p))

    if p < 0:
        p *= -1
    
    if p == 0:
        p = 1
        
    if c < f:
        cont = c
        
        while cont <= f:
            print(cont, end=' ', flush=True)
            cont += p
            sleep(0.5)
        print('FIM!!') 

    elif c > f:
        cont = c
        
        while cont >= f:
            print(cont, end=' ', flush=True)
            cont -= p
            sleep(0.5)
        print('FIM!!')

ctg_prog(1, 10, 1)
ctg_prog(10, 0, 2)

title('contagem personalisada: ')
com = int(input('começo: '))
fim = int(input('fim: '))
passo = int(input('passo: '))

ctg_prog(com, fim, passo)
