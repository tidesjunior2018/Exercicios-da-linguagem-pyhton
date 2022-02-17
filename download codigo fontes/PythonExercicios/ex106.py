'''
106-Faça um mini-sistema que use o Interactive Help do Python.O usuário vai digitar o comando e o manual vai
aparecer.Quando o usuário digitar "FIM",o programa se encerrará.

OBS: USE CORES
'''


def ajuda(com):
    help(com)


def titulo(msg,cor=0):
    tam=len(msg)+4
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)


#programa principal

comando=''

while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    comando=str(input('Função da Biblioteca ->'))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
titulo('FIM DO PROGRAMA')
