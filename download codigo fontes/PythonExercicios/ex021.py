'''
21-Faça um programa em Pyhton que abra e reproduza um arquivo mp3.
'''
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()