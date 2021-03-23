'''
21-Faça um programa em Pyhton que abra e reproduza um arquivo mp3.
'''
import pygame
pygame.mixer.init()
musica=pygame.mixer.Sound('ex021.mp3')
musica.play()
pygame.event.wait()