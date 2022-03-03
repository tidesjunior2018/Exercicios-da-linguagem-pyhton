'''
111-Crie um pacote chamado UtilidadesCeV que tenha dois módulos internos chamado moeda e dado.
Transfira todas as funções utilizadas nos desafios 107,108 e 109 para o primeiro pacote e mantenha tudo funcionando.
'''

import utilidadescev.moeda

preco=float(input('Digite o preço: '))
taxa=int(input('Digite a taxa:[0-para indicar nenhuma taxa] '))

if taxa == 0:
    utilidadescev.moeda.resumo(preco)
elif taxa > 0 :
    utilidadescev.resumo(preco,taxa)
