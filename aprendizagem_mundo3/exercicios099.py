from time import sleep
from random import randint

def title(msg):
    print(f'\033[35m{"======" * 10}')
    print(f'{msg:^60}')
    print(f'{"======" * 10}\033[m')
    
def search_larger(a):
    cont = maior = 0
    title('analisando os numeros: ')
    
    for c, i in enumerate(a):
        print(i, end=' ', flush=True)
        sleep(0.3)
        
        if cont == 0:
            maior = i
        
        else:
            if i > maior:
                maior = i    
            
        cont += 1
        
    print('\nforam informados {} valores e o maior numero é: {}'.format(cont, maior))

lista = []

for c in range(0, 10):
    lista.append(randint(1, 100))
    
search_larger(lista)
search_larger([1, 2, 3, 5, 7, 10])

lista2 = []

title('valores personalisados:')
print('digite os valores a serem usados: ')

for c in range(0, 10):
    lista2.append(int(input('-')))

search_larger(lista2)