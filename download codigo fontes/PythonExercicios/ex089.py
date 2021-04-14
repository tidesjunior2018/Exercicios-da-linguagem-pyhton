'''
89-Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.No final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar a nota de cada um individualmente.
'''

listaAlunos = []
qtdAlunos = 0
continuar = 'S'

while continuar != 'n':
   nome = str(input(f'Entre com o nome do aluno: '))
   nota1 = int(input(f'Entre com a nota 1 do aluno {nome}: '))
   nota2 = int(input(f'Entra com a nota 2 do aluno {nome}: '))
   listaAlunos.append([nome, nota1, nota2])
   qtdAlunos += 1
   continuar = str(input('Quer continuar? [S/n]').lower())
  # continuar = continuar.lower()

for i in listaAlunos:
  media = i[1]+i[2]/2
  print(listaAlunos.index(i),i[0],media)
