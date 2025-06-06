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

# aluse muutjad
palkX = screenX // 2 - 60
palkY = screenY / 1.5
palkAsukoht = (palkX, palkY)
palkVasakule = False
palkParemale = True

# palli muutujad
pallX = screenX // 2 - 10
pallY = 50
pallKiirusX = 3
pallKiirusY = 3

# punktisüsteem
skoor = 0
font = pygame.font.SysFont(None, 36)

while True:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # aluse liikumine
    if palkParemale == True:
        palkX += 3
        if palkX + 120 >= screenX:
            palkParemale = False
            palkVasakule = True
    elif palkVasakule == True:
        palkX -= 3
        if palkX <= 0:
            palkVasakule = False
            palkParemale = True

    # palli liikumine
    pallX += pallKiirusX
    pallY += pallKiirusY

    # palli põrkumine seintest
    if pallX <= 0 or pallX + 20 >= screenX:
        pallKiirusX = -pallKiirusX
    if pallY <= 0:
        pallKiirusY = -pallKiirusY

    # Rect objektide loomine kokkupõrke tuvastamiseks
    pallRect = pygame.Rect(pallX, pallY, 20, 20)
    palkRect = pygame.Rect(palkX, palkY, 120, 20)

    # kokkupõrke tuvastamine
    if pallRect.colliderect(palkRect) and pallKiirusY > 0:
        pallKiirusY = -pallKiirusY
        skoor += 1

    # pall põrkas vastu alumist serva
    if pallY + 20 >= screenY:
        pallKiirusY = -pallKiirusY
        skoor -= 1

    # joonistame objektid ekraanile
    screen.fill(taustvarv)
    screen.blit(pall, [pallX, pallY])
    screen.blit(palk, [palkX, palkY])

    # skoori kuvamine
    skoorTekst = font.render(f"Skoor: {skoor}", True, (0, 0, 0))
    screen.blit(skoorTekst, (10, 10))

    pygame.display.flip()