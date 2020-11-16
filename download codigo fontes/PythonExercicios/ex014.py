'''
14-Escreva um programa que converta uma temperatura digitada em °C para °F.
'''

temperaturacelsius = float(input('Qual a temperatura em Cº: '))
fahrenheit = (1.8 * temperaturacelsius) + 32
print('A temperatura em {:.1f}Cº corresponde a {:.1f}Fº'.format(temperaturacelsius, fahrenheit))
