from random import randint
from time import sleep
itens=('pedra','papel','tesoura')
computador=randint(0,2)
print('''SUAS OPÇÔES:
0 - PEDRA
1 - PAPEL
2 - TESOURA''')
jogador=int(input('O que você quer jogar: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('='*28)
print('Computador escolheu : {}'.format(itens[computador]))
print('A sua escolha foi : {}'.format(itens[jogador]))
print('='*28)

if computador == 0:#Computador escolheu PEDRA
    if jogador == 0:#Jogador escolheu PEDRA
        print('EMPATE!!!')
    elif jogador == 1:#Jogador escolheu PAPEL
        print('JOGADOR VENCEU!!!')
    elif jogador == 2:#Jogador escolheu TESOURA
        print('COMPUTADOR VENCEU!!!')
    else:
        print('Jogada Inválida!!!!')

elif computador == 1:#Computador escolheu PAPEL
    if jogador == 0:#Jogador escolheu PEDRA
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 1:#Jogador escolheu PAPEL
        print('EMPATE!!!')
    elif jogador == 2:#Jogador escolheu TESOURA
        print('JOGADOR VENCEU!!!')
    else:
        print('Jogada Inválida!!!')

elif computador == 2:#Computador escolheu TESOURA
    if jogador == 0:#Jogador escolheu PEDRA
        print('JOGADOR VENCEU!!!')
    elif jogador == 1:#Jogador escolheu PAPEL
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 2:#Jogador escolheu TESOURA
        print('EMPATE!!!')
    else:
        print('Jogada Inválida!!!')
