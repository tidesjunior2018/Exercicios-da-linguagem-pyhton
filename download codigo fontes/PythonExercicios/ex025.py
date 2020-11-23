'''
25-Crie um programa que leia o nome de uma pessoa e diga se ela tem o 'SILVA' no nome. 
'''
nome = str(input('Digite seu nome completo: ')).strip()
nomem = nome.upper()
print('Seu nome tem Silva? {}'.format('SILVA' in nomem))
