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
