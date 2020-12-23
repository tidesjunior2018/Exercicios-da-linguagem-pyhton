'''
58-Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero
entre 0 e 10.Só que agora vai tentar advinhar até acertar mostrando no final
quantos palpites foram necessários até vencer.
'''
import random
palpite=0
print('\033[33m{:=^40}'.format('JOGO DA ADVINHAÇÂO 2.0'))
print('\033[m')
numerosorteado=random.randint(0,10)
print(numerosorteado)
acertou=False

while not acertou:
    numero=int(input('Digite o valor entre 0 e 10: '))
    palpite+=1
    if numero == numerosorteado:
        acertou=True
    else:
        if numero < numerosorteado:
            print('É maior.Tente mais uma vez!')
        elif numero > numerosorteado:
            print('É menos.Tente mais uma vez!')

print('Você acertou com {} palpites.'.format(palpite))
