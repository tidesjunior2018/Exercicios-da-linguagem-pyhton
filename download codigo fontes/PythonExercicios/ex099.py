'''
99 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.Seu programa tem analisar todos eles e dizer qual é o maior.
'''

from time import sleep
def maior(* num):
    maior=0
    cont=0
    print("Analisando os valores passados...")    
    for valor in num:
        print(f"{valor}",end=" ",flush=True)
        sleep(0.3)
        if cont==0:
            maior=valor
        else:
            if valor>maior:
                maior=valor
        cont+=1
    print(f"Foram informados {cont} valores")
    print(f"O maior valor informado foi:{maior}")
    
    
def mostrarlinha():
    print("-=-"*30)

mostrarlinha()
maior(2,9,4,5,7,1)
mostrarlinha()
maior(4,7,0)
mostrarlinha()
maior(1,2)
mostrarlinha()
maior(6)
mostrarlinha()
maior()
mostrarlinha()
