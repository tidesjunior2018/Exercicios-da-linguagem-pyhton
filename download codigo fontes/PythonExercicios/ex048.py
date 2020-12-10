'''
48-Faça um programa que calcule a soma de todos os números impares que são
múltiplos de três e que se encontram no intervalo de 1 até 500
'''
soma=0
cont=0
for c in range(1,500,2):
    if c%3 == 0:
        soma=soma+c
        cont=cont+1
print('A soma de {} valores pedidos é igual a {}'.format(cont,soma))