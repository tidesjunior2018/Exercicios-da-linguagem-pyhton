'''
40-Crie um programa que leia duas notas de um aluno e calcule sua média,mostrando uma mensagem no final,de acordo com a média atingida.

==>Média abaixo de 5.0 : REPROVADO
==>Média entre 5.0 e 6.9 : RECUPERAÇÃO
==>Média 7.0 ou superior: APROVADO
'''

nome=str(input('Seu nome: '))
nota1=float(input('Nota1: '))
nota2=float(input('Nota2: '))
media=(nota1+nota2)/2
print('O aluno com nome {} de nota {:.1f} e {:.1f} tem média {:.1f} e está ' .format(nome, nota1, nota2, media))
if media >= 7:
    print('APROVADO')
elif media < 5:
    print('REPROVADO')
else:
    print('em RECUPERAÇÂO')
