num=(int(input('Digite um número:')),int(input('Digite um número:')),int(input('Digite um número:')),
     int(input('Digite um número:')))
print('\n')
print('-'*34)
print(f'Os valores da tupla são: {num}')
#a)
if 9 in num:
     print(f'O valor 9 apareceu {num.count(9)} vezes')
else:
     print('O valor 9 não apareceu nenhuma vez!!!')
#b)
if 3 in num:
     print(f'O valor 3 está na {num.index(3)+1}ª posição.')
else:
     print('O valor 3 não está em nenhuma posição!!!')
#c)
print('Os valores pares dentro da tupla são: ',end=' ')
for i in num:
     if i%2 == 0:
          print(i,end=' ')
print('\n')
print('-'*34)