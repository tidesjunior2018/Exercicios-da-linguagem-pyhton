'''
4-Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''
n = input("Digite algo: ")
print("O tipo primitivo desse valor é: {}".format(type(n)))
print("Está em alfanumerico: {}".format(n.isalnum()))
print("Contem números: {}".format(n.isnumeric()))
print("Está em maiúsculas: {}".format(n.isupper()))
print("Está em minúsculas: {}".format(n.islower()))
print("Está capitalizada: {}".format(n.capitalize()))
