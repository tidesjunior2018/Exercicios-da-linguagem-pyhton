n=int(input('Qual o número que você quer a tabuada: '))
print('='*20)
print('TABUADA DO N° {}'.format(n))
print('='*20)
for c in range(0,11):
    print('|{} X {} = {}|'.format(n,c,n*c))
print('='*20)
