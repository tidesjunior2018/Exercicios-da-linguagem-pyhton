'''
108-Adapte o código do desafio 107 criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
'''

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