'''
96-Faça um programa que tenha uma função chamada área(),que receba as dimensões de terreno retangular(largura X
comprimento) e mostre a área do terreno
'''


def area(largura,comprimento):
    area = largura * comprimento

    print(f'A área total do terreno é {area} m²')


def mostrarlinha():
    print('-'*10)


print('Controle do terreno')
mostrarlinha()
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

area(largura, comprimento)
