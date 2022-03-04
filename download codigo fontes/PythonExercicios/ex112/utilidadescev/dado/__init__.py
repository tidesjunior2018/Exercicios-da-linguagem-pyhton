def leiaDinheiro(msg):
    flag=False
    while not flag:
        entrada=str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip()=='':
            print(f'\033[0;31mErro: \"{entrada}\" é um preço inválido\033[m')
        else:
            flag=True
            return float(entrada)