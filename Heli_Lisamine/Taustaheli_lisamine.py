import pygame

pygame.init()

pygame.mixer.music.load('music/Taustaheli.wav')
pygame.mixer.music.play(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()