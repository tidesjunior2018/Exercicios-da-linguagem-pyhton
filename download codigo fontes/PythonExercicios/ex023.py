numero = int(input("Digite um número: "))
n = str(numero)
'''num1 = numero // 1000
auxnum1 = numero % 1000
num2 = auxnum1 // 100
auxnum2 = numero % 100
num3 = auxnum2 // 10
num4 = auxnum2 % 10'''
print("Analisando o número {}".format(numero))
print("\nUnidade : {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(n[3], n[2], n[1], n[0]))
