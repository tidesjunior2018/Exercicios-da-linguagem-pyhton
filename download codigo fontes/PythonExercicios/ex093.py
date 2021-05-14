'''
93-Crie um programa que gerencie o aproveitamento de um jogador de futebol.O programa vai ler o nome do jogador e quantas ele jogou.Depois vai ler a quantidade de gols feitos em cada partida.No final será guardado no dicionário incluindo o total de gols feitos durante o campeonato.
'''

jogador={}
gols=[]
i=0

jogador['nome']=str(input('Nome do jogador: ')).upper()

partidas=int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))

for i in range(0,partidas):
    gols.append(int(input(f'Quantos gols fez na {i+1}º partida: ')))

jogador['gols'] = gols[:] # [:] significa cóṕia

jogador['total'] = sum(gols)

print('-=-'*30)

print(jogador)

print('-=-'*30)

for k,v in jogador.items():
    print(f'O {k} tem valor {v}')

print('-=-'*30)

print(f'O jogador {jogador["nome"]} fez {partidas} partidas')

for c, gol in enumerate(gols):
    print(f'    => No {c+1}° jogo fez {gol} gols')

print(f'Foi um total de {jogador["total"]} gols')

print('-=-'*30)

print()