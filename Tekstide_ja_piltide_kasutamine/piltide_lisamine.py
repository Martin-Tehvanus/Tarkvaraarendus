import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#Lisame pildid
bg = pygame.image.load("img/bg.jpg")
youWin = pygame.image.load("img/youwin.png")
youWin = pygame.transform.scale(youWin, [300, 120])
screen.blit(bg,[0,0])
screen.blit(youWin,[180,100])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()

