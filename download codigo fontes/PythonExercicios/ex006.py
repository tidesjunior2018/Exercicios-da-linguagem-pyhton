'''
6-Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.
'''
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raizquadrada = n ** (1/2)
print('O dobro de {} é = {}, \nO triplo de {} é = {}, \nRaiz Quadrada de {} é = {:.2f}'.format(n, dobro, n, triplo, n, raizquadrada))
