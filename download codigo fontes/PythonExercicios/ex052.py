'''
52-Faça um programa que leia um número inteiro e diga se ele ou não número
primo.
'''
num=int(input('Digite o numero: '))
cont=0
for c in range(1,num+1):
    if num%c == 0:
        print('\033[34m',end=' ')
        cont+=1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[mO número {} foi dividido {} vezes'.format(num,cont))
if cont == 2:
    print('\033[34m')
    print('Esse número é primo!!!')
else:
    print('\033[31m')
    print('Esse numero não é primo!!!')