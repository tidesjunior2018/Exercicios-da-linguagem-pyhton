'''
86-Crie um programa que crie uma matriz de 3X3 e preencha os valores lidos pelo teclado. 
 ______________
|____|____|___|
|____|____|___|
|____|____|___|

No final mostre a matriz na tela com a formatação correta.
'''
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite o valor da [{linha},{coluna}]:'))
print()
print('-='*40)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'{matriz[linha][coluna]:^5}',end=' ')
    print()
print('-='*40)