'''
89-Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.No final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar a nota de cada um individualmente.
'''
dados=list()
nomes=list()
notas=list()

num_alunos=int(input('Quantos alunos você deseja:'))

for i in range(0,6):
    nome=str(input('Nome:'))
    nomes.append(nome)
    nota1=int(input(f'Qual a 1°nota do {nome}:'))
    notas.append(nota1)
    nota2=int(input(f'Qual a 2° nota do {nome}'))
    notas.append(nota2)
    dados.append(nomes[:])
    dados.append(notas[:])
    nomes.clear()
    notas.clear()

for c in dados:
    print(c)
