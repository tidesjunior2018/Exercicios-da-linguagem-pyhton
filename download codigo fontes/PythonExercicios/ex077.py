palavras=('AMIGO','BOLA','ESCOLA','FACULDADE','RELOGIO')
for p in palavras:
    print(f'\n\033[37m Na palavra {p} temos :',end=' ')
    for letra in p:
        if letra in 'AEIOU':
            print(f'\033[34m{letra}',end=' ')
print('\n\033[37m')
