'''
104-Crie um programa que tenha a função leiaint() que vai funcionar de forma semelhante a função input() do python,
só que a validação para aceitar apenas o valor númerico.
'''
def leiaInt(msg):
    flag =False
    while True:
        num = str(input(msg))
        if num.isnumeric():
            num=int(num)
            flag=True
        else:
            print('\033[0;31mERRO!!!Digite um número válido\033[m')
        if flag:
            break
    return num

#programa principal
n=leiaInt("Digite um numero:")
print(f"O número digitado foi:{n}")