'''
98-Faça um programa que tenha uma função chamada contador() que receba três parâmetros: inicio, fim e passo.Seu
programa tem que realizar três contagem através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem persornalizada

'''

from time import sleep


def contador(inicio, fim, passo):

    if inicio > fim:
        passo *= -1
    elif inicio > fim and passo < 0:
        passo *= 1
    elif inicio < fim and passo < 0:
        passo *= -1

    for cont in range(inicio, fim, passo):
        print(f'{cont}', end=' ', flush=True)
        sleep(0.5)
    print()


def escreva(msg):
    tam = len(msg)
    print('-'*tam)
    print(msg)
    print('-'*tam)


#A)
escreva('Contagem de 1 até 10, de 1 em 1')
contador(1, 11, 1)
#B)
escreva('Contagem de 10 até 0, de 2 em 2')
contador(10, -1, 2)
#C)
escreva('Agora é a sua vez de personalizar')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
escreva(f'Contagem de {inicio} até o {fim} de {passo} em {passo}')
contador(inicio, fim, passo)
