'''
44-Elabore um programa que calcule um valor a ser pago por um produto,considerando o seu preço normal e a condição de pagamento:

->À vista dinheiro/cheque:10% de desconto       ->Em até 2X no cartão:preço normal
->À vista no cartão:5% de desconto              ->3X ou mais no cartão:20% de juros
'''

print('{:-^50}'.format('SUPERMECADOS EXTRA'))# centralizar
valorprod=float(input('Qual o valor do produto:R$ '))
print('Valor do produto : R$ {:.2f}'.format(valorprod))
print('\n 1-A vista dinheiro / cheque \n 2-A vista no cartao \n 3-2 X no cartão \n 4-3 X ou mais no cartão')
print('-'*50)
print('\n')
op=int(input('Qual a sua opção:'))
if op == 1:
    valorprod2=valorprod - (valorprod * 0.10)
    print('O valor do produto que é R$ {:.2f} com 10% de desconto sai a R$ {:.2f}'.format(valorprod,valorprod2))
elif op == 2:
    valorprod3=valorprod - (valorprod * 0.05)
    print('O valor do produto que é R$ {:.2f} com 5% de desconto sai a R$ {:.2f}'.format(valorprod,valorprod3))
elif op == 3:
    parcela1=valorprod / 2
    print('O valor do produto que é R$ {:.2f} divido em 2X será de R$ {:.2f} SEM JUROS'.format(valorprod,parcela1))
    print('O valor do produto é R$ {:.2f}'.format(valorprod))
elif op == 4:
    parcelas=int(input('Quantas parcelas:'))
    valorprod4=(valorprod + (valorprod * 0.20)) / parcelas
    print('O valor do produto de R$ {:.2f} em {} parcelas será de R$ {:.2f} COM JUROS'.format(valorprod,parcelas,valorprod4))
    valorprod5=valorprod + (valorprod * 0.20)
    print('O valor do produto de R$ {:.2f} com 20% de juros será de R${:.2f}'.format(valorprod,valorprod5))
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!!!')
    valorprod6=valorprod
    print('O valor do produto será de R$ {:.2f}'.format(valorprod6))