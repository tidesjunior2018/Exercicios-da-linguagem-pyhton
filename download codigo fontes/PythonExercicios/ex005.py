'''
5-Faça um programa que leia um número e mostre na tela o seu sucessor e o antecessor.
'''
num = int(input('Digite um numero: '))
ant = num - 1
suc = num + 1
print('Verificando o número {}, o antecessor é {} e o sucessor é {} '.format(num, (num - 1), (num + 1)))
