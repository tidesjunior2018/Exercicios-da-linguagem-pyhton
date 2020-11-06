soma=0
n=999
flag=False


while not flag:
    num=int(input('Digite um valor[999 para parar]: '))
    if num == n:
        break
    soma = soma + num
print('SOMA = {}'.format(soma))