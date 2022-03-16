from datetime import date

anoAtual = date.today().year
dados = dict()

dados['nome'] = str(input('o nome da pessoa é?: '))
dados['ano de nascimento'] = int(input('o ano de nascimento da pessoa é?: '))
dados['carteira de trabalho'] = int(input('a carteira de trabalho da pessoa é? (digite 0 caso nao houver!!): '))
dados['idade'] = anoAtual - dados['ano de nascimento'] 

if dados['carteira de trabalho'] != 0:
    dados['ano de contratacão'] = int(input('qual o ano de contrataçao?: '))
    dados['salario'] = float(input('qual o salario?: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano de contratacão'] + 35 ) - anoAtual)
    
print(f'\033[35m{"======" * 10}')
print(f'{"DADOS PESSOAIS":^60}')
print(f'{"======" * 10}\033[m')

for c, i in dados.items():
    if c in 'carteira de trabalho' or c in 'idade' or c in 'aposentadoria':
        print('a {} é: {}'.format(c, i))
    else:
        print('o {} é: {}'.format(c, i))