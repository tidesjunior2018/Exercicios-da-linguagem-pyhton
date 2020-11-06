from random import randint
soma=0
cont=0

print('{:=^60}'.format('PAR OU IMPAR'))

while True:
    computador = randint(0, 10)
    valor=int(input('Escolha um valor[1 - 10]: '))
    soma+=valor+computador
    print('-'*40)
    if soma%2 == 0:
        print(f'O PC escolheu {computador} e o jogador escolheu {valor}. A soma foi {soma}.DEU PAR!!!')
        print('-' *40)
        print('\nVOCÊ GANHOU!!!')
        soma=0
        cont+=1
    elif soma%2 != 0:
        print(f'O PC escolheu {computador} e o jogador escolheu {valor}. A soma foi {soma}.DEU IMPAR!!! ')
        print('-' * 40)
        print('\nVOCÊ PERDEU!!!')
        break
    print('Vamos jogar novamente.....')
print('-=-'*60)
print(f'\nFIM DO JOGO !!! Você venceu {cont} vezes consecutivas.')