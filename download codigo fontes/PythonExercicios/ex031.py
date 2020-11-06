distancia = int(input('Qual a distancia total da viagem?(km) '))
if distancia <= 200:
    print('O preço da passagem vai custar R$ {:.2f}'.format(distancia * 0.50))
else:
    print('O preço da passagem vai custar R$ {:.2f}'.format(distancia * 0.45))
