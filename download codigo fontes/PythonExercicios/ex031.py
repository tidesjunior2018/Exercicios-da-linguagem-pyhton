'''
31-Desenvolva um programa que pergunte a distância de uma viagem em Km.Calcule o preço da passagem cobrando R$ 0,50 por km para viagens de até 200 Km e R$ 0,45 para viagens mais longas.
'''
distancia = int(input('Qual a distancia total da viagem?(km) '))
if distancia <= 200:
    print('O preço da passagem vai custar R$ {:.2f}'.format(distancia * 0.50))
else:
    print('O preço da passagem vai custar R$ {:.2f}'.format(distancia * 0.45))
