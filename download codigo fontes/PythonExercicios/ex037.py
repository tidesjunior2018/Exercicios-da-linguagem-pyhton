'''
37-Escreva um programa que leia um número inteiro qualquer e para o usuário escolher qual será a base de conversão.
==> [1] para binário
==> [2] para octal
==> [3] para hexadecimal
'''

numero=int(input("Digite um numero inteiro: "))
print('''Escolha uma opcão para base de conversao: 
[1] - Converter para BINÁRIO
[2] - Converter para OCTAl
[3] - Converter para HEXADECIMAL''')
opcao=int(input('Digite sua opção: '))
if opcao == 1:
    print('O numero {} covertido para binário é igual {}'.format(numero, bin(numero)[2:]))
elif opcao ==2:
    print('O numero {} convertido para octal é igual {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O numero {} convertido para hexadecimal é igual {}'.format(numero, hex(numero)[2:]))
else:
    print("OPÇÃO INEXISTENTE!!!TENTE NOVAMENTE(1, 2, 3)")

