import pygame
import random
import sys

pygame.init()

# muutujad
clock = pygame.time.Clock()
skoor = 0
kiirus = 3  # auto liikumise kiirus
labi = 0  # mängu lõpp ehk menüü kuvamine
highscore = 0  # Kõrgeim skoor, mis salvestatakse

# punase auto muutujad
pAsukoht = 300
pKiirus = 9


# algse kõrgused (need määratakse iga mängu alguses suvaliselt)
def määrake_korgused():
    return random.randrange(1, 479), random.randrange(1, 479), random.randrange(1, 479)


korgus1, korgus2, korgus3 = määrake_korgused()

# auto tee vahemikud (paneb iga auto teatud tee rea peale)
alg1 = 180, korgus1  # esimene tee rida
alg2 = 300, korgus2
alg3 = 420, korgus3

# aken
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Ülesanne 4")

# autod ja taust
punane_auto = pygame.image.load("yl4/f1_red.png")
sinine_auto1 = pygame.image.load("yl4/f1_blue.png")  # vasak
sinine_auto2 = pygame.image.load("yl4/f1_blue.png")  # keskmine
sinine_auto3 = pygame.image.load("yl4/f1_blue.png")  # parem
taust = pygame.image.load("yl4/bg_rally.jpg")

# siniste autode pööramine õigele poolde
sinine_auto1 = pygame.transform.rotate(sinine_auto1, 180)
sinine_auto2 = pygame.transform.rotate(sinine_auto2, 180)
sinine_auto3 = pygame.transform.rotate(sinine_auto3, 180)


# kokkupõrke tuvastamise funktsioon
def kokkuporke_tuvastus():
    # punase auto mõõdud
    p_auto_rect = pygame.Rect(pAsukoht, 390, punane_auto.get_width(), punane_auto.get_height())

    # siniste autode mõõdud
    sinine1_rect = pygame.Rect(180, korgus1, sinine_auto1.get_width(), sinine_auto1.get_height())
    sinine2_rect = pygame.Rect(300, korgus2, sinine_auto2.get_width(), sinine_auto2.get_height())
    sinine3_rect = pygame.Rect(420, korgus3, sinine_auto3.get_width(), sinine_auto3.get_height())

    # kontrollime, kas punase auto ristub mõne sinise autoga
    if p_auto_rect.colliderect(sinine1_rect) or p_auto_rect.colliderect(sinine2_rect) or p_auto_rect.colliderect(
            sinine3_rect):
        return True
    return False


# põhikood
while True:
    clock.tick(60)  # fps (60+ sobilik)

    # autode liikumine
    if labi == 0:  # Kui mäng on käimas
        korgus1 += kiirus
        korgus2 += kiirus
        korgus3 += kiirus

        # alla sõit + skoori lisamine
        if korgus1 > 480:
            korgus1 = 0
            skoor += 1
        if korgus2 > 480:
            korgus2 = 0
            skoor += 1
        if korgus3 > 480:
            korgus3 = 0
            skoor += 1

        # autode positiooni uuendamine (pärast alla jõudmist ja skoori saamist)
        alg1 = (180, korgus1)
        alg2 = (300, korgus2)
        alg3 = (420, korgus3)

        # Kui mäng on lõppenud, ekraan mustaks
        if kokkuporke_tuvastus():
            labi = 1
            if skoor > highscore:  # Salvestame kõrgeima skoori
                highscore = skoor
    else:  # Kui mäng on läbi, siis must ekraan ja menüü
        screen.fill((0, 0, 0))  # Täidetakse ekraan mustaga
        font = pygame.font.Font(None, 25)  # Tekst väiksemaks
        text = font.render(f"Skoor: {skoor}  Uuesti alustamiseks vajuta Enter, väljumiseks Escape", True,
                           [255, 255, 255])
        screen.blit(text, (50, 200))  # Paigutame teksti vasakule

    # Kui mäng on aktiivne, siis kuvatakse autode liikumist
    if labi == 0:
        screen.blit(taust, (0, 0))
        screen.blit(punane_auto, (pAsukoht, 390))
        screen.blit(sinine_auto1, alg1)
        screen.blit(sinine_auto2, alg2)
        screen.blit(sinine_auto3, alg3)

        # skoori kuvamine pygame aknasse
        font = pygame.font.Font(None, 30)  # Tekst väiksemaks
        text = font.render("Skoor: " + str(skoor), True, [255, 255, 255])
        screen.blit(text, (270, 0))

    # sündmuste töötlemine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # kontrollime, kas mäng on lõppenud või käib
        if labi == 0:  # Kui mäng käib
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pAsukoht += pKiirus
                elif event.key == pygame.K_LEFT:
                    pAsukoht -= pKiirus

        elif labi == 1:  # Kui mäng on lõppenud
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    # kui Enter vajutatakse, alustame mängu uuesti
                    labi = 0
                    skoor = 0  # Resetteerime skoori mängu alguses
                    korgus1, korgus2, korgus3 = määrake_korgused()  # määrame igal korral uued kõrgused
                    alg1 = 180, korgus1
                    alg2 = 300, korgus2
                    alg3 = 420, korgus3
                elif event.key == pygame.K_ESCAPE:
                    # kui Escape vajutatakse, mäng suletakse
                    pygame.quit()
                    sys.exit()

        # vasaku tee poole kontroll punase auto jaoks
        if pAsukoht < 138:
            pAsukoht += pKiirus
        # parema tee poole kontroll punase auto jaoks
        elif pAsukoht > 453:
            pAsukoht -= pKiirus

    # ekraani peal oleva uuendamine
    pygame.display.flip()