'''
91-Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.Guarde esses resultados em um dicionário.No final coloque o dicionário em ordem,sabendo que o vencedor tirou o maior numero no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
resultado = {'jogador 1': randint(1,6),'jogador 2': randint(1,6),'jogador 3': randint(1,6),'jogador 4': randint(1,6)}

ranking = {}

print()

for r,num in resultado.items():
    print(f'O {r} tirou o numero {num}')
    sleep(1)

print()

ranking = sorted(resultado.items(),key=itemgetter(1),reverse=True)

print(f'   ==Ranking dos Jogadores==')
print('-=-'*20)

for i,v in enumerate(ranking):
    print(f'    O {i+1} lugar foi {v[0]} com o numero {v[1]}')
    sleep(1)

print('-=-'*20)

print()
