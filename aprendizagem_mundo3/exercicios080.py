num_list = []

for i in range(0, 5):
    num = int(input(('digite um valor: ')))
    if (i == 0 or num >= num_list[-1]):
        num_list.append(num)
        print('adicionado ao final da lista')
    
    else:
        pos = 0
        while pos < len(num_list):
            if num <= num_list[pos]:
                num_list.insert(pos, num)
                print('adicionado na posiçao {} da lista'.format(pos))
                break
            pos += 1  
             
print('os valores digitados foram {}'.format(num_list))