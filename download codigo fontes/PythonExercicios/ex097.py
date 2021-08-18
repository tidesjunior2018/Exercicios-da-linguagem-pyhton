'''
97-Faça um programa que tenha uma função que chamada escreva() que receba um texto qualquer como parâmetro e mostre
na mensagem com tamanho adaptável

EX:
entrada:                     Saida:
                           ----------
escreva('Olá Mundo')       Olá Mundo
                           -----------
'''


def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


escreva('Olá Mundo!!!')
escreva('Aristides Junior')
