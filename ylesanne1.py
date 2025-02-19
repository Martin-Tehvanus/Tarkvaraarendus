import pygame

pygame.init()

# aken
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Foor - Martin Tehvanus")

# värvid
gray = (128, 128, 128)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# ringi raadius
circle_radius = 40

# ringide asukohad
circle_positions = [
    (screen_width // 2, screen_height // 4.6),
    (screen_width // 2, screen_height // 2),
    (screen_width // 2, 2.2 * screen_height // 2.8)
]

# valgusfoori kasti suurus ja positsioon
box_width = 100
box_height = 270
box_x = (screen_width - box_width) // 2
box_y = (screen_height - box_height) // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # värvib tausta mustaks
    screen.fill(black)

    # joonistab raami
    pygame.draw.rect(screen, gray, (box_x, box_y, box_width, box_height), 2)

    # joonistab ringid
    for i, position in enumerate(circle_positions):
        color = red if i == 0 else yellow if i == 1 else green
        pygame.draw.circle(screen, color, position, circle_radius)

    # uuendab ekraani
    pygame.display.flip()

pygame.quit()