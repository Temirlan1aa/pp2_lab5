import pygame
import random
import sys
import time

CELL_SIZE = 20
WIDTH, HEIGHT = 600, 600
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)
        self.grow_flag = False

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False

    def grow(self):
        self.grow_flag = True

    def check_wall_collision(self):
        head_x, head_y = self.body[0]
        return not (0 <= head_x < COLS and 0 <= head_y < ROWS)

    def check_self_collision(self):
        return self.body[0] in self.body[1:]

    def draw(self, screen):
        for segment in self.body:
            x, y = segment
            pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self, snake_body):
        self.weight = random.choice([1, 2, 3])
        self.position = self.generate_position(snake_body)
        self.spawn_time = time.time()

    def generate_position(self, snake_body):
        while True:
            pos = (
                random.randint(0, COLS - 1),
                random.randint(0, ROWS - 1)
            )
            if pos not in snake_body:
                return pos

    def draw(self, screen):
        x, y = self.position
        color = RED if self.weight == 1 else (255, 165, 0) if self.weight == 2 else (255, 255, 0)
        pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def is_expired(self, duration=5):
        return time.time() - self.spawn_time > duration

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake OOP - Extended")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.score = 0
        self.level = 1
        self.speed = 5
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                    self.snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                    self.snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                    self.snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                    self.snake.direction = (1, 0)

    def update(self):
        self.snake.move()
        if self.snake.check_wall_collision() or self.snake.check_self_collision():
            print("Game Over")
            self.running = False
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.score += self.food.weight
            self.food = Food(self.snake.body)
            if self.score // 4 + 1 > self.level:
                self.level += 1
                self.speed += 2
        if self.food.is_expired():
            self.food = Food(self.snake.body)

    def draw_ui(self):
        score_text = self.font.render(f"Score: {self.score}  Level: {self.level}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def render(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.draw_ui()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(self.speed)
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
