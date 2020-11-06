import datetime
ano = int(input('Qual o seu ano de nascimento?'))
anoatual = datetime.date.today().year
idade = anoatual - ano
print('A sua idade é: {} anos e você entra na '.format(idade))

if idade <= 9:
    print('Categoria MIRIM')
elif (idade > 9) and (idade <= 14):
    print('Categoria JUVENIL')
elif (idade > 14) and (idade <= 19):
    print('Categoria JUNIOR')
elif (idade > 19) and (idade <= 25):
    print('Categoria SENIOR')
elif idade > 25:
    print('Categoria MASTER')

