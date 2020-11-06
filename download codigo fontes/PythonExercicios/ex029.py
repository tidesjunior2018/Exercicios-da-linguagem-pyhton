velocidadedocarro = int(input('Digite a velocidade atual do carro: '))
if velocidadedocarro > 80:
    print('MULTADO !!! Você excedeu o limite de 80 km/h')
    multa = (velocidadedocarro - 80) * 7
    print('O valor da multa é = R$ {:.2f}'.format(multa))
print('Bom Dia !!! Lembre - se do cinto de segurança')