import random
from time import sleep
print('='*130)
print('Jogo de Advinhação ')
print('='*130)
numero = int(input('\nEm que numero pensei: '))
print('PROCESSANDO....')
sleep(5)
numerosorteado = random.randint(0, 5)

if numero == numerosorteado:
    print('Parabéns você acertou !!!')
else:
    print('Ganhei!!! Eu pensei no numero {} e você digitou {}'.format(numerosorteado, numero))
