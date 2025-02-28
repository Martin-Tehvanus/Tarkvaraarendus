# impordid
import pygame
import sys

# käivitus
pygame.init()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Ülesanne 3")
screen.fill([153, 255, 153])

## kood

# kasutaja sisestused
rsuur = int(input("Sisesta ruudu küljepikkus pikslites: "))
rarv = int(input("Sisesta ridade arv: "))
varv = int(input("Sisesta veergudee arv: "))
# joone värv
jvrv_sises = input("Sisesta joone värv (r,g,b): ")
jvrv_vrts = jvrv_sises.split(',')
jvrv = (int(jvrv_vrts[0]), int(jvrv_vrts[1]), int(jvrv_vrts[2]))

# joonistamise funktsioon
def ruutude_joonistamine(screen, rsuur, rarv, varv, jvrv):
    for rida in range(rarv):
        for veerg in range(varv):
            x = veerg * rsuur  # veergude jaoks kasutame x-koordinaati
            y = rida * rsuur   # ridade jaoks kasutame y-koordinaati
            pygame.draw.rect(screen, jvrv, (x, y, rsuur, rsuur), 1)

# asjade joonistamine ekraanile
ruutude_joonistamine(screen, rsuur, rarv, varv, jvrv)
print("Joonistamine on valmis, mine pygamei aknale")

# lõpetus
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()

pygame.quit()