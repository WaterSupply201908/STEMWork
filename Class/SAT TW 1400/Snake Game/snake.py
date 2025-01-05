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

  def draw_snake(self):
    for block in self.body:
      block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size,
                               cell_size, cell_size)
      pygame.draw.rect(screen, (183, 191, 122), block_rect)

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
    pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

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
