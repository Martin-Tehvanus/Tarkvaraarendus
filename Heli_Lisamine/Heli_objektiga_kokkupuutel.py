import time
import pygame

pygame.init()

hit_sound = pygame.mixer.Sound('music/Hit.wav')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    time.sleep(1)
    pygame.mixer.Sound.play(hit_sound)