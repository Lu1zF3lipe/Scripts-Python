from random import randint
from os import system
from time import sleep


dificult = 0
cores = [
        '\033[32m', #verde
        '\033[36m', #azul
        '\033[31m', #vermelho 
        '\033[33m', #amarelo
         ]
colors = ['verde', 'azul', 'vermelho', 'amarelo']
colororder = list()

def colorgenerator(dificult):
    for i in range(1, 5 + dificult):
        color = randint(0, 3)
        colororder.append(colors[color])
    
    return colororder
    
    
def  displayorder():
    for i, c in enumerate(colororder):
        system('cls')
        
        if c in 'verde':
            print('\033[32m')
            print(c)
            
        if c in 'vermelho':
            print('\033[31m')
            print(c)
            
        if c in 'amarelo':
            print('\033[33m')
            print(c)
            
        if c in 'azul':
            print('\033[36m')
            print(c)
        
        print('\033[m')
        sleep(1)
        system('cls')
        sleep(1)
     
     
def checksenquece(playetorder):
    cont = 0
    global dificult
     
    for i, j in enumerate(colororder):
        for c, f in enumerate(playetorder):
            if(i == c):
                if (j == f):
                    cont += 1
                    
                    if cont == dificult + 4:
                        dificult += 1
                        print('voce passou de level')
                        del colororder[:]
                        
                    break
            
                else:
                    return 1
            
         
while True:
    input('aperte "ENTER" para iniciar')
    
    colororder = colorgenerator(dificult)
    displayorder()
    
    print('nivel de dificuldade: {}'.format(dificult))
    print('digite a ordem correta: ')
    
    playerorder = list()
    
    for i in range(1, 5 + dificult):
        playerorder.append(input(f'{i}° cor: '))
    
    flag = checksenquece(playerorder)
       
    if flag == 1:
        print('voce perdeu, tente novamente!!!')
        print('pontuaçao maxima: ', dificult)
        option = input('deseja reiniciar?: ')
        dificult = 0
        del colororder[:]
        
        if option in 'Nn':
            break
            