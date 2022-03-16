expression = str(input('digite uma espressao: '))
val = []

for char in expression:
    teste = 0

    if (char == '('):
        val.append('(')
    
    if (len(val) == 0):
        teste = 1

    elif (char == ')'):
        if (len(char) > 0):
            val.pop()
            
if (len(val) == 0 and teste == 0):
    print('a expressao esta correta')

elif (teste == 0 or teste == 1):
    print('a expressao esta errada')  

        