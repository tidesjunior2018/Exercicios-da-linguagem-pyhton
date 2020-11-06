num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor:'))
if num1 > num2 and num1 > num3:
    maior = num1
    print('Maior é = {}'.format(maior))
else:
    if num2 > num1 and num2 > num3:
        maior = num2
        print('Maior = {}'.format(maior))
    else:
        maior = num3
        print('Maior = {}'.format(maior))

if num1 < num2 and num1 < num3:
    menor = num1
    print('Menor = {}'.format(menor))
else:
    if num2 < num1 and num2 < num3:
        menor = num2
        print('Menor = {}'.format(menor))
    else:
        menor = num3
        print('Menor = {}'.format(menor))