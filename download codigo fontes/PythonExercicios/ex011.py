'''
11-Faça um programa que leia a altura e a largura de uma parede em metros, calcule a área e a quantidade necessária para pinta-lá, sabendo que cada litro de tinta pinta 2m².
'''

largura = float(input('Largura da parede: '))
altura = float(input('Altura da Parede: '))
area = largura * altura
pintaraparede = area / 2
print('Sua parede tem a dimensão de {}m X {}m tem uma área de {}m²'.format(largura, altura, area))
print('Para pintar a parede você precisará de {}l'.format(pintaraparede))

