'''
105-Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes situações:

-Quantidade de notas

-A maior nota

-A menor nota

-A média da turma

-Situação(opcional)

Adiciona também as docstrings

'''

def notas(tam,sit=False):
    """
        -->Função para analisar notas e situações do aluno
    :param tam:aceita várias notas de alunos
    :param sit:valor opcional,mostrando a situação do aluno
    :return:dicionário com as informações sobre a situação da turma
    """
    alunos = dict()
    soma=0
    notas=list()
    for i in range(0, tam):
        notas.append(float(input(f'Digite a nota {i + 1} que você quer colocar:')))
        soma=soma + notas[i]
    media=soma/tam
    alunos['total de notas']=tam
    alunos['media']=media
    alunos['maior']=max(notas)
    alunos['menor']=min(notas)

    if sit:
        if alunos['media']>=7:
            alunos['situacao']='BOA'
        elif alunos['media']<7 or alunos['media']>=5:
            alunos['situacao']='RAZOÁVEL'
        else:
            alunos['situacao']='RUIM'

    return alunos

tam=int(input('Digite quantas notas você quer colocar:'))
turma=notas(tam)
print(turma)
