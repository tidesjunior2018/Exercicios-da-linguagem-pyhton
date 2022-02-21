'''
106-Faça um mini-sistema que use o Interactive Help do Python.O usuário vai digitar o comando e o manual vai
aparecer.Quando o usuário digitar "FIM",o programa se encerrará.

OBS: USE CORES
'''

from time import sleep
cores=('\033[m',    #0-sem cores
       '\033[0;30;41m',#1-vermelho
       '\033[0;30;42m',#2-verde
       '\033[0;30;43m',#3-amarelo
       '\033[0;30;44m',#4-azul
       '\033[0;30;45m',#5-roxo
       '\033[7;30m'    #6-branco
       );

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(cores[6],end='')
    help(com)
    print(cores[0],end='')
    sleep(2)

def titulo(msg,cor=0):
    tam=len(msg)+4
    print(cores[cor],end='')
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)
    print(cores[0],end='')
    sleep(1)

#programa principal

comando=''

while True:
    titulo('SISTEMA DE AJUDA PYHELP',2)
    comando=str(input('Função da Biblioteca ->'))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
titulo('FIM DO PROGRAMA',1)
