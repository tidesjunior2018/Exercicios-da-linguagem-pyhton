from lib.interface import *

def arquivoExiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!!!!!!')
    else:
        print(f'O arquivo {nome} foi criado com sucesso!!!')
        
def leiaArquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('Houve um erro na hora da leitura do arquivo')
    else:
        cabecalho('Pessoas Cadastradas')
        print(a.readlines())