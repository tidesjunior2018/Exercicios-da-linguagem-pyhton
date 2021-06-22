'''
94-Crie um programa que leia o nome,sexo e idade de várias pessoas,guardando os dados da pessoa em um dicionário e todos os dicionários em uma lista.No final mostre:

A)Quantas pessoas cadastradas.
B)A média de idade
C)Uma lista com mulheres
D)Uma lista com idade acima da média
'''

galera=[]
pessoas={}
somaidade=0
mediaidade=0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome:')).upper()
    pessoas['idade'] = int(input('Idade:'))
    somaidade=somaidade+pessoas['idade']

    while True:
        pessoas['sexo'] = str(input('Sexo:')).upper()[0]

        if pessoas['sexo'] in 'MF':
            break

        print('ERRO!!!Digite apenas a letra M ou F.')
    
    galera.append(pessoas.copy())
    
    resp=str(input('Quer Continuar [S/N]')).upper()[0]

    while True:
        if resp in 'SN':
            break

        print('ERRO!!!Digite apenas a letra S ou N.')

    if resp == 'N':
        break
print('=-='*30)
#a)
print(f'Ao todo foram {len(galera)} pessoas cadastradas')
#b)
print(f'A média de idade foi de {somaidade/len(galera)} anos')
#c)
print('As mulheres cadastradas foram ',end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'],end=' ')
print()
#d)
mediaidade=somaidade/len(galera)
print('Lista das pessoas com idade acima da média:')
for p in galera:
    if p['idade'] > mediaidade:
        print('     ')
        for k,v in p.items():
            print(f'{k}={v}',end=' ')
        print()
print()
print('<<<Fim do Programa>>>')