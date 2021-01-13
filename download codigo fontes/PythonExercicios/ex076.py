'''
76-Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,na sequência.No final mostre uma listagem de preços organizandos os dados de forma tabular
'''
produtos=('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,
          'Transferidor',4.20,'Compasso',9.99)
print('-'*40)
print(f'{"Listagem de Preços":^40}')
print('-'*40)

for posiçao in range(len(produtos)):
    if posiçao % 2 == 0:
        print(f'{produtos[posiçao]:.<30}',end=' ')
    else:
        print(f'RS {produtos[posiçao]:>5.2f}')

print('-'*40)