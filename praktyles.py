import pygame
import sys
import random

pygame.init()

screen=pygame.display.set_mode([1080,720])
pygame.display.set_caption("Praktiline ülesanne")
screen.fill([123,123,123])
clock = pygame.time.Clock()

posX = 1080/2
posY = 720/2
kiirusX = 0
kiirusY = 0
suundX = 0
suundY = 0

rstX = 0
rstY = 0

ristkylikud = []
for i in range(15):
    rstX = random.randint(1, 1080)
    rstY = random.randint(1, 720)
    ristkylikud.append([rstX, rstY])

    for i in range(len(ristkylikud)):
        pygame.draw.rect(screen, [255, 0, 0], [ristkylikud[i][0], ristkylikud[i][1], 20, 20])

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                kiirusX = 4
            elif event.key == pygame.K_LEFT:
                kiirusX = -4
            elif event.key == pygame.K_UP:
                kiirusY = -4
            elif event.key == pygame.K_DOWN:
                kiirusY = 4

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                kiirusX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                kiirusY = 0

    for i in range(len(ristkylikud)):
        pygame.draw.rect(screen, [0, 0, 0], [ristkylikud[i][0], ristkylikud[i][1], 40, 50])


    posX += kiirusX
    posY += kiirusY


    ruut = pygame.draw.rect(screen,[0, 0, 255],[posX, posY, 30, 30])

     if ruut.colliderect(ristkylikud):
        print("Töötab")

    pygame.display.flip()
    screen.fill([123,123,123])