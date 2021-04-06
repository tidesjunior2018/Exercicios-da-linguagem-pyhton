'''
88-Faça um programa que ajuda um jogador da MEGASENA a criar PAlPITES.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números de 1 a 60 para cada jogo cadastrando em uma lista completa.
'''
from random import randint
from time import sleep
numeros=[]
jogos=[]
print('-'*30)
print('    Sorteio da Mega Sena    ')
print('-'*30)
numerosdejogos=int(input('Quantos jogos você quer que eu sorteie:'))
total=0
while total <= numerosdejogos-1:
    cont=0
    while True:
        num=randint(1,60)
        if num not in numeros:
            numeros.append(num)
            cont+=1
        if cont >= 6:
            break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    total+=1
print()
print('>'*30)
print(f' Sorteando {numerosdejogos} jogos ')
print('>'*30)

for i,n in enumerate(jogos):
    print(f'Jogo {i+1}: {n}')
    sleep(2)
print()
print('-='*5,'Sucesso nos Jogos','-='*5)
print()
