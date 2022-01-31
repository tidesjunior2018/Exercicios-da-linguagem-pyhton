'''
101-Crie um programa que tenha uma função chamada voto() que vai receber o ano de nascimento de uma pessoa,retornando um valor literal indicando se uma pessoa tem o voto NÃO VOTA,OPCIONAL,OBRIGATÓRIO nas eleições.
'''

def voto(ano):
    from datetime import date
    anoatual=date.today().year
    idade=anoatual-ano
    if idade<16:
        return f'Com {idade} anos:NÃO VOTA'
    elif idade>=16 and idade<18 or idade>65:
        return f'Com {idade} anos:VOTO OPCIONAL'
    elif idade>=18:
        return f'Com {idade} anos:VOTO OBRIGATÓRIO'

#programa principal
nasc=int(input('Em ano ano você nasceu:'))
respostaidade=voto(nasc)
print(respostaidade)