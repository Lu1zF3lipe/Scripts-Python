cores = ('\033[m' #sem cor
         '\033[30m' #vermelho 
         '\033[31m' 
         )

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('=' * tam )
    print(f'  {msg}')
    print('=' * tam )
    print(cores[0], end='')
    

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('funçao ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    
    else:
        ajuda(comando)

titulo('ate logo', 1)