'''
89-Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.No final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar a nota de cada um individualmente.
'''

listaAlunos = []
qtdAlunos = 0
continuar = 'S'

while continuar != 'n':
   nome = str(input(f'Entre com o nome do aluno: '))
   nota1 = float(input(f'Entre com a nota 1 do aluno {nome}: '))
   nota2 = float(input(f'Entra com a nota 2 do aluno {nome}: '))
   listaAlunos.append([nome, nota1, nota2])
   qtdAlunos += 1
   continuar = str(input('Quer continuar? [S/n]').lower())
  # continuar = continuar.lower()

print(f'{"N°":<4}{"NOME:":<10}{"MEDIA:":>8}')
for i in listaAlunos:
  media = (i[1]+i[2])/2
  print(f'{listaAlunos.index(i):<4}{i[0]:<10}{media:>8.1f}')

while True:
    opc=int(input('Você que ver as notas de que aluno: (999 para interromper)'))
    if opc == 999:
        print('Finalizando...')
        break
    if opc < len(listaAlunos):
        print(f'Notas de {listaAlunos[opc][0]} são {listaAlunos[opc][1]} e '
              f'{listaAlunos[opc][2]}')
print('<<<','Volte Sempre!!!','<<<')
