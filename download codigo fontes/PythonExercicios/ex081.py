'''
81-Crie um programa que vai ler vários números e colocá-los em uma lista.Depois disso mostre:

a)Quantos números foram digitados.
b)A lista de valores,ordenada de forma decrescente.
c)Se o valor 5 foi digitado e está ou não na lista.
'''

lista=[]
flag=False
cont=0

while not flag:
    num=int(input('Digite um valor: '))
    lista.append(num)
    cont+=1

    continuar=str(input('Quer continuar[S/N]:')).upper()

    if continuar == 'N':
        flag=True

print('-='*40)
if 5 in lista:
    print('O numero 5 está na lista.')
else:
    print('O número 5 não está na lista.')
        
print(f'O usuário digitou {cont} números')
print('A lista de valores digitados ordenada de forma decrescente= ',end=' ')
lista.sort(reverse=True)

for i in lista:
    print(f'{i}',end=' ')
print('\n')
