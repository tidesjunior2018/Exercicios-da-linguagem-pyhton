'''
17-Faça um programa que leia um comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e mostre o comprimento da hipotenusa.

Ex: |   \
    |    \
    |     \
    |      \
    |       \
    |_ _ _ _ \
'''
import math
catetooposto = float(input('Digite o comprimento do cateto oposto: '))
catetoadjacente = float(input('Digite o comprimento do cateto adjacente: '))
'hipotenusa = math.sqrt((catetooposto ** 2) + (catetoadjacente ** 2))'
hipotenusa = math.hypot(catetooposto, catetoadjacente)
print('A hipotenusa é = {:.2f}'.format(hipotenusa))
