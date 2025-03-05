import pygame
import random
import sys # juurde lisatud
pygame.init()

#värvid
red = [255, 0, 0]
lGreen = [153, 255, 153]

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill(lGreen)

for i in range (1,10):
    x = random.randint(0, 620)
    y = random.randint(0, 460)
    pygame.draw.rect(screen, red, [x, y, 20, 20])

    pygame.display.flip()

# sulgemine juurde lisatud, et ruute oleks näha
while True:
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()

pygame.quit()