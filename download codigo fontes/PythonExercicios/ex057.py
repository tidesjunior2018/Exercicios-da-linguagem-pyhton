'''
57-Faça um programa que leia o sexo de uma pessoa,mas só aceite os valores M
ou F .Caso esteja errado peça a digitação novamente até ter o valor correto.
'''
sexo=str(input('Digite o seu sexo:[M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo=str(input('\033[31m DADOS INVÁLIDOS!!!\n\033[mDigite novamente o seu sexo:[M/F] ')).strip().upper()[0]
if sexo == 'M':
    print('\nSexo \033[34mMASCULINO \033[m incluido com sucesso!!!')
if sexo == 'F':
    print('\nSexo \033[31mFEMININO \033[m incluido com sucesso!!!')
