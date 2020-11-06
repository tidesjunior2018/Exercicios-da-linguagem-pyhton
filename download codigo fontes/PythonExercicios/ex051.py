print('{:=^40}'.format('10 termos de uma P.A'))# centralizar
primeirotermo=int(input('Digite o primeiro termo: '))
print('\n')
razao=int(input('Digite a razão:'))
for n in range(1,11):
    pa=primeirotermo+(n-1)*razao
    print('{}'.format(pa),end=' -> ')
print('ACABOU!!!')