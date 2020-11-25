'''
36-Ecreva um programa para aprovar o empréstimo bancário para a compra de uma casa.Pergunte o valor da casa,o salário do comprador e em quantos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou o empréstimo será negado. 
'''

valorcasa = float(input("Qual o valor da casa: R$ "))

salario = float(input("Digite o seu salário: R$ "))

financiamento = int(input("Quantos anos de financiamento: "))

prestacao = valorcasa / (financiamento * 12)

minimo = ((salario * 30) / 100)

print("Para pagar uma casa de R${:.2f} em {} anos "
      ", a prestação será de R${:.2f} ".format(valorcasa, financiamento, prestacao))

if prestacao <= minimo:
    print("EMPRESTIMO ACEITO")
else:
    print("EMPRESTIMO NEGADO")
