import pygame
from pygame import Vector2
import sys
import random


class MAIN:

  def __init__(self):
    self.snake = Snake()
    self.fruit = Fruit()

  def update(self):
    self.snake.move_snake()
    self.check_collision()
    self.check_fail()

  def draw_elements(self):
    self.fruit.draw_fruit()
    self.snake.draw_snake()

  def check_collision(self):
    if self.fruit.pos == self.snake.body[0]:
      self.fruit.randomize()
      self.snake.add_block()

  def game_over(self):
    pygame.quit()
    exit()

  def check_fail(self):
    if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[
        0].y < cell_number:
      self.game_over()

    for block in self.snake.body[1:]:
      if block == self.snake.body[0]:
        self.game_over()


class Snake:

  def __init__(self):
    self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
    self.direction = Vector2(-1, 0)
    self.new_block = False

    self.head_up = pygame.image.load('head_up.png').convert_alpha()
    self.head_down = pygame.image.load('head_down.png').convert_alpha()
    self.head_right = pygame.image.load('head_right.png').convert_alpha()
    self.head_left = pygame.image.load('head_left.png').convert_alpha()

    self.tail_up = pygame.image.load('tail_up.png').convert_alpha()
    self.tail_down = pygame.image.load('tail_down.png').convert_alpha()
    self.tail_right = pygame.image.load('tail_right.png').convert_alpha()
    self.tail_left = pygame.image.load('tail_left.png').convert_alpha()

    self.body_vertical = pygame.image.load('body_vertical.png').convert_alpha()
    self.body_horizontal = pygame.image.load('body_horizontal.png').convert_alpha()
  
  def update_head_graphics(self) :
    head_relation = self.body[1] - self.body[0]

    if head_relation == Vector2(1, 0) :
      self.head = self.head_left
    elif head_relation == Vector2(-1, 0) :
      self.head = self.head_right
    elif head_relation == Vector2(0, 1) :
      self.head = self.head_up
    elif head_relation == Vector2(0, -1) :
      self.head = self.head_down

  def update_tail_graphics(self) :
    tail_relation = self.body[-2] - self.body[-1]

    if tail_relation == Vector2(1, 0) :
      self.tail = self.tail_left
    elif tail_relation == Vector2(-1, 0) :
      self.tail = self.tail_right
    elif tail_relation == Vector2(0, 1) :
      self.tail = self.tail_up
    elif tail_relation == Vector2(0, -1) :
      self.tail = self.tail_down

  def draw_snake(self):
    self.update_head_graphics()
    self.update_tail_graphics()

    for index, block in enumerate(self.body) :
      block_rect = pygame.Rect(block.x * cell_size,
                               block.y * cell_size,
                               cell_size, cell_size)

      if index == 0 :
        screen.blit(self.head, block_rect)
      elif index == len(self.body) - 1 :
        screen.blit(self.tail, block_rect)
      else :
        previous_block = self.body[index + 1] - block
        next_block = self.body[index - 1] - block

        if previous_block.x == next_block.x :
          screen.blit(self.body_vertical, block_rect)
        elif previous_block.y == next_block.y :
          screen.blit(self.body_horizontal, block_rect)
    # for block in self.body:
    #  block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size,
    #                           cell_size, cell_size)
    #  pygame.draw.rect(screen, (183, 191, 122), block_rect)

  def move_snake(self):
    if self.new_block:
      body_copy = self.body[:]
      body_copy.insert(0, body_copy[0] + self.direction)
      self.body = body_copy
      self.new_block = False
    else:
      body_copy = self.body[:-1]
      body_copy.insert(0, body_copy[0] + self.direction)
      self.body = body_copy

  def add_block(self):
    self.new_block = True


class Fruit:

  def __init__(self):
    self.randomize()

  def draw_fruit(self):
    fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size,
                             cell_size, cell_size)
    screen.blit(apple, fruit_rect)
  # pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

  def randomize(self):
    self.x = random.randint(0, cell_number - 1)
    self.y = random.randint(0, cell_number - 1)
    self.pos = Vector2(self.x, self.y)


# Main program
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('apple.png').convert_alpha()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      pygame.quit()
      exit()
    if e.type == SCREEN_UPDATE:
      main_game.update()
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_UP:
        if main_game.snake.direction.y != 1:
          main_game.snake.direction = Vector2(0, -1)
      if e.key == pygame.K_RIGHT:
        if main_game.snake.direction.x != -1:
          main_game.snake.direction = Vector2(1, 0)
      if e.key == pygame.K_DOWN:
        if main_game.snake.direction.y != -1:
          main_game.snake.direction = Vector2(0, 1)
      if e.key == pygame.K_LEFT:
        if main_game.snake.direction.x != 1:
          main_game.snake.direction = Vector2(-1, 0)

  screen.fill((175, 215, 70))
  main_game.draw_elements()

  pygame.display.update()
  clock.tick(60)
