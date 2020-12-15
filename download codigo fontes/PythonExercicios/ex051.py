'''
51-Desenvolva um programa que leia o primeiro termo e a razão de uma PA.No
final mostre os 10 primeiros termos dessa progressão.
'''

print('{:=^40}'.format('10 termos de uma P.A'))# centralizar
primeirotermo=int(input('Digite o primeiro termo: '))
print('\n')
razao=int(input('Digite a razão:'))
for n in range(1,11):
    pa=primeirotermo+(n-1)*razao
    print('{}'.format(pa),end=' -> ')
print('ACABOU!!!')