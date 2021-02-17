'''
85-Crie um programa onde o usuário possa digitar sete valores númericos e cadastre em uma lista única que mantenha separado valores pares e ímpares.No final,mostre os valores pares e ímpares de forma crescente.
'''
numeros=[[],[]]
for i in range(1,8):
    valor=int(input(f'Digite o {i}° valor:'))
    if valor%2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print()
print('-='*40)
print(f'Lista = {numeros}')
print(f'Os valores pares são: {numeros[0]}')
print(f'Os valores ímpares são: {numeros[1]}')
print('-='*40)
print()