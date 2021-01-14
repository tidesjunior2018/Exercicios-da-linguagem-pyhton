'''
80-Crie um programa que leia cinco valores númericos e guarde-os em uma lista,já na posição correta de inserção(sem usar o sort()).No final mostre a lista ordenada na tela. 
'''
lista = list()

for i in range(0, 5):
    num = int(input('Digite um valor:'))

    if i == 0 or num > lista[- 1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print('\n')
print('='*30)
print(f'Os valores digitados em ordem são: {lista}')
print('='*30)
print('\n')
