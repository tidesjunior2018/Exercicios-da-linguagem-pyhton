'''
84-Faça um programa que leia o nome e o peso de várias pessoas guardando tudo em uma lista.No final mostre:

A)Quantas pessoas foram cadastradas.
B)Uma listagem com as pessoas mais pesadas.
C)Uma listagem com as pessoas mais leves.

'''

pessoas=list()
dado=list()
totalpessoas=0
flag=False
maior=menor=0

while not flag:
    dado.append(str(input('Nome:')))
    dado.append(float(input('Peso:')))
    totalpessoas+=1

    if totalpessoas == 1:
        maior=menor=dado[1]
    else:
        if dado[1] > maior:
            maior=dado[1]
        if dado[1] < menor:
            menor = dado[1]

    pessoas.append(dado[:])
    dado.clear()
    resp=str(input('Quer continuar[S/N]: ')).upper()

    if resp=='N':
        break

print('=-'*30)
print('Pessoas = ',end='')
for p in pessoas:
    print(f'{p}',end='')
print('\n')
print(f'Foram cadastradas {totalpessoas} pessoas')
print(f'O maior peso foi de {maior}Kg')
print(f'O menor peso foi de {menor}Kg')
print('=-'*30)
print('\n')