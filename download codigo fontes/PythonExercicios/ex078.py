'''
78-Faça um programa que leia 5 valores númericos e guarde em uma lista.No final mostre qual foi o maior e o menor valor digitado e suas respectivas posições.
'''
listanumero = list()
maior = 0
menor = 0

for i in range(0,5):
    listanumero.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = listanumero[i]
        pos = i
    else:
        if listanumero[i] > maior:
            maior = listanumero[i]
        if listanumero[i] < menor:
                menor = listanumero[i]

print(f'\nos 5 números digitados são: {listanumero}')
print(f'o maior dentro da lista é: {maior} que fica na posições ',end=' ')
for pos, valor in enumerate(listanumero):
    if valor == maior:
        print(f'{pos}',end=' ')
print('\n')
print(f'o menor dentro da lista é: {menor} que fica na posições ',end=' ')
for pos, valor in enumerate(listanumero):
    if valor == menor:
        print(f'{pos}',end=' ')
