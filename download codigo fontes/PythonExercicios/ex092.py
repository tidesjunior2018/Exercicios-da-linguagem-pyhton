'''
92-Crie um programa que leia nome,ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário,se por acaso o CPTS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.Calcule e acrescente além da idade,com quantos anos a pessoa vai se aposentar. 
'''

from datetime import date

trabalhador = {}

trabalhador['nome'] = input('Nome: ').upper()
trabalhador['ano_nascimento'] = int(input('Ano de nascimento:'))
trabalhador['idade'] = date.today().year - trabalhador['ano_nascimento']
trabalhador['CPTS'] = int(input('Carteira de Trabalho(0 não tem):'))

if trabalhador['CPTS'] != 0:
    trabalhador['ano de contratação'] = int(input('Ano de Contratacao: '))
    trabalhador['salario'] = float(input('Salário:R$ '))
    trabalhador['diferença'] = trabalhador['ano de contratação'] - trabalhador['ano_nascimento']    
    trabalhador['aposentadoria'] = trabalhador['diferença'] + 35
    
del trabalhador['ano_nascimento']
del trabalhador['diferença']

print('=-'*10)

for k,v in trabalhador.items():
    print(f' {k} tem valor {v}')

print('=-'*10)

print()