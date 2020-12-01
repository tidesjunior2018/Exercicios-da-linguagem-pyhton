'''
43-Desenvolva uma lógica que leia o peso e altura de uma pessoa,calcule seu imc e mostre seu status de acordo com a tabela abaixo:

->Abaixo de 18.5:Abaixo do peso     ->25 até 30:Sobrepeso
->Entre 18.5 e 25:Peso ideal        ->30 até 40:Obesidade
                                    ->Acima de 40:Obesidade mórbida
'''
peso=float(input('Qual é o seu peso?(Kg)'))
altura=float(input('Qual é a sua altura?(m²)'))
imc=peso/(altura*altura)
print('O seu indice de massa corporea é de {:.2f} e está '.format(imc),end='')

if imc < 18.5:
    print('abaixo do peso!!!')
elif (imc >= 18.5) and (imc < 25):
    print('com peso ideal!!!')
elif (imc >= 25) and (imc < 30):
    print('com sobrepeso!!!')
elif (imc >= 30) and (imc <= 40):
    print('com obesidade!!!')
elif imc >= 40:
    print('com obsedidade mórbida!!!')