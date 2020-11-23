'''
24-Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.
'''
frase = str(input("Digite a cidade que você nasceu: ")).strip()
frasem = frase.upper()
print('SANTO' in frasem)