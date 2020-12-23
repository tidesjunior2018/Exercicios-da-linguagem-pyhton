'''
60-Faça um programa que leia um numero qualquer e mostre seu fatorial.

EX:

5!= 5 X 4 X 3 X 2 X 1 = 120
'''


'''fat=1
n=int(input('Digite um valor: '))
for c in range(n,0,-1):
    fat*=c
    print(c,'X ',end=' ')
print(fat)'''

fatorial=1
n=int(input('Digite um valor:'))
i=1
while i <= n:
    fatorial=fatorial*i
    i=i+1
print('\nO fatorial de {}! = {}'.format(n,fatorial))
