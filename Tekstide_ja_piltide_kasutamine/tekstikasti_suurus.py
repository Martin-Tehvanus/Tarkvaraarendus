import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#lisame teksti
font = pygame.font.Font(pygame.font.match_font('arial'), 50)
text = font.render("Hello PyGame", True, [0,0,0])

#tekstikasti suurus
text_width = text.get_rect().width
text_height = text.get_rect().height

screen.blit(text, [320,240])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()