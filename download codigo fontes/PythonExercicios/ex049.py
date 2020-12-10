'''
49-Refaça o desafio 009, mostrando a tabuada de um número que o usúario
escolher, só que agora utilizando o laço FOR.
'''

n=int(input('Qual o número que você quer a tabuada: '))
print('='*20)
print('TABUADA DO N° {}'.format(n))
print('='*20)
for c in range(0,11):
    print('|{} X {} = {}|'.format(n,c,n*c))
print('='*20)
