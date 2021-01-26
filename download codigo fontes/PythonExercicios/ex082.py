'''
82-Crie um programa que vai ler vários números e colocar em uma lista.Depois disso,crie duas listas extras que vão conter apenas valores pares e os valores impares digitados,respectivamente.Ao final mostre o conteúdo das três listas geradas.
'''
lista=[]
flag=False

while not flag:
    numero=int(input('Digite um número: '))
    lista.append(numero)

    continuar=str(input('Quer continuar[S/N]: ')).upper()

    if continuar=='N':
        break
print('\n')
print('Lista de numéros pares= ',end='')
for j in lista:
    if j % 2 == 0:
        print(f'{j}',end=' ')
print('\n')
print('Lista de números impares= ',end='')
for k in lista:
    if k % 2 != 0:
        print(f'{k}',end=' ')
print('\n')
print('Lista= ',end='')
for i in lista:
    print(f'{i}',end=' ')
print('\n')