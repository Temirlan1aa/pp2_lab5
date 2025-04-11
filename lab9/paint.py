import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint App")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

bg_color = WHITE
color = BLACK
radius = 5

mode = 'brush'
drawing = False
start_pos = None

font = pygame.font.SysFont(None, 24)

def draw_ui():
    pygame.draw.rect(screen, RED,   (10, 10, 30, 30))
    pygame.draw.rect(screen, GREEN, (50, 10, 30, 30))
    pygame.draw.rect(screen, BLUE,  (90, 10, 30, 30))
    pygame.draw.rect(screen, BLACK, (130, 10, 30, 30))
    pygame.draw.rect(screen, (200, 200, 200), (170, 10, 80, 30))
    eraser_text = font.render("Eraser", True, BLACK)
    screen.blit(eraser_text, (175, 15))
    mode_text = font.render(f"Mode: {mode}", True, BLACK)
    size_text = font.render(f"Brush size: {radius}", True, BLACK)
    screen.blit(mode_text, (270, 10))
    screen.blit(size_text, (270, 35))

screen.fill(bg_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                mode = 'brush'
            elif event.key == pygame.K_r:
                mode = 'rect'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_s:
                mode = 'square'
            elif event.key == pygame.K_t:
                mode = 'triangle_right'
            elif event.key == pygame.K_h:
                mode = 'rhombus'
            elif event.key == pygame.K_w:
                mode = 'triangle_eq'
            elif event.key == pygame.K_UP:
                radius = min(100, radius + 1)
            elif event.key == pygame.K_DOWN:
                radius = max(1, radius - 1)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 10 <= x <= 40 and 10 <= y <= 40:
                color = RED
                mode = 'brush'
            elif 50 <= x <= 80 and 10 <= y <= 40:
                color = GREEN
                mode = 'brush'
            elif 90 <= x <= 120 and 10 <= y <= 40:
                color = BLUE
                mode = 'brush'
            elif 130 <= x <= 160 and 10 <= y <= 40:
                color = BLACK
                mode = 'brush'
            elif 170 <= x <= 250 and 10 <= y <= 40:
                color = bg_color
                mode = 'eraser'
            else:
                drawing = True
                start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos
                if mode == 'rect':
                    pygame.draw.rect(screen, color, (x1, y1, x2 - x1, y2 - y1), radius)
                elif mode == 'square':
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(screen, color, (x1, y1, side * (1 if x2 > x1 else -1), side * (1 if y2 > y1 else -1)), radius)
                elif mode == 'circle':
                    rad = int(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, rad, radius)
                elif mode == 'triangle_right':
                    points = [start_pos, (x1, y2), (x2, y2)]
                    pygame.draw.polygon(screen, color, points, radius)
                elif mode == 'triangle_eq':
                    height = (3**0.5 / 2) * abs(x2 - x1)
                    top = (x1 + (x2 - x1) / 2, y1)
                    left = (x1, y1 + height)
                    right = (x2, y1 + height)
                    pygame.draw.polygon(screen, color, [top, left, right], radius)
                elif mode == 'rhombus':
                    mid_x = (x1 + x2) / 2
                    mid_y = (y1 + y2) / 2
                    points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
                    pygame.draw.polygon(screen, color, points, radius)

            drawing = False
            start_pos = None

        elif event.type == pygame.MOUSEMOTION:
            if drawing and mode in ['brush', 'eraser']:
                mx, my = event.pos
                pygame.draw.circle(screen, color, (mx, my), radius)

    draw_ui()
    pygame.display.flip()
    clock.tick(60)
