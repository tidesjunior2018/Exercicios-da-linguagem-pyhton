'''
115-Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

O sistema vai ter 2 opções:cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
''' 

from lib.interface import *
from lib.arquivo import *
from time import sleep

arq='cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!!!')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)

    
while True:
    resposta=menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Listar Pessoas','Sair do Sistema'])
    if resposta == 1:
        #listar pessoas cadastradas
        leiaArquivo(arq)
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Opção 3')
    elif resposta == 4:
        cabecalho('\033[36mSaindo do sistema...Até Breve!!!\033[m')
        break
    else:
        print('\033[31mERRO!!!Escolha uma opção válida.\033[m')
    sleep(1)