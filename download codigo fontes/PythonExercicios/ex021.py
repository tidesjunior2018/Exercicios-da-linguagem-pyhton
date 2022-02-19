'''
21-Faça um programa em Pyhton que abra e reproduza um arquivo mp3.
'''
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("/home/tidesjr/Documentos/MeusProjetos/ExerciciosdePyhton/Exercicios-da-linguagem-pyhton/download codigo fontes/PythonExercicios/ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()