import pygame

pygame.init()

# Экран
LENGTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("Game")

fill_color = (255, 255, 255)

circle_color = (0 , 0 , 0)
circle_x = 50
circle_y = 50
R = 25


step = 5

clock = pygame.time.Clock() 

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print(event)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and circle_y - R>= step:
        circle_y -= step
    if keys[pygame.K_s] and circle_y + R <= HEIGHT - step:
        circle_y += step
    if keys[pygame.K_a] and circle_x - R>= step:
        circle_x -= step
    if keys[pygame.K_d] and circle_x + R<= LENGTH - step:
        circle_x += step

    screen.fill(fill_color)

    pygame.draw.circle(screen , circle_color , (circle_x , circle_y) , 25)

    pygame.display.update()

    clock.tick(20)