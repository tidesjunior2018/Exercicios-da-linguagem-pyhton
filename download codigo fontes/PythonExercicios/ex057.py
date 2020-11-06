sexo=str(input('Digite o seu sexo:[M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo=str(input('\033[31m DADOS INVÁLIDOS!!!\n\033[mDigite novamente o seu sexo:[M/F] ')).strip().upper()[0]
if sexo == 'M':
    print('\nSexo \033[34mMASCULINO \033[m incluido com sucesso!!!')
if sexo == 'F':
    print('\nSexo \033[31mFEMININO \033[m incluido com sucesso!!!')
