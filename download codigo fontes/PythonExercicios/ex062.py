primeirotermo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razao: '))
i=1
termo=10
total=0
while termo != 0:
    total=total+termo
    while i <= total:
        pa=primeirotermo+(i-1)*razao
        print('{} ->'.format(pa),end=' ')
        ultimotermo = pa
        i=i+1
    print('PAUSA!!!')
    termo=int(input('Quantos termos você quer?'))
print('P.A com {} números mostrados'.format(total))