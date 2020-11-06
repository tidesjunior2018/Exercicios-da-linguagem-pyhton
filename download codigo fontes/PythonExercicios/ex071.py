print('{:=^40}'.format('BANCO MARQUES JUNIOR '))
valor=int(input('Qual o valor a ser sacado:R$ '))
total=valor
ced=100
totalced=0
while True:
    if total >= ced:
        total-=ced
        totalced+=1
    else:
        if totalced > 0:
            print(f'Você receberá {totalced} notas de R$ {ced}')
        if ced == 100:
            ced=50
        elif ced == 50:
            ced=20
        elif ced == 20:
            ced=10
        elif ced == 10:
            ced=1

        totalced=0
        if total == 0:
            break
print('\nVolte sempre !!!')
