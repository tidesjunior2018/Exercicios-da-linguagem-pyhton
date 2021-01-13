'''
74-Crie um programa que vai gerar cinco números aleatórios e colocá-lo em uma tupla.Depois mostre a listagem de números gerados e indique o maior e o menor que estão na tupla.
'''
from random import randint
tupla=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores sorteados são:{tupla}')
for i in range(1,6):
    if i==1:
        maior=tupla[0]
        menor=tupla[0]
    else:
        if tupla[1] > maior:
            maior=tupla[1]
        if tupla[2] > maior:
            maior=tupla[2]
        if tupla[3] > maior:
            maior = tupla[3]
        if tupla[3] > maior:
            maior=tupla[4]
        if tupla[1] < menor:
            menor=tupla[1]
        if tupla[2] < menor:
            menor=tupla[2]
        if tupla[3] < menor:
            menor=tupla[3]
        if tupla[4] < menor:
            menor=tupla[4]
print(f'MAIOR={maior}')
print(f'MENOR={menor}')
