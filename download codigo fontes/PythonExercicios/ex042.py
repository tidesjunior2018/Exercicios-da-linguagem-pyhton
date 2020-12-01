'''
42-Refaça o desafio 35 dos triângulos,acrescentando o recurso de mostrar que tipo de triângulo será formado.

==>Equilátero:Todos os lados iguais. 
==>Isósceles:Dois lados iguais.
==>Escaleno:Todos os lados diferentes.
'''

print('-'*50)
print('ANALISADOR DE TRIÂNGULO VERSÂO 2.0')
print('-'*50)
print('\n')
valor1=float(input('Digite o primeiro segmento: '))
valor2=float(input('Digite o segundo segmento: '))
valor3=float(input('Digite o terceiro segmento: '))

if valor1 < valor2 + valor3 and valor2 < valor1 + valor3 and valor3 < valor1 + valor2:
    print('Podem formar um triângulo ', end='')
    if valor1 == valor2  and valor1 == valor3 and valor2 == valor3:
        print('EQUILÁTERO!!!')
    if valor1 == valor2 and valor2 != valor3 or valor1 == valor3 and valor3 != valor2 or valor2 == valor3 and valor3 != valor1:
        print('ISOSCELES!!!')
    if valor1 != valor2 and valor2 != valor3 and valor1 != valor3:
        print('ESCALENO!!!')
else:
    print('os lados não podem formar um triangulo')
