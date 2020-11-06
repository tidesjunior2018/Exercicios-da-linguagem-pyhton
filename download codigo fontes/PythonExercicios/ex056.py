soma=0
maioridade=0
nomemaisvelho=''
contmulher=0;
menoridademulher=0
for pessoas in range(1,5):
    print('{:=^20}'.format('{}ª Pessoa'.format(pessoas)))
    nome=str(input('Nome:'))
    idade=int(input('Idade:'))
    sexo=str(input('Sexo [M/F]:')).upper()
    if pessoas == 1 and sexo == 'M':
        maioridade=idade
        nomemaisvelho=nome
    if sexo == 'M' and idade > maioridade:
            maioridade=idade
            nomemaisvelho=nome
    if pessoas == 1 and sexo == 'F':
        menoridademulher=idade

    if sexo == 'F' and idade < menoridademulher:
        contmulher+=1

    soma+=idade
mediadogrupo=soma/pessoas
print('\nA média do grupo num total de {} pessoas é de {} anos'.format(pessoas,mediadogrupo))
print('\nO nome do homem mais velho é {}'.format(nomemaisvelho.upper()))
print('\nSão {} mulheres que tem menos de 20 anos'.format(contmulher))