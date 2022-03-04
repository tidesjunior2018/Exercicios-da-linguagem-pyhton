'''
112-Dentro do pacote utilidadescev que criamos no desafio 111,temos um módulo chamado dado.Crie uma função leiaDinheiro() que seja capaz de funcionar como a função input() mais como uma validação de dados para aceitar apenas valores monetários.
'''

import utilidadescev.moeda
import utilidadescev.dado

preco=utilidadescev.dado.leiaDinheiro('Digite o preço:')
taxa=utilidadescev.dado.leiaDinheiro('Digite a taxa:[0-para indicar nenhuma taxa] ')

if taxa == 0:
    utilidadescev.moeda.resumo(preco)
elif taxa > 0 :
    utilidadescev.moeda.resumo(preco,taxa)
