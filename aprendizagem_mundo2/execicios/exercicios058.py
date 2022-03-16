from random import randint

print(10 * '{}======='.format('\033[35m'))
print('                        JOGO DA ADIVINHAÇAO')
print(10 * '{}======='.format('\033[35m'))

rand = randint(0, 10)
num = int(input('\033[1;36mDigite um numero de 0 a 10: '))

if (num > rand):
    print('\033[1;34mfoi quase! o seu valor foi muito alto!!\033[m\n')

else:
    print('\033[1;34mfoi quase! o seu valor foi muito baixo!!\033[m\n')

cont = 1

while not num == rand:
    cont += 1
    num = int(input('\033[1;31merrou!! tente novamente: \033[m'))

    if (num > rand):
        print('\033[1;34mfoi quase! o seu valor foi muito alto!!\033[m\n')

    elif(num < rand):
        print('\033[1;34mfoi quase! o seu valor foi muito baixo!!\033[m\n')

if(cont == 1):
    print('\033[1;32mvoce acertou de primeira parabems!!!\033[m\n\n\n\n')

elif(cont == 2):   
    print('\033[1;32mdroga! vc ganhou!!\033[m\n\n\n\n')

elif(6 > cont > 2):
    print('\033[1;32mvoce acertou e usou {} tentativas\033[m\n\n\n\n'.format(cont))

else:
    print('\033[1;33mvoce é muito ruim pq uso {} tentativas pra adivinhar\033[m\n\n\n\n'.format(cont))
