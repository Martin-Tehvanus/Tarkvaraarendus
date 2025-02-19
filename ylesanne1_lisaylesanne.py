import pygame

pygame.init()

# aken
screen_width = 300
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Foor - Martin Tehvanus")

# värvid
gray = (128, 128, 128)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# ringi raadius
circle_radius = 40

# ringide asukohad
original_height = 300

circle_positions = [
    (screen_width // 2, int(original_height // 4.6)),
    (screen_width // 2, int(original_height // 2)),
    (screen_width // 2, int(2.2 * original_height // 2.8))
]

# valgusfoori kasti suurus ja positsioon
box_width = 100
box_height = 270
box_x = (screen_width - box_width) // 2
box_y = (original_height - box_height) // 2

# posti ja aluse asukohad
post_width = 20
post_height = 120
post_x = screen_width // 2 - post_width // 2
post_y = box_y + box_height  # algab foori alt

# Trapetsikujulise aluse nurgad
base_top_y = post_y + post_height  # posti lõpp
base_bottom_y = base_top_y + 30  # aluse põhi
base_width_top = 30  # ülemine kitsam osa
base_width_bottom = 60  # alumine laiem osa

base_points = [
    (screen_width // 2 - base_width_bottom // 2, base_bottom_y),  # vasak alumine
    (screen_width // 2 + base_width_bottom // 2, base_bottom_y),  # parem alumine
    (screen_width // 2 + base_width_top // 2, base_top_y),  # parem ülemine
    (screen_width // 2 - base_width_top // 2, base_top_y)   # vasak ülemine
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # värvib tausta mustaks
    screen.fill(black)

    # joonistab raami
    pygame.draw.rect(screen, gray, (box_x, box_y, box_width, box_height), 2)

    # joonistab posti
    pygame.draw.rect(screen, gray, (post_x, post_y, post_width, post_height))

    # joonistab postialuse ja täidab Eesti lipu värvidega
    pygame.draw.polygon(screen, blue, [  # Sinine ülemine osa
        (screen_width // 2 - base_width_bottom // 2, base_bottom_y - 20),
        (screen_width // 2 + base_width_bottom // 2, base_bottom_y - 20),
        (screen_width // 2 + base_width_top // 2, base_top_y),
        (screen_width // 2 - base_width_top // 2, base_top_y)
    ])
    pygame.draw.polygon(screen, black, [  # Must keskmine osa
        (screen_width // 2 - base_width_bottom // 2, base_bottom_y - 10),
        (screen_width // 2 + base_width_bottom // 2, base_bottom_y - 10),
        (screen_width // 2 + base_width_bottom // 2, base_bottom_y - 20),
        (screen_width // 2 - base_width_bottom // 2, base_bottom_y - 20)
    ])
    pygame.draw.polygon(screen, white, [  # Valge alumine osa
        (screen_width // 2 - base_width_bottom // 2, base_bottom_y),
        (screen_width // 2 + base_width_bottom // 2, base_bottom_y),
        (screen_width // 2 + base_width_bottom // 2, base_bottom_y - 10),
        (screen_width // 2 - base_width_bottom // 2, base_bottom_y - 10)
    ])

    # joonistab ringid
    for i, position in enumerate(circle_positions):
        color = red if i == 0 else yellow if i == 1 else green
        pygame.draw.circle(screen, color, position, circle_radius)

    # uuendab ekraani
    pygame.display.flip()

pygame.quit()