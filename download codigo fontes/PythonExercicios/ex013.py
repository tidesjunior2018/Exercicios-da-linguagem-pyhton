salario = float(input('Qual o seu sálario: R$ '))
porcentagem = (salario * 15) / 100
reajustesalario = salario + porcentagem
print('O seu salário R$ {:.2f} com 15% de aumento é: R$ {:.2f}'.format(salario, reajustesalario))
