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
        for linha in a:
            dados=linha.split(';')
            dados[1]=dados[1].replace('\n','')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
    finally:
        a.close()
        
def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a=open(arq,'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso.')
            a.close()