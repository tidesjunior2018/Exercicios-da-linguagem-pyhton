'''
64-Crie um programa que leia varios números inteiros pelo teclado.O programa só vai parar quando o usuário digitar 999,que é a condição de parada.No final,mostre quantos números foram digitados e qual foi a soma (desconsiderando o flag).
'''
soma=0
n=999
flag=False


while not flag:
    num=int(input('Digite um valor[999 para parar]: '))
    if num == n:
        break
    soma = soma + num
print('SOMA = {}'.format(soma))