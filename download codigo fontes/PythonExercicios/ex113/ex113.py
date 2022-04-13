'''
113-Descreva uma função leiaInt() que fizemos no desafio 104 incluindo a possibilidade da digitação de um número do tipo inválido.Aproveite e crie uma função leiaFloat() com a mesma funcionalidade.
'''
from leia import leiaInt
from leia import leiaFloat

n1=leiaInt('Digite um número:')
n2=leiaFloat('Digite um número real:')
print(f'O número inteiro foi : {n1} e o numero real foi: {n2}')
