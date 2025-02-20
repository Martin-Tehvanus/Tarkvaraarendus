import pygame

pygame.init()

WIDTH, HEIGHT = 300, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Foor - Martin Tehvanus")

gray = (128, 128, 128)
traffic_colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0)]
flag_colors = [(0, 51, 153), (0, 0, 0), (255, 255, 255)]

circle_radius = 40

box_width, box_height = 100, 270
box_x = (WIDTH - box_width) // 2
box_y = 105

circle_positions = [
    (150, 65 + 90),
    (150, 150 + 90),
    (150, 235 + 90)
]

post_width = 20
post_height = 40
post_x = 150 - post_width // 2
post_y = box_y + box_height

base_height = 25
base_width = 80
base_top_y = post_y + post_height
base_bottom_y = base_top_y + base_height
top_width = base_width - 2 * base_height

base_polygon = [
    (150 - top_width // 2, base_top_y),
    (150 + top_width // 2, base_top_y),
    (150 + base_width // 2, base_bottom_y),
    (150 - base_width // 2, base_bottom_y)
]

def get_boundary_points(y, top_y, left_top, right_top):
    left = left_top - (y - top_y)
    right = right_top + (y - top_y)
    return left, right

left_top_base = 150 - top_width // 2
right_top_base = 150 + top_width // 2

y1 = base_top_y + 8
y2 = y1 + 8
y3 = base_bottom_y

lt1, rt1 = get_boundary_points(base_top_y, base_top_y, left_top_base, right_top_base)
lt1_b, rt1_b = get_boundary_points(y1, base_top_y, left_top_base, right_top_base)
stripe1 = [
    (lt1, base_top_y),
    (rt1, base_top_y),
    (rt1_b, y1),
    (lt1_b, y1)
]

lt2, rt2 = get_boundary_points(y1, base_top_y, left_top_base, right_top_base)
lt2_b, rt2_b = get_boundary_points(y2, base_top_y, left_top_base, right_top_base)
stripe2 = [
    (lt2, y1),
    (rt2, y1),
    (rt2_b, y2),
    (lt2_b, y2)
]

lt3, rt3 = get_boundary_points(y2, base_top_y, left_top_base, right_top_base)
lt3_b, rt3_b = get_boundary_points(y3, base_top_y, left_top_base, right_top_base)
stripe3 = [
    (lt3, y2),
    (rt3, y2),
    (rt3_b, y3),
    (lt3_b, y3)
]

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, gray, (post_x, post_y, post_width, post_height))
    pygame.draw.rect(screen, gray, (box_x, box_y, box_width, box_height), 2)

    for i, pos in enumerate(circle_positions):
        pygame.draw.circle(screen, traffic_colors[i], pos, circle_radius)

    pygame.draw.polygon(screen, flag_colors[0], stripe1)
    pygame.draw.polygon(screen, flag_colors[1], stripe2)
    pygame.draw.polygon(screen, flag_colors[2], stripe3)

    pygame.draw.polygon(screen, gray, base_polygon, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()