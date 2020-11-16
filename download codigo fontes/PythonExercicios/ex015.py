'''
15-Faça um programa que pergunte a quantidade de km pecorridos de um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar,sabendo que o carro custa R$60 reais por dia e R$0.15 por km rodados.
'''

diascarrosalugados = int(input('Quantos dias o carro foi alugado: '))
kmrodados = float(input('Quantos km rodados: '))
totaldias = diascarrosalugados * 60
totalkmrodados = kmrodados * 0.15
preco = totaldias + totalkmrodados
print('O preço a pagar é : R$ {:.2f}'.format(preco))