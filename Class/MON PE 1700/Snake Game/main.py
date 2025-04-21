import pygame
import sys
import random
from pygame import Vector2

class Snake :
    def __init__(self) :
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self) :
        for block in self.body :
            block_rect = pygame.Rect(block.x*CELL_SIZE, block.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (183, 191, 122), block_rect)

    def move_snake(self) :
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0]+self.direction)
        self.body = body_copy

class Fruit :
    def __init__(self) :
        # create x and y pos
        self.x = random.randint(0, CELL_NUMBER-1)
        self.y = random.randint(0, CELL_NUMBER-1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self) :
        # draw a square
        fruit_rect = pygame.Rect(self.pos.x*CELL_SIZE, self.pos.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

# Main program
pygame.init()
CELL_SIZE = 40
CELL_NUMBER = 20
screen = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE, CELL_NUMBER*CELL_SIZE))
clock = pygame.time.Clock()

fruit = Fruit()
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True :
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            pygame.quit()
            sys.exit()

    # Game Logic
    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()

    pygame.display.update()
    clock.tick(60)
