'''
70-Crie um programa que leia o nome e o preço de vários produtos.O programa deverá perguntar se o usuário quer continuar.No final mostre:
A)Qual o total gasto na compra.
B)Quantos produtos custam mais de R$1000,00.
C)Qual é o nome do produto mais barato.
'''
totalcompras=contproduto=menor=contador=0
nomemaisbarato=''
print('{:-^70}'.format('CASAS MARQUES'))
print('\n')
while True:
    print('{:*^20}'.format('PRODUTO'))
    produto=str(input('Nome:'))
    preco=float(input('Preço:R$'))
    contador+=1
    print('*' * 20)
    totalcompras+=preco
    if totalcompras > 1000:
        contproduto+=1
    if contador == 1:
        menor=preco
        nomemaisbarato=produto
    elif preco < menor:
        menor=preco
        nomemaisbarato=produto
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer Continuar[S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^70}'.format('FIM DO PROGRAMA'))
print('*'*66)
print(f'*TOTAL = R$ {totalcompras:.2f}                                                 *')
print(f'*Existem {contproduto} que passa R$ 1000.00                                  *')
print(f'*O nome do produto mais barato foi {nomemaisbarato} que custa R$ {menor:.2f}           *')
print('*'*66)
