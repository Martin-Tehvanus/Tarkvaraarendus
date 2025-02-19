# käivitus
import pygame
pygame.init()
pygame.font.init()
import math

## Kood allpool

# akna tegemine
ekr = pygame.display.set_mode( (640, 480) )
pygame.display.set_caption("Ülesanne 2")

# pildid
taust = pygame.image.load("yl2/bg_shop.jpg")
muua = pygame.image.load("yl2/seller.png")
tkstmull = pygame.image.load("yl2/chat.png")

# Lisaülesanne 2 pildid
vikk = pygame.image.load("yl2/VIKK logo.png")
tort = pygame.image.load("yl2/kook.png")
m66k = pygame.image.load("yl2/Mõõk.png")

# müüa ja tekstimull õigeks suuruseks tegemine
muua = pygame.transform.scale(muua, (int(muua.get_width() * 0.288), int(muua.get_height() * 0.288)))
tkstmull = pygame.transform.scale(tkstmull, (int(tkstmull.get_width() * 0.85), int(tkstmull.get_height() * 0.85)))

# Lisaülesanne 2 pildid õigeks suuruseks
vikk = pygame.transform.scale(vikk, (int(vikk.get_width() * 0.5), int(vikk.get_height() * 0.5)))
tort = pygame.transform.scale(tort, (int(tort.get_width() * 0.025), int(tort.get_height() * 0.025)))
m66k = pygame.transform.scale(m66k, (int(m66k.get_width() * 0.2), int(m66k.get_height() * 0.2)))

# pöörab mõõka
m66k = pygame.transform.rotate(m66k, -45)

# jätab akna avatuks kuni ristis kinni panna
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

## kuvab asjad ekraanil

# piltide kuvamine
    ekr.blit(taust, (0, 0))
    ekr.blit(muua, (105, 160)) # esimene vasakult-paremale , teine ülevalt-alla
    ekr.blit(tkstmull, (245, 65)) # esimene vasakult-paremale , teine ülevalt-alla

# Lisaülesanne 2 pildid
    ekr.blit(vikk, (0, 0))
    ekr.blit(tort, (300, 190))
    ekr.blit(m66k, (490, 100))

# tekst
    font = pygame.font.Font(None, 35)
    text = font.render("Tere, olen Martin", True, [255, 255, 255])
    ekr.blit(text, [270, 145])

# Lisaülesanne 2 tekst
    text = "TULEVIK 2050"
    cx, cy, r = 100, 50, 100
    start_angle = 180
    end_angle = 0
    step = (end_angle - start_angle) / (len(text) - 1)

    for i, char in enumerate(text):
        angle = math.radians(start_angle + i * step)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        ekr.blit(font.render(char, True, (255, 255, 255)), (x, y))

# akna uuendamine
    pygame.display.flip()

pygame.quit()
pygame.font.quit()
