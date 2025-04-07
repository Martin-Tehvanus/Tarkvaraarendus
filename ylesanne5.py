# impordid
import pygame
import sys

# ekraani suurus
screenX = 640
screenY = 480

# ekraani asjad
pygame.init()
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("PingPong")
taustvarv = (149, 203, 255)
screen.fill(taustvarv)
clock = pygame.time.Clock()

# palli ja aluse kuvamine
pall = pygame.image.load("yl5/pall.png")
palk = pygame.image.load("yl5/alus.png")

# palli ja aluse suuruse määramine
pall = pygame.transform.scale(pall, [20, 20])
palk = pygame.transform.scale(palk, [120, 20])

#aluse muutjad
palkX = 0
palkY = 0
palkAsukoht = (palkX, palkY)

# palli muutujad
pallX = 0
pallY = 0


#palli ja aluse ekraanile panemine
screen.blit(pall, [pallX, pallY])
screen.blit(palk, [palkX, screenY/1.5])

while True:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()


 #   palkX += 1
    print(palkX) # 522
    pallX += 1
    pallY += 1

    if palkX == 0 or palkX < 0:
        palkX += 1
    elif palkX > 522:
        palkX -= 1

    screen.blit(pall, [pallX, pallY])
    screen.blit(palk, [palkX, screenY/1.5])

    pygame.display.flip()
    screen.fill(taustvarv)