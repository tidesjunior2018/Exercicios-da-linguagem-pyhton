'''
29-Escreva um programa que leia a velocidade do carro.Se ele utrapassar 80Km/h,mostre dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite. 
'''
velocidadedocarro = int(input('Digite a velocidade atual do carro: '))
if velocidadedocarro > 80:
    print('MULTADO !!! Você excedeu o limite de 80 km/h')
    multa = (velocidadedocarro - 80) * 7
    print('O valor da multa é = R$ {:.2f}'.format(multa))
print('Bom Dia !!! Lembre - se do cinto de segurança')