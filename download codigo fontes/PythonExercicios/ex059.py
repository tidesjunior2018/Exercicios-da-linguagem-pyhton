from time import sleep
sair=False
num1=float(input('Valor 1: '))
num2=float(input('Valor 2: '))
print('='*30)
while not sair:
    print('[1] - Soma \n'
          '[2] - Multiplicação \n'
          '[3] - Maior \n'
          '[4] - Novos Números \n'
          '[5] - Sair')
    print('='*30)
    opcao=int(input('Escolha sua opção:'))
    if opcao == 1:
        soma=num1+num2
        print('A soma de {:.1f} + {:.1f} é {:.1f} '.format(num1,num2,soma))
    elif opcao == 2:
        multiplicacao=num1*num2
        print('A multiplicacão de {:.1f} X {:.1f} é {:.1f}'.format(num1,num2,multiplicacao))
    elif opcao == 3:
        if num1 > num2:
            print('Entre {:.1f} e {:.1f} , o {:.1f} é maior'.format(num1,num2,num1))
        elif num2 > num1:
            print('Entre {:.1f} e {:.1f} , {:.1f} é maior'.format(num1,num2,num2))
        else:
            print('Não existe número maior!!!')
    elif opcao == 4:
        num1 = float(input('Novo valor 1: '))
        num2 = float(input('Novo valor 2: '))
    elif opcao == 5:
        sair = True
        print('FINALIZANDO.....')
        sleep(3)
    else:
        print('OPÇÃO INVÁLIDA!!! TENTE NOVAMENTE 1 ATÉ O 5.')
    print('='*30)
print('FIM!!! VOLTE A QUALQUER HORA.')