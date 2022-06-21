def linha(tam = 42):
    return '-' * tam


def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    i=1
    cabecalho('MENU PRINCIPAL')
    for item in lista:
        print(f'\033[33m{i}-\033[34m{item}\033[m')
        i=i+1
    print(linha())
    opcao=leiaInt('\033[32mSua Opção:\033[m')
    return opcao
    

def leiaInt(msg):
    try:
        n=int(input(msg))
    except (TypeError,ValueError):
        print('\033[31mErro!!!Digite um número inteiro válido.\033[m')
    except (KeyboardInterrupt):
        print('\033[31mO usuário preferiu não digitar o número.\033[m')
        return 0
    else:
        return n
    
