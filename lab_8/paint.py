import pygame
import sys

# === Инициализация ===
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint App")
clock = pygame.time.Clock()

# === Цвета ===
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

bg_color = WHITE
color = BLACK
radius = 5

# === Переменные для режимов ===
mode = 'brush'  # brush, rect, circle, eraser
drawing = False
start_pos = None

# === Интерфейс ===
font = pygame.font.SysFont(None, 24)

def draw_ui():
    pygame.draw.rect(screen, RED,   (10, 10, 30, 30))
    pygame.draw.rect(screen, GREEN, (50, 10, 30, 30))
    pygame.draw.rect(screen, BLUE,  (90, 10, 30, 30))
    pygame.draw.rect(screen, BLACK, (130, 10, 30, 30))

    # Кнопка "Ластик"
    pygame.draw.rect(screen, (200, 200, 200), (170, 10, 80, 30))
    eraser_text = font.render("Eraser", True, BLACK)
    screen.blit(eraser_text, (175, 15))

    # Подписи
    mode_text = font.render(f"Mode: {mode}", True, BLACK)
    size_text = font.render(f"Brush size: {radius}", True, BLACK)
    screen.blit(mode_text, (270, 10))
    screen.blit(size_text, (270, 35))

# === Основной цикл ===
screen.fill(bg_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # === Управление ===
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                mode = 'brush'
            elif event.key == pygame.K_r:
                mode = 'rect'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_UP:
                radius = min(100, radius + 1)
            elif event.key == pygame.K_DOWN:
                radius = max(1, radius - 1)

        # === Мышь нажата ===
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Палитра цветов
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

                if mode == 'rect':
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    width = x2 - x1
                    height = y2 - y1
                    pygame.draw.rect(screen, color, (x1, y1, width, height), radius)

                elif mode == 'circle':
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    rad = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, rad, radius)

            drawing = False
            start_pos = None

        elif event.type == pygame.MOUSEMOTION:
            if drawing and mode in ['brush', 'eraser']:
                mx, my = event.pos
                pygame.draw.circle(screen, color, (mx, my), radius)

    draw_ui()
    pygame.display.flip()
    clock.tick(60)
