'''
73-Crie uma tupla com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,na ordem da colocação.Depois mostre:

A)Os 5 primeiros.
B)Os últimos 4 colocados.
C)Times em ordem alfabética.
D)Em que posição está a chapecoense.  
'''
times=('Flamengo','Palmeiras','Santos','São Paulo','Corinthians','Internacional','Gremio','Bahia',
       'Atlético-PR','Goiás','Vasco da Gama','Atlético','Fortaleza','Botafogo','Cruzeiro','Ceará SC',
       'CSA','Chapecoense','Avaí')

print(f'Lista de Times: {times}')
print('=-='*50)
print(f'Os cinco primeiros colocados são:{times[0:5]}')
print('=-='*50)
print(f'Os quatro últimos colocados são:{times[-4:]}')
print('=-='*50)
print(f'Os times em ordem alfabética:{sorted(times)}')
print('=-='*50)
print(f'O time chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('=-='*50)