primeirotermo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razao: '))
i=1
while i <= 10:
    pa=primeirotermo+(i-1)*razao
    print('{} ->'.format(pa),end=' ')
    i=i+1
print('Acabou!!!')
