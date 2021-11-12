'''
100-Faça um programa que tenha lista uma chamada números e tenha duas funções sorteia() e somaPar().A primeira função vai sortear 5 numeros e colocá-los dentro de uma lista e a segunda função vai mostrar a soma de todos os valores pares sorteados pela função anterior.
'''
from random import randint

num=list()

def sorteia(num):
    cont=0
    while cont<5:
        valor=randint(1,10)
        num.append(valor)
        cont+=1
    print(f"Mostrando a lista sorteada = {num}")


def somaPar(num):
    soma=0
    for num2 in num:
        if num2%2==0:
            soma+=num2
    print(f"Analisando a lista sorteada a soma dos números pares é:{soma}")

    
sorteia(num)
somaPar(num)
