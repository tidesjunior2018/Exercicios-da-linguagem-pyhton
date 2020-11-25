'''
38-Escreva um programa que leia dois números inteiros e compare:
==>O primeiro valor é maior
==>O segundo valor é maior
==>Não existe maior,os dois são iguais
'''

num1=int(input('Digite o primeiro numero: '))
num2=int(input('Digite o segundo numero: '))
if num1 > num2:
    print('O primeiro numero é maior ')
elif num2 > num1:
    print('O segundo numero é maior ')
elif num1==num2:
    print('O dois numeros são iguais ')
