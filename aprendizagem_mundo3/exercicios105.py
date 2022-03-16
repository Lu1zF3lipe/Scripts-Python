def notas(*n, sit=False):
    aluno = dict()
    aluno['maior']= max(n)
    aluno['menor']= min(n)
    
    acum = cont = 0
    for c in range(len(n)):
        cont += 1
        acum += n[c]
    
    aluno['total']= cont
    aluno['media']= acum/cont
    
    if sit == True:
        
        if aluno['media'] >= 7:
            aluno['situaçao']= 'OTIMA'
            
        elif 7 > aluno['media'] >= 6:
            aluno['situaçao']= 'BOA'
            
        elif aluno['media'] < 6:
            aluno['situaçao']= 'RUIM'
            
    return aluno

resp = notas(5, 6, 4, 6, 7, sit=True)
print(resp)