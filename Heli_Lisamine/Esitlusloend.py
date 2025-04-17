import pygame
import random

pygame.init()

sounds = ['snd1.wav', 'snd2.wav', 'snd3.wav', 'snd4.wav', 'snd5.wav']
pygame.mixer.music.load('music/'+random.choice(sounds))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()