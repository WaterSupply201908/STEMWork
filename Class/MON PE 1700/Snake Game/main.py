import pygame
import sys
import random
from pygame import Vector2

class Main :
    def __init__(self) :
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self) :
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self) :
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self) :
        if self.fruit.pos == self.snake.body[0] :
            self.fruit.randomize()
            self.snake.add_block()

class Snake :
    def __init__(self) :
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self) :
        for block in self.body :
            block_rect = pygame.Rect(block.x*CELL_SIZE, block.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (183, 191, 122), block_rect)

    def move_snake(self) :
        if self.new_block :
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0]+self.direction)
            self.body = body_copy
        else :
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0]+self.direction)
            self.body = body_copy

    def add_block(self) :
        self.new_block = True

class Fruit :
    def __init__(self) :
        # create x and y pos
        self.randomize()

    def draw_fruit(self) :
        # draw a square
        fruit_rect = pygame.Rect(self.pos.x*CELL_SIZE, self.pos.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

    def randomize(self) :
        self.x = random.randint(0, CELL_NUMBER-1)
        self.y = random.randint(0, CELL_NUMBER-1)
        self.pos = Vector2(self.x, self.y)

# Main program
pygame.init()
CELL_SIZE = 40
CELL_NUMBER = 20
screen = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE, CELL_NUMBER*CELL_SIZE))
clock = pygame.time.Clock()

#fruit = Fruit()
#snake = Snake()
main = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True :
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if e.type == SCREEN_UPDATE :
            #snake.move_snake()
            main.update()
        if e.type == pygame.KEYDOWN :
            if e.key == pygame.K_UP :
                main.snake.direction = Vector2(0, -1)
            if e.key == pygame.K_DOWN :
                main.snake.direction = Vector2(0, 1)
            if e.key == pygame.K_LEFT :
                main.snake.direction = Vector2(-1, 0)
            if e.key == pygame.K_RIGHT :
                main.snake.direction = Vector2(1, 0)

    # Game Logic
    screen.fill((175, 215, 70))
#    fruit.draw_fruit()
#    snake.draw_snake()
    main.draw_elements()

    pygame.display.update()
    clock.tick(60)
