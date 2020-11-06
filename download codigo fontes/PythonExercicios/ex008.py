'''
8-Escreva um valor em metros e exiba convertido em centímetros e milímetros.

                        km hm dam m dm cm mm  
'''
m = float(input('Distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('Uma distância de {:.1f}m corresponde a : '.format(m))
print('Km = {:.4f} \nHm = {:.4f} \nDam = {:.1f} \nDm = {:.0f} \nCm = {:.0f} \nMm = {:.0f}'.format(km, hm, dam, dm, cm, mm))
