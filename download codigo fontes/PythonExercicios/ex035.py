print('-'*50)
print('ANALISADOR DE TRIANGULO')
print('-'*50)
valor1 = float(input('\nPRIMEIRO SEGMENTO: '))
valor2 = float(input('SEGUNDO SEGMENTO: '))
valor3 = float(input('TERCEIRO SEGMENTO: '))

if valor1 < valor2+valor3 and valor2 < valor1+valor3 and valor3 < valor1+valor2:
    print('\nOs segmentos PODEM FORMAR um triangulo')
else:
    print('\nOs segmentos NÃO PODEM FORMAR um triangulo')
