valores = []
resp = False

while not resp:

    num = (int(input('Digite um valor:')))

    if num not in valores:
        valores.append(num)
    else:
        print('Valor que já existe !!!')

    continuar = str(input('Quer continuar [S/N]: ')).upper()

    if continuar == 'N':
        resp = True

print('Lista = ', end=' ')
valores.sort()

for i in valores:
    print(f'{i}', end=' ')
