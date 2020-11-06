maior=0
menor=0
for pessoas in range(1,6):
    peso=float(input('Qual o peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso

print('\nO maior peso lido foi {:.1f}Kg'.format(maior))
print('\nO menor peso lido foi {:.1f}Kg'.format(menor))