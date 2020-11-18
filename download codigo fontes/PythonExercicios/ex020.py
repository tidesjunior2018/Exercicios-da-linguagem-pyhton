'''
20-O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.
'''
import random
nome1 = input('Primeiro nome: ')
nome2 = input('Segundo nome: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')
lista = [nome1, nome2, nome3, nome4]
ordemdeapresentacao= random.shuffle(lista)
print('A ordem de apresentação: ')
print(lista)
