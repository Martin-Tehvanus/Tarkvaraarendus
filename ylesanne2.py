# käivitus
import pygame
pygame.init()
pygame.font.init()

## Kood allpool

# akna tegemine
ekr = pygame.display.set_mode( (640, 480) )
pygame.display.set_caption("Ülesanne 2")

# pildid
taust = pygame.image.load("yl2/bg_shop.jpg")
muua = pygame.image.load("yl2/seller.png")
tkstmull = pygame.image.load("yl2/chat.png")

# müüa ja tekstimull õigeks suuruseks tegemine
muua = pygame.transform.scale(muua, (int(muua.get_width() * 0.288), int(muua.get_height() * 0.288)))
tkstmull = pygame.transform.scale(tkstmull, (int(tkstmull.get_width() * 0.85), int(tkstmull.get_height() * 0.85)))

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

# tekst
    font = pygame.font.Font(None, 35)
    text = font.render("Tere, olen Martin", True, [255, 255, 255])
    ekr.blit(text, [270, 145])

# akna uuendamine
    pygame.display.flip()

pygame.quit()
pygame.font.quit()