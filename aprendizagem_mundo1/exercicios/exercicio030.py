num = int(input('\033[36mdigite um numero: '))
resto = num%2 

print(resto)

if (resto == 0):
    print('\033[32messe numero é par\033[m')
    
else:
    print('\033[31messe numero é inpar\033[m')