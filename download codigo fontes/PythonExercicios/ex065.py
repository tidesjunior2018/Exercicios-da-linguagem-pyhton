total=0
soma=0
maior=0
menor=0
resp=False
while not resp:
    num=int(input('Digite um valor: '))
    soma += num
    total += 1

    if total == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    continuar=str(input('Quer continuar[S/N]: ')).upper()
    if continuar == 'N':
        resp=True

media=soma/total

print('Você digitou {} números\n'
      'Media = {}\n'
      'Maior = {}\n'
      'Menor = {}\n'
      .format(total,media,maior,menor))
