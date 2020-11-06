salario = float(input('Quanto você ganha ? R$ '))
if salario <= 1250:
    salarionovo = salario + (salario * 0.15)
    print('O seu salario com aumento de 15 % é = R${:.2f}'.format(salarionovo))
else:
    salarionovo = salario + (salario * 0.10)
    print('O seu salario com aumento de 10 % é = R${:.2f}'.format(salarionovo))
