diascarrosalugados = int(input('Quantos dias o carro foi alugado: '))
kmrodados = float(input('Quantos km rodados: '))
totaldias = diascarrosalugados * 60
totalkmrodados = kmrodados * 0.15
preco = totaldias + totalkmrodados
print('O preço a pagar é : R$ {:.2f}'.format(preco))