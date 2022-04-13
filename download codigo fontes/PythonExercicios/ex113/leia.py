def leiaInt(msg):
    flag=False
    while not flag:
        try:
            num=str(input(msg)).replace(',','.')
            num2=int(num)
            flag=True
        except KeyboardInterrupt:
            print()
            print('\033[1;41m O usuário quis parar o progama.O valor padrão é 0\033[m')
            print()
            return 0
        except:
            print('\033[1;41m Erro!!!Digite um número inteiro sem ser por extenso\033[m')
        else:
            return num2

def leiaFloat(msg):
    flag=False
    while not flag:
        try:
            num=str(input(msg)).replace(',','.')
            num2=float(num)
            flag=True
        except KeyboardInterrupt:
            print()
            print('\033[1;41m O usuário quis parar o progama.O valor padrão é 0\033[m')
            print()
            return 0
        except:
            print('\033[1;41mErro!!!Digite um número real sem ser por extenso.\033[m')
    return num2