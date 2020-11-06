contidade = 0
conthomens = 0
contmulher = 0
while True:
    print('{:=^30}'.format('CADASTRAR PESSOA'))
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo=str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if idade >= 18:
            contidade+=1
        if sexo == 'M':
            conthomens+=1
        if sexo == 'F' and idade < 20:
            contmulher+=1
    print('PESSOA INCLUÍDA COM SUCESSO!!!')
    print('='*30)
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Quer Continuar [S/N]:')).strip().upper()[0]
    if resposta == 'N':
        break
print('*'*30)
print(f'Total de pessoas com mais de 18 anos:{contidade}')
print(f'temos {conthomens} homens cadastrados.')
print(f'Temos {contmulher} mulheres cadastradas com menos de 20 anos.')