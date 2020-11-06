from datetime import date
anonascimento=int(input('Ano de nascimento: '))
anoatual=date.today().year
idade=anoatual - anonascimento

if idade<18:
    quantanosfalta=18-idade
    print('você tem {} anos e ainda falta {} anos para se alistar.'.format(idade, quantanosfalta))
    anoalistamento=anoatual+quantanosfalta
    print('Seu alistamento será em {}.'.format(anoalistamento))
elif idade==18:
    print('Você tem {} anos e é hora de se alistar.'.format(idade))
elif idade>18:
    quantanosfoi=idade-18
    print('Você tem {} anos e já passou do tempo de se alistar.Tem {} anos do ano do alistamento'.format(idade, quantanosfoi))
    anoalistamento=anoatual-quantanosfoi
    print('Seu alistamento foi em {}.'.format(anoalistamento))
