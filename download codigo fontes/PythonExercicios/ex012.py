produto = float(input('Qual o preço do produto: R$'))
porcentagem = (produto * 5) / 100
resultadofinal = produto - porcentagem
print('O produto com valor de R${:.2f} na promoção de 5% sai a R${:.2f}'.format(produto, resultadofinal))