import math
angulo = int(input('Digite o ângulo que você quer:'))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O seno do ângulo {:.0f}º é = {:.2f}'.format(angulo, seno))
print('O cosseno do ângulo {:.0f}º é = {:.2f}'.format(angulo, cos))
print('A tangente do ângulo {:.0f}º é = {:.2f}'.format(angulo, tang))
