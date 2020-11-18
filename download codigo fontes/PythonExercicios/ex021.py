'''
21-Faça um programa em Pyhton que abra e reproduza um arquivo mp3.
'''
import pygame.examples.aliens.main()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()