import pygame
import random
import sys
import time

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision")
clock = pygame.time.Clock()

#create main rectangle
rect_1 = pygame.Rect(0, 0, 25, 25)

posX, posY = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
speedX, speedY = 0, 0
directionX, directionY = 0, 0

#create empty list, then create 16 obstacle rectangles using a loop and add to list
obstacles = []
for _ in range(16):
  obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
  obstacles.append(obstacle_rect)

#define colours
BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


run = True
while run:
    clock.tick(60)
  #update background
    screen.fill(BG)

  #check collision and change colour
    col = GREEN
    for obstacle in obstacles:
        if rect_1.colliderect(obstacle):
            col = RED


  #draw all rectangles
    pygame.draw.rect(screen, col, rect_1)
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle,)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speedX = 3
            elif event.key == pygame.K_LEFT:
                speedX = -3
            elif event.key == pygame.K_UP:
                speedY = -3
            elif event.key == pygame.K_DOWN:
                speedY = 3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                speedX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speedY = 0

    posX += speedX
    posY += speedY
    rect_1 = pygame.draw.rect(screen, col, [posX, posY, 30, 30])
  #update display
    pygame.display.flip()
    screen.fill(BLUE)

    if col == RED:
        time.sleep(2)
        pygame.quit()
        sys.exit()

pygame.quit()