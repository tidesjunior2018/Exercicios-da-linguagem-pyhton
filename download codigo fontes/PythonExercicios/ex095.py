'''
95-Aprimore o desafio 093 para que ele funcione para vários jogadores,incluindo um sistema de verificação de detalhamento de aproveitamento de cada jogador.
'''
time=[]
jogador={}
gols=[]
i=0

while True:
    jogador.clear()

    jogador['jogador']=str(input('Nome do jogador:')).upper()
    partidas=int(input(f'Quantas partidas o {jogador["jogador"]} jogou:'))
    
    gols.clear()

    for i in range(0,partidas):
        gols.append(int(input(f'Quantos gols fez no {i+1}° jogo:')))

    jogador['gols']=gols[:]
    jogador['total']=sum(gols)

    time.append(jogador.copy())

    while True:
        resp = str(input('Você quer continuar[S/N]: ')).upper()[0]

        if resp in 'SN':
            break

        print('ERRO!!!Digite apenas a letra S ou N.')

    if resp == 'N':
        break

print('-=-'*40)

print('Cod ',end='')

for i in jogador.keys():
    print(f'{i:<15}',end='')

print()

print('-'*40)

for k,v in enumerate(time):

    print(f'{k:>2}', end=' ')
    for dados in v.values():
        print(f'{str(dados):<14}',end=' ')
    print()

print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para encerrar]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro!!! Não existe jogador com esse com código {busca}.Tente '
              'novamente!')
    else:
        print(f'Levantamento do jogador {time[busca]["jogador"]}')
        for i,g in enumerate(time[busca]['gols']):
            print(f'    No {i+1}° jogo fez {g} gols')
    print('-'*40)
print()
print('<< VOLTE SEMPRE >>')



