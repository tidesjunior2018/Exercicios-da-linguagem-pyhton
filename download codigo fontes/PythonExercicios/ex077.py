'''
77-Crie um programa que tenha uma tupla com várias palavras(não usar acentos).Depois disso,você deve mostrar,para cada palavra quais são suas vogais.
'''
palavras=('AMIGO','BOLA','ESCOLA','FACULDADE','RELOGIO')
for p in palavras:
    print(f'\n\033[37m Na palavra {p} temos :',end=' ')
    for letra in p:
        if letra in 'AEIOU':
            print(f'\033[34m{letra}',end=' ')
print('\n\033[37m')
