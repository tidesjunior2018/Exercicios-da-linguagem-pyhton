'''
67-Faça um programa que mostre a tabuada de vários números,um de cada vez para cada valor digitado pelo usuário.O programa deve ser interrompido quando o número solicitado for negativo.
'''
while True:
    n=int(input('Você que ver a tabuada de qual valor: '))
    if n < 0:
        break
    print('-=-'*30)
    for i in range(1,11):
        print(f'{n} X {i} = {n*i}')
    print('-=-'*30)
print('\n\033[31mPROGRAMA TERMINADO !!! \033[mVOLTE SEMPRE...')
