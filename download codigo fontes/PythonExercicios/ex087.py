'''
86-Crie um programa que crie uma matriz de 3X3 e preencha os valores lidos pelo teclado. 
 ______________
|____|____|___|
|____|____|___|
|____|____|___|

No final mostre:

a)A soma de todos os valores pares digitados.
b)A soma de todos os valores da terceira coluna.
c)O maior valor da segunda linha.
'''
matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma=0
terceira_coluna_soma=0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um numero na posição[{linha},{coluna}]:'))
        if matriz[linha][coluna]%2 == 0:
            soma+=matriz[linha][coluna]
        terceira_coluna_soma+=matriz[linha][2]
        if coluna == 0:
            maior_segunda_linha=matriz[1][coluna]
        elif matriz[1][coluna] > maior_segunda_linha:
            maior_segunda_linha=matriz[1][coluna]

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'{matriz[linha][coluna]:^5}',end=' ')
    print()

print(f'A soma de todos os valores pares digitados foi:{soma}')
print(f'A soma de todos os valores da terceira coluna foi:{terceira_coluna_soma}')
print(f'O maior valor da segunda linha é:{maior_segunda_linha}')
print()