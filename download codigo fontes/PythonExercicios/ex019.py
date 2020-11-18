'''
19-Um professor quer sortear um dos seus quatros alunos para apagar o quadro.Faça um programa que ajude ele,lendo o nome deles e escrevendo o nome escolhido.
'''
import random
nome1 = input('Primeiro nome: ')
nome2 = input('Segundo nome: ')
nome3 = input('Terceiro nome:')
nome4 = input('Quarto Nome: ')

lista = [nome1, nome2, nome3, nome4]

escolhido = random.choice(lista)
print('\nO escolhido pelo professor foi {}'.format(escolhido))
