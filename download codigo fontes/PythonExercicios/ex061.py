'''
61-Refaça o desafio 051,lendo o primeiro termo e a razão de uma P.A, mostrando os 10 primeiros termos usando a estrutura while. 
'''
primeirotermo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razao: '))
i=1
while i <= 10:
    pa=primeirotermo+(i-1)*razao
    print('{} ->'.format(pa),end=' ')
    i=i+1
print('Acabou!!!')
