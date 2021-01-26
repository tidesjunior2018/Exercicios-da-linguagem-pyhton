'''
83-Crie um programa onde o usuário digite uma expressão qualquer entre parênteses.Seu aplicativo deverá analisar se a expressão passada está com parênteses fechados na ordem correta.
'''
soma=soma2=0
expressao=str(input('Digite a expressão:'))
for simb in expressao:
    if simb == '(':
        soma+=1
    else:
        if simb == ')':
            soma2+=1

if soma == soma2:
    print('Os parênteses estão fechado de forma correta')
else:
    print('Os parênteses estão fechado de forma incorreta')
print('\n')