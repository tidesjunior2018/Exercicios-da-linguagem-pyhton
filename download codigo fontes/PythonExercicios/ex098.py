'''
98-Faça um programa que tenha uma função chamada contador() que receba três parâmetros: inicio, fim e passo.Seu
programa tem que realizar três contagem através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem persornalizada

'''

from time import sleep


def contador(inicio, fim, passo):

    if passo == 0:
        passo = 1

    if fim == 0:
        fim = -1

    if inicio < fim:
        if passo < 0:
            passo = abs(passo)
        escreva(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        cont = inicio
        fim = fim + 1
        for cont in range(inicio, fim, passo):
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
        print('Fim!!!')

    if inicio > fim:
        if passo > 0:
            passo *= -1
        escreva(f'Contagem de {inicio} até {abs(fim)-1} de {abs(passo)} em {abs(passo)}')
        cont = inicio
        for cont in range(inicio, fim, passo):
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
        print('Fim!!!')
    print()


def escreva(msg):
    tam = len(msg)
    print('-'*tam)
    print(msg)
    print('-'*tam)


#A)
contador(1, 10, 1)
#B)
contador(10, -1, -2)
#C)
escreva('Agora é a sua vez de personalizar')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
