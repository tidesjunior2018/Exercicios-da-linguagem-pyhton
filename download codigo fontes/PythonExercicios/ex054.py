import datetime
anoatual=datetime.date.today().year
cont=0#contador de menores
cont2=0#contador de maiores
for pessoas in range(1,8):
    anodenascimento=int(input('Em que ano a {}ª pessoa nasceu: '.format(pessoas)))
    idade=anoatual-anodenascimento
    if idade >= 18:
        cont+=1
    else:
        cont2+=1
print('\nSão {} pessoas de maiores e {} pessoas de menores num total de {} pessoas'.format(cont,cont2,pessoas))