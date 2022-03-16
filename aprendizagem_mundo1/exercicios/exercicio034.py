salario = float(input('qual o salario do funcionario: '))
reajuste = salario * 0.10 

if (salario <= 1250):
    reajuste = salario * 0.15
    
print('o funcionario passara a receber R${:.2f}'.format(salario + reajuste))