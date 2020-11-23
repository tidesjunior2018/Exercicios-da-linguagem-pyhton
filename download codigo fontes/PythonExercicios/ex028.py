'''
28-Faça um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.O programa deverá escrever na tela do usuário venceu ou perdeu. 
'''
import random
from time import sleep
print('='*20)
print('Jogo de Advinhação ')
print('='*20)
numero = int(input('\nEm que numero pensei: '))
print('PROCESSANDO....')
sleep(5)
numerosorteado = random.randint(0, 5) #Faz o computador "PENSAR"

if numero == numerosorteado:
    print('Parabéns você acertou !!!')
else:
    print('Ganhei!!! Eu pensei no numero {} e você digitou {}'.format(numerosorteado, numero))
