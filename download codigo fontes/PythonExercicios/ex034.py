'''
34-Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00 , calcule um aumento de 10%.Para inferiores ou iguais,o aumento é de 15%.
'''
salario = float(input('Quanto você ganha ? R$ '))
if salario <= 1250:
    salarionovo = salario + (salario * 0.15)
    print('O seu salario com aumento de 15 % é = R${:.2f}'.format(salarionovo))
else:
    salarionovo = salario + (salario * 0.10)
    print('O seu salario com aumento de 10 % é = R${:.2f}'.format(salarionovo))
