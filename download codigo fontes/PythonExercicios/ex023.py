'''
23-Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

Ex:

Número: 1834

Unidade: 4 dezena: 3 centena: 8 milhar: 1
'''
numero = int(input("Digite um número: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Analisando o número {}".format(numero))
print("\nUnidade : {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(u, d, c, m))
