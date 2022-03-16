print(10 * '{}======='.format('\033[33m'))
print('                 CONVERSOR DEC --> BIN, OCT, HEX')
print(10 * '=======')

num = int(input('\033[032mdigite um numero qualquer: '))

print('\nescolha uma forma de comversao')
print('1 ----> binario')
print('2 ----> octal')
print('3 ----> hexadecimal')
escolha = int(input('\nqual a forma de conversao?: '))

if (escolha == 1):
    print('\033[31m{} em binario é: {}\033[m\n\n'.format(num, bin(num)[2:]))

elif (escolha == 2):
    print('\033[34m{} em octal é: {}\033[m\n\n'.format(num, oct(num)[2:]))

elif (escolha == 3):
    print('\033[36m{} em hexdecimal é: {}\033[m\n\n'.format(num, hex(num)[2:]))

else:
    print('opçao invalida tente novamente!!\n\n')