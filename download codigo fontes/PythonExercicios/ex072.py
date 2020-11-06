lista=('zero','um','dois','tres',
     'quatro','cinco','seis','sete',
     'oito','nove','dez','onze','doze',
     'treze','quatorze','quinze','desesseis',
     'desessete','dezoito','dezenove','vinte')
while True:
    num=int(input('Digite um número entre 0 e 20:'))
    if 0 <= num <= 20:
        break
    print('Tente Novamente!!!',end='')
print(f'Você digitou {lista[num]} por extenso.')
