def title(msg):
    tam = len(msg) + 6
    print(f'\033[35m{"="}' * tam)
    print(f'   {msg}')
    print(f'{"="}' * tam, end= '')
    print('\033[m')
    
title('luiz felipe')
title('curso de python')
title('CeV')