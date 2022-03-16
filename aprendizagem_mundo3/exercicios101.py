from datetime import date

anoAtual = date.today().year

def voto(ano):
    global cond 
    global idade
    idade = anoAtual - ano
    
    if 16 >= idade < 18 or idade >= 65:
        cond = 'voto opcional'
    
    elif idade < 16:
        cond = 'nao vota'
    
    elif idade >= 18:
        cond = 'voto obrigatorio'
    
    return cond

voto(int(input('digite o ano de nascimento: ')))
print('a idade é {} anos, e a situaçao da pessoa é : {}'.format(idade, cond))