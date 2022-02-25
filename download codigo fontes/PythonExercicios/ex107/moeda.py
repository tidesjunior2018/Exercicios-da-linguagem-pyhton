'''
107-Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),diminuir(),dobrar() e metade().Faca também um programa que importe esse módulo e use algumas dessas funções.
'''


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
