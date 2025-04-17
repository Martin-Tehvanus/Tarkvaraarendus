import pygame

pygame.init()

# värvid
red = [255, 0, 0]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Klaviatuuriga juhtimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

# koordinaadid ja kiirus
posX, posY = screenX / 2, screenY / 2
speedX, speedY = 0, 0

gameover = False
while not gameover:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speedX = 3
            elif event.key == pygame.K_LEFT:
                speedX = -3
            elif event.key == pygame.K_UP:
                speedY = -3
            elif event.key == pygame.K_DOWN:
                speedY = 3

    posX += speedX
    posY += speedY
    ruut = pygame.draw.rect(screen, red, [posX, posY, 30, 30])
    pygame.display.flip()
    screen.fill(lBlue)
pygame.quit()