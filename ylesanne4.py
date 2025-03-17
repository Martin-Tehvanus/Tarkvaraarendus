# impordid
import pygame
import sys
import random
pygame.init()

# muutujad
clock = pygame.time.Clock()
skoor = 0
kiirus = 3 # auto liikumise kiirus

# auto alustuse kõrgused (suvaliselt valitud 1 ja 479 vahel)
korgus1 = random.randrange(1, 479)
korgus2 = random.randrange(1, 479)
korgus3 = random.randrange(1, 479)



# auto tee vahemikud (paneb iga auto teatud tee rea peale)
alg1 = 180, korgus1 # esimene tee rida, esimene arv paneb auto tee keskele (joonte vahele), teiseks on kõrgus
alg2 = 300, korgus2
alg3 = 420, korgus3

# aken
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne 4")


# autod ja taust
punane_auto = pygame.image.load("yl4/f1_red.png")
sinine_auto1 = pygame.image.load("yl4/f1_blue.png") # vasak
sinine_auto2 = pygame.image.load("yl4/f1_blue.png") # keskmine
sinine_auto3 = pygame.image.load("yl4/f1_blue.png") # parem
taust = pygame.image.load("yl4/bg_rally.jpg")

# põhikood
while True:
    clock.tick(60) # fps (60+ sobilik)

    # autode liikumine
    korgus1 += kiirus
    korgus2 += kiirus
    korgus3 += kiirus

    # alla sõit + skoori lisamine
    if korgus1 > 480:
        korgus1 = 0
        skoor +=1
    if korgus2 > 480:
        korgus2 = 0
        skoor +=1
    if korgus3 > 480:
        korgus3 = 0
        skoor +=1

    # autode positiooni uuendamine (pärast alla jõudmist ja skoori saamist)
    alg1 = (180, korgus1)
    alg2 = (300, korgus2)
    alg3 = (420, korgus3)

    # asjade kuvamine pygame aknasse
    screen.blit(taust, (0,0))
    screen.blit(punane_auto, (300,390))
    screen.blit(sinine_auto1, alg1)
    screen.blit(sinine_auto2, alg2)
    screen.blit(sinine_auto3, alg3)

    #skoori kuvmine pygame aknasse
    font = pygame.font.Font(None, 35)
    text = font.render("Skoor: " + str(skoor), True, [255, 255, 255])
    screen.blit(text, (270, 0))

# ristist kinni panemine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()