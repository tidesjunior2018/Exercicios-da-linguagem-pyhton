'''
102-Crie um programa que tenha uma função fatorial() que receba dois parâmetros:o primeiro indique o número a calcular e o outro chamado show que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo do fatorial
'''

def fatorial(n,show=False):
    global fat,numero
    fat=1
    
    if show==True:
        print(f'O processo do fatorial do {numero} é:')
        print()
        for cont in range(n,0,-1):
            fat=fat*cont
            if cont>1:
                print(f'{cont}',end=' X ')
            else:
                print(f'{cont}',end='  ')
        print(f'= {fat}')
    else:
        for c in range(n,0,-1):
            fat=fat*c
        print(f'O fatorial de {numero}! = {fat}')
        

#Programa Principal
numero=int(input('Qual o número que você quer saber o fatorial:'))
fatorial(numero)
