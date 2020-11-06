'''
10-Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''
real = float(input('Quanto dinheiro você tem na carteira: R$ '))
dolares = real / 3.95
euro = real / 4.48
print('Você pode comprar com:\nR${:.2f} = U$$ {:.2f}'.format(real, dolares))
print('R${:.2f} = E{:.2f}'.format(real, euro))
