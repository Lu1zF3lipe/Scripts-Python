from time import sleep
from random import randint

lista = []

def title(msg):
    print(f'\033[35m{"======" * 10}')
    print(f'{msg:^60}')
    print(f'{"======" * 10}\033[m')
    
def num_gem():
    cont = 0
    for c in range(1, 7):
        lista.append(randint(1, 10))

    for c, i in enumerate(lista):
        print(i, end='', flush=True)
        cont += 1
        
        for c in range(1, 4):
            if cont == 6:
                break
            else:
                sleep(0.15)
                print('.', end='', flush=True)
            
    print('\nos numeros sorteados foram: {}'.format(lista), end=' ')
        
def soma_par(a):
    soma = 0
    
    for c, i in enumerate(a):
        if i % 2 == 0:
            soma += i
    
    print('\na soma dos numeros pares é: {}'.format(soma))    

title('gerando numeros')
num_gem()
soma_par(lista)