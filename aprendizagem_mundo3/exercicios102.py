from math import factorial

def fatorial(num, show=False):
    """calculo do fatorial
    

    Args:
        num (int): numero que se deseja calcular o fatorial
        show (bool, optional): opçao para se ver o calculo do fatorial. Defaults to False.

    Returns:
        int: o resutado do fatorial
    """
    
    resut = factorial(num)
    
    if show == True:
        cont = 0
        comeco = num
        
        while comeco >= 1:
            print(comeco, end='')
            comeco -= 1
            cont += 1
            
            for c in range(0, num):
                if cont == num:
                    print('=',end='')
                    break
                else:
                    print('x',end='')
                    break
                
        print(resut)

    return resut

num = int(input('digite um numero: '))
print('o fatorial de {} é: {}'.format(num, factorial(num)))

option = str(input('deseja ver o calculo? [S/N]: '))
if option in 'sS':
    fatorial(num, True)