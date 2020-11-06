'''
7-Desenvolva um programa que leia duas notas do aluno, calcule e mostre a sua média.
'''
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2)/2
print('A média entre {} e {} = {:.1f}'.format(n1, n2, media))
