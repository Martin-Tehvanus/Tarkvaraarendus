# impordid
import pygame
import sys
import random
pygame.init()

# muutujad
clock = pygame.time.Clock()
skoor = 0
korgus1 = random.randrange(0, 479)
korgus2 = random.randrange(0, 479)
kiirus = 5


# auto lubatud asukohad
alg1 = 180, korgus1 # esimene tee vahemik, esimene arv paneb auto tee keskele, teiseks on kõrgus
alg2 = 420, korgus2 # teine tee vahemik, esimene arv paneb auto tee keskele, teiseks on kõrgus

# aken
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne 4")


# autod ja taust
punane_auto = pygame.image.load("yl4/f1_red.png")
sinine_auto1 = pygame.image.load("yl4/f1_blue.png")
sinine_auto2 = pygame.image.load("yl4/f1_blue.png")
taust = pygame.image.load("yl4/bg_rally.jpg")

# põhikood





while True:
    clock.tick(60)
# asjade kuvamine
    screen.blit(taust, (0,0))
    screen.blit(punane_auto, (300,390))
    screen.blit(sinine_auto1, alg1)
    screen.blit(sinine_auto2, alg2)


#skoor
    font = pygame.font.Font(None, 35)
    text = font.render(str(skoor), True, [255, 255, 255])
    screen.blit(text, (310, 0))

# ristist kinni
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.display.flip()
pygame.quit()




# Puudu

#Lisa siniste autode animatsioon ülevalt alla
#   autod jäävad tee vahemikku - tehtud
#   alustavad erinevatelt kõrgustelt - tehtud
#   kui auto alla jõuab, hakkab ta uuesti ülevalt alla liikuma

#Kuva skoor - tehtud
#   kui sinine auto jõuab alla, lisatakse skoorile punkte juurde
#   arv, mida soovid lisada tekstikasti, tuleb teisendada tekstiks str(number) - tehtud