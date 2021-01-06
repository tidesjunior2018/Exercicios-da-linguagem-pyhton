'''
63-Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci. 

Ex:
0->1->1->2->3->5->8
'''
print('='*30)
print('Sequencia de fibonnaci')
print('='*30)
n=int(input('Quantos termos você quer: '))
t1=0
t2=1
i=3
print('~'*40)
print('{} -> {}'.format(t1,t2),end=' -> ')
while i <= n:
    t3=t1+t2
    print('{}'.format(t3),end=' -> ')
    t1=t2
    t2=t3
    i+=1
print('Fim!!!')
print('~'*40)
