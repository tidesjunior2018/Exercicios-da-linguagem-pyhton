'''
88-Faça um programa que ajuda um jogador da MEGASENA a criar PAlPITES.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números de 1 a 60 para cada jogo cadastrando em uma lista completa.
'''
import random
numerosaleatorios=[]

numerosjogos=int(input('Quer que eu sorteie quantos jogos:'))

for i in range(0,3):
    sub_numerosaleatorios=[]
    for j in range(6):
        sub_numerosaleatorios.append(random.randint(1,60))
        numerosaleatorios.append(sub_numerosaleatorios)

    print(f'Jogo {i}:{numerosaleatorios}')
    print()