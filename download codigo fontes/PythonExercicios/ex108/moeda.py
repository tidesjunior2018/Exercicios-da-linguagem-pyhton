def aumentar(p,taxa=0):
    p=p+(p*(taxa/100))
    return p

def diminuir(p,taxa=0):
    p=p-(p*(taxa/100))
    return p

def dobrar(p):
    return p*2

def metade(p):
    return p/2
