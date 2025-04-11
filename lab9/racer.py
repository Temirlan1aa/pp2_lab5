import pygame 
import sys
import random
import time
from pygame.locals import *

pygame.init() 

enemy_image = "Enemy.png"
player_image = "Player.png"
background = pygame.image.load("AnimatedStreet.png")
coin_image = pygame.image.load("coin.png")
crash_sound = "crash.wav"
background_music = "background.wav"


black = (0, 0, 0)
white = (255, 255, 255)
Gray = (128, 128, 128)
Red = (255, 0, 0)

width, height = 400, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Race")

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("GAME OVER", True, black)

score = 0
coins_collected = 0
speed = 5
coin_timer = 0
coin_weights = [1, 2, 3]  
speed_boost_threshold = 10 

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(enemy_image)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score 
        self.rect.move_ip(0, speed)
        if self.rect.bottom > height:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            score += 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(player_image)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and (pressed_keys[K_LEFT] or pressed_keys[K_a]):
            self.rect.move_ip(-5, 0)
        if self.rect.right < width and (pressed_keys[K_RIGHT] or pressed_keys[K_d]):
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(coin_image, (30, 30))
        self.rect = self.image.get_rect()
        self.weight = random.choice(coin_weights)
        self.reset()

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.bottom > height:
            self.reset()

    def reset(self):
        self.rect.center = (random.randint(30, 370), random.randint(-100, -40))
        self.weight = random.choice(coin_weights)

P = Player()
E = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E)

coins = pygame.sprite.Group()
for _ in range(3):  
    coin = Coin()
    coins.add(coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(P, E, *coins)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

FPS = pygame.time.Clock()
pygame.mixer.Sound(background_music).play(-1) 

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.1 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.blit(background, (0, 0))

    scores = font_small.render(f"Score: {score}", True, black)
    coins_text = font_small.render(f"Coins: {coins_collected}", True, black)
    display.blit(scores, (10, 10))
    display.blit(coins_text, (10, 30))

    for entity in all_sprites:
        display.blit(entity.image, entity.rect)
        entity.move()

    for coin in coins:
        if pygame.sprite.collide_rect(P, coin):
            coins_collected += coin.weight
            coin.reset()

            if coins_collected >= speed_boost_threshold:
                speed += 1
                speed_boost_threshold += 10  

    if pygame.sprite.spritecollideany(P, enemies):
        pygame.mixer.Sound(crash_sound).play()
        time.sleep(0.5)

        display.fill(Red)
        display.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FPS.tick(60)
