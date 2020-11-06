frase=str(input('Digite uma frase: ')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=''
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
print('\nVocê digitou a seguinte frase {} e o inverso é {}'.format(junto,inverso))
if inverso == junto:
    print('\033[34m')
    print('Temos um palíndromo!!!')
else:
    print('\033[31m')
    print('Não é palíndromo!!!')
