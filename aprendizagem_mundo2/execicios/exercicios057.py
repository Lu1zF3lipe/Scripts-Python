sexo = str(input('qual é o seu sexo?: ')).upper().strip() [0]

while not sexo in 'FM':
    sexo = str(input('valores invalidos, tente novamente: ')).upper().strip() [0]

if(sexo == 'M'):
    print('sexo masculino resgistrado com sucesso')

else: 
    print('sexo feminino resgistrado com sucesso')