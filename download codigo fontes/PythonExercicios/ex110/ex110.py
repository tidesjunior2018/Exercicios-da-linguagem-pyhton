'''
110-Adicione ao moeda.py criado nos desafios anteriores uma função chamada resumo(),que mostra na tela algumas funções que já temos no modulo criado até aqui.
'''
import moeda
preco=float(input('Digite o preço: '))
taxa=int(input('Digite a taxa:[0-para indicar nenhuma taxa] '))

if taxa == 0:
    moeda.resumo(preco)
elif taxa > 0 :
    moeda.resumo(preco,taxa)
