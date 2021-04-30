'''
90-Faça um programa que leia nome e a media de aluno,guardando também a situação em um dicionário.No final mostre a estrutura na tela.
'''
pessoa = {}

pessoa['nome'] = str(input('Nome : ')).upper()
pessoa['media'] = float(input(f"Média do aluno {pessoa['nome']}: "))

if pessoa['media'] >= 7:
    pessoa['situacao'] = 'Aprovado'
else:
     if pessoa['media'] >= 5 and pessoa['media'] <= 6.9:
         pessoa['situacao'] = 'Prova final'
     else :
         if pessoa['media'] < 5:
             pessoa['situaçao'] = 'Reprovado'

print('-=-'*20)
for p,v in pessoa.items():
    print(f'-{p} = {v}')
    print()
print('-=-'*20)

print()
