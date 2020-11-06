nome = str(input('Digite seu nome completo: ')).strip()
nomedividido = nome.split()
print('\nPrazer em te conhecer !!! \n')
print('Seu primeiro nome é {}'.format(nomedividido[0]))
ultimonome = nomedividido[len(nomedividido) - 1]
print('Seu último nome é {}'.format(ultimonome))
