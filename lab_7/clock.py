import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("Mickey Clock")

rightarm = pygame.image.load("min_hand.png")
leftarm = pygame.image.load("sec_hand.png")
mainclock = pygame.transform.scale(pygame.image.load("clock.png"), (650, 500))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    minute_angle = minute * 6 + (second / 60) * 6  
    second_angle = second * 6 
    
    screen.fill((255, 255, 255))
    screen.blit(mainclock, (75, 50))

    rotated_rightarm = pygame.transform.rotate(rightarm, -minute_angle-54)
    rightarm_rect = rotated_rightarm.get_rect(center=(400, 300)) 
    screen.blit(rotated_rightarm, rightarm_rect) 
    
    rotated_leftarm = pygame.transform.rotate(leftarm, -second_angle-105)
    leftarm_rect = rotated_leftarm.get_rect(center=(400, 300))
    screen.blit(rotated_leftarm, leftarm_rect)
    
    pygame.display.update()

    clock.tick(60)