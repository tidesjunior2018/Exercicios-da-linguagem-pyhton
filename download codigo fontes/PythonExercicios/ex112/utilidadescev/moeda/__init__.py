def aumentar(p=0,taxa=0):
    res=p+(p*(taxa/100))
    return res

def diminuir(p=0,taxa=0):
    res=p-(p*(taxa/100))
    return res

def dobrar(p=0):
    res=p*2
    return res

def metade(p=0):
    res=p/2
    return res

def moeda(p=0,moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')

def resumo(p=0,taxa=0):
    print('-'*30)
    print('Resumo do Valor'.center(30))
    print('-'*30)
    print(f'Valor analisado:{moeda(p)}')
    print(f'Valor com reajuste de {taxa}% = {moeda(aumentar(p,taxa))}')
    print(f'Valor com desconto de {taxa}% = {moeda(diminuir(p,taxa))}')
    print(f'Dobro do preço:{moeda(dobrar(p))}')
    print(f'Metade do preço:{moeda(metade(p))}')
    print(f'-'*30)