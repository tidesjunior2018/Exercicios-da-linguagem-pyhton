'''
22-Crie um programa que leia um nome completo de uma pessoa e mostre:

==> O nome com todas as letras maiúsculas e minúsculas.
==> Quantas letras ao todo(sem considerar espaços).
==> Quantas letras tem o primeiro nome
'''
nomecompleto = str(input("Digite seu nome completo: "))
nomemaiuscula = nomecompleto.upper()
nomeminuscula = nomecompleto.lower()
tamanhodonome = len(nomecompleto) - nomecompleto.count(" ")
nomedividido = nomecompleto.split()
tamanhodoprimeironome = len(nomedividido[0])
print("\n Analisando o nome.....\n")
print("Seu nome em maiúsculas é : {} \nSeu nome em minúscula é: {}".format(nomemaiuscula, nomeminuscula))
print("Seu nome todo tem {} letras \nSeu primeiro nome é {} e tem {} letras".format(tamanhodonome, nomedividido[0], tamanhodoprimeironome))
