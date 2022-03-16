def isint(msg):
    
    while True:
        num = input(msg)
        
        if num.isnumeric():
            valor = num
            break
        
        else:
            print('\033[31mERRO!!! digite um numero valido.\033[m')
    
    return valor

n = isint('digite um numero: ')
print('voce acabou de digitar o numero: {}'.format(n))
