'''
26-Faça um programa que leia uma frase pelo teclado e mostre:

==> Quantas vezes aparece a letra "A". 
==> Em que posição aparece a primeira vez. 
==> Em que posição aparece a última vez. 
'''
frase = str(input('Digite uma frase : ')).strip()
frasem = frase.upper()
contadora = frasem.count('A')
print('A letra A aparece {} vezes.'.format(contadora))
acharaletra = frasem.find('A')
print('A primeira letra A começou na posição {}'.format(acharaletra + 1))
acharultimaletra = frasem.rfind('A')
print('A última letra A está na posição {}'.format(acharultimaletra + 1))