'''
46-Faça um programa que mostre na tela uma contagem regressiva para estouro
dos fogos de artificios ,indo de 10 a 0 , com uma pausa de 1 segundo entre eles.
'''
import emoji
from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print(emoji.emojize('FELIZ ANO NOVO !!!:fireworks:',use_aliases=True))

