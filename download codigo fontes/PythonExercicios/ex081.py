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

print(f'O usuário digitou {cont} números')
print(f'A lista de valores digitados ordenada de forma decrescente são:{lista.sort(reverse=True)}

