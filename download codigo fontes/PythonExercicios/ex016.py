'''
16-Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
'''

from math import trunc
num = float(input('Digite um valor: '))
valorporcaointeira = trunc(num)
print('O valor digitado {} na porcão inteira = {}'.format(num, valorporcaointeira))
